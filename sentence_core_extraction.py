import stanfordnlp
from typing import List
from collections import namedtuple
import glob
import re

# initialize stanfordnlp pipeline
nlp = stanfordnlp.Pipeline(processors='tokenize,pos,depparse',
                           use_gpu=True)


def extract_sentence_core(text: str) -> List[str]:
    """ extract sentence cores for further relation extractions """
    
    doc = nlp(text)
    # namedtuple container for Word object
    Word = namedtuple('Word', 'text, index, governor, gov_index, relation')
    reduced_sentences = []
    
    for sentence in doc.sentences:
    
        words = []
        root = 0
        # process the dependency of each token
        for dep in sentence.dependencies:
            
            # specify what the root is
            if dep[1] == 'root':
                root = dep[2].index
            
            word = Word(dep[2].text, dep[2].index, dep[0].text, dep[0].index,
                        dep[1])
            words.append(word)
            
        # extract words that depend on root
        reduced = []
        for word in words:
            if (word.gov_index == root and word.relation != 'punct') or \
                    (word.relation == 'root'):
                reduced.append(word.text)
    
        # print the sentence core to a file
        reduced_sentences.append(' '.join(reduced) + '.\n')
    reduced_sentences.append('\n')
    return reduced_sentences
    
    
def extract_file(filename: str) -> List[str]:
    cores = []
    
    with open(filename, 'r') as document:
        paragraph = ""
        i = 1

        # process each line
        for line in document:
    
            # if at the end of a paragraph
            if line == '\n':
                print(f"    Processing file {i}")
                cores.extend(extract_sentence_core(paragraph))
        
                i += 1
                paragraph = ""  # reset paragraph
            else:
                paragraph += line  # append line to paragraph
                
    return cores
    
    
if __name__ == '__main__':
    
    # list of all text files containing abstracts
    file_list = glob.glob('data/cleaned texts/*.txt')
    
    for file in file_list:
        year = re.search(r'\d{4}', file)[0]
        print(f"Processing {year} files:")
        sentence_cores = extract_file(file)

        # write sentence cores to a file
        with open(f"output/sentence_cores_{year}.txt", 'w+') as core_file:
            for core in sentence_cores:
                core_file.write(core)
