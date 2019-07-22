import re
from typing import List
import glob


def is_abstract(paragraph: List[str]) -> bool:
    """ Return if a paragraph is useful information or not
        including abstracts and titles
    """
    
    # paragraphs less than 3 lines are not likely to be an abstract
    if len(paragraph) < 3:
        return False
    
    # paragraphs that start with "Author information" are not abstracts
    if paragraph[0].startswith("Author information"):
        return False
    
    # paragraphs that are lists of authors are not abstracts
    pattern_authors = re.compile(r'\b.*?\b\(\d+\)')
    if pattern_authors.match(''.join(paragraph)):
        return False
    
    return True


def extract_abstracts(filename: str) -> List[str]:
    # list of abstracts
    abstracts = []
    
    # read the file
    with open(filename, 'r') as infile:
        chunk = []  # chunk of lines to form a paragraph
        
        for cur_line in infile:
            
            # some lines have words like PURPOSE, RESULTS, etc., at the
            # beginning of the line; theses words have to be removed
            match = re.match(r'^([A-Z/\s]+):\s(.*\n?)', cur_line)
            if match:
                # lines containing irrelevant info are removed
                ignore_kw = {'PMCID', 'PMID', 'DOI'}
                if match.group(1) not in ignore_kw:
                    chunk.append(match.group(2))
                    
            # a newline means it's the end of a paragraph
            elif cur_line == '\n':
                
                if is_abstract(chunk):  # if this chunk is an abstract
                    
                    chunk = ''.join(chunk)  # join strings to form a paragraph
                    abstracts.append(chunk)  # add it to abstracts
                    
                chunk = []  # reset chunk

            # all other cases, append the line to chunk
            else:
                chunk.append(cur_line)
    return abstracts


if __name__ == '__main__':
    
    # list of all text files containing abstracts
    file_list = glob.glob('data/original texts/*.txt')
    
    for file in file_list:
        
        year = re.search(r'\d{4}', file)[0]  # year of the articles
        # cleaned abstracts
        abstract_list = extract_abstracts(file)
        print(len(abstract_list))
        
        # write to a new file
        with open(f'data/cleaned texts/cleaned_texts_{year}.txt', 'w+') as outfile:
            for line in abstract_list:
                outfile.write(line)
                outfile.write('\n')
