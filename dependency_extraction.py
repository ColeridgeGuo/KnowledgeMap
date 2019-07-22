import stanfordnlp
from typing import TextIO
from collections import namedtuple
import re

# initialize stanfordnlp pipeline
nlp = stanfordnlp.Pipeline(processors='tokenize,pos,depparse',
                           use_gpu=True)

noncore_relations = {'obl', 'vocative', 'expl', 'dislocated', 'advcl', 'advmod',
                     'nmod', 'appos', 'acl', 'amod', 'cc', 'conj', 'case',
                     'det', 'flat', 'nmod:poss', 'punct', 'mark', 'compound'
                     }


def extract_sentence_core(text: str, core: TextIO = None):
    """ extracts the dependencies of text, writes them to a file,
        and writes the sentence core to anothe file.
    """
    
    doc = nlp(text)
    # namedtuple container for Word object
    Word = namedtuple('Word', 'text, index, governor, gov_index, relation')
    
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
        print(' '.join(reduced) + '.', file=core, flush=True)
        
    print(file=core, flush=True)  # separates each file
    
    
if __name__ == '__main__':
    
    # cleaned_texts.txt       - all abstracts
    # sentence_cores.txt      - sentence cores
    with open("data/cleaned_texts.txt", 'r') as document, \
            open("output/sentence_cores.txt", 'w+') as core_file:
        
        paragraph = ""
        i = 1
        
        for line in document:
                
            if line == '\n':
                print(f"Processing file {i} \n")
                extract_sentence_core(paragraph, core_file)
                
                i += 1
                paragraph = ""  # reset paragraph
            else:
                paragraph += line
