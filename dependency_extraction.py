import stanfordnlp
from typing import TextIO
import re

# initialize stanfordnlp pipeline
nlp = stanfordnlp.Pipeline(processors='tokenize,pos,depparse',
                           use_gpu=True)

noncore_relations = {'obl', 'vocative', 'expl', 'dislocated', 'advcl', 'advmod',
                     'nmod', 'appos', 'acl', 'amod', 'cc', 'conj', 'case',
                     'det', 'flat', 'nmod:poss', 'punct', 'mark', 'compound'
                     }


def extract_sentence_core(text: str, full: TextIO, core: TextIO):
    """ extracts the dependencies of text, writes them to a file,
        and writes the sentence core to anothe file.
    """
    
    doc = nlp(text)
    for sentence in doc.sentences:
    
        reduced = []
        # process the dependency of each token
        for dep in sentence.dependencies:
            
            token = dep[2].text
            relation = dep[1]
            
            if relation not in noncore_relations:
                reduced.append(token)
    
        # print dependencies to a file
        sentence.print_dependencies(file=full)
        print(file=full, flush=True)  # separates each sentence
    
        # print the sentence core to a file
        print(' '.join(reduced) + '.', file=core, flush=True)
        
    print('-', file=full, flush=True)  # separates each file
    print(file=core, flush=True)  # separates each file
    
    
if __name__ == '__main__':
    
    # cleaned_texts.txt       - all abstracts
    # sentence_cores.txt      - sentence cores
    # full_dependencies.txt   - detailed dependencies of each sentence
    with open("data/cleaned_texts.txt", 'r') as document, \
            open("output/full_dependencies.txt", 'w+') as full_file, \
            open("output/sentence_cores.txt", 'w+') as core_file:
        
        paragraph = ""
        i = 1
        
        # pattern matching "molecular diagnosis"
        mlc_dig_pt = re.compile(r'[m|M]olecular.*?\n*?[d|D]iagnosis')
        
        for line in document:
                
            if line == '\n':
                print(f"Processing file {i}")
                
                # extract sentence core only if it entails molecular diagnosis
                if mlc_dig_pt.search(paragraph):
                    print(f"File {i} entails molecular diagnosis.")
                    extract_sentence_core(paragraph, full_file, core_file)
                    
                i += 1
                paragraph = ""  # reset paragraph
            else:
                paragraph += line
