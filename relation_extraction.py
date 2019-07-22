import stanfordnlp
from typing import TextIO
from collections import namedtuple
import re

# initialize stanfordnlp pipeline
nlp = stanfordnlp.Pipeline(processors='tokenize,pos,depparse',
                           use_gpu=True)


def extract_sentence_core(text: str):
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
    
    
if __name__ == '__main__':
    
    sentence_cores = []
    
    # cleaned_texts.txt     - all abstracts
    # sentence_cores.txt    - sentence cores
    with open("data/cleaned_texts.txt", 'r') as document, \
            open("output/sentence_cores.txt", 'w+') as core_file:
        
        paragraph = ""
        i = 1
        
        for line in document:
                
            if line == '\n':
                print(f"Processing file {i} \n")
                sentence_cores.extend(extract_sentence_core(paragraph))
                
                i += 1
                paragraph = ""  # reset paragraph
            else:
                paragraph += line
        
        for core in sentence_cores:
            core_file.write(core)
