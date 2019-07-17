import re
from typing import List


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
    
    # paragraphs that are DOI, PMCID, PMID info are not abstracts
    # pattern_doi = re.compile(r'')
    if paragraph[0].startswith("DOI:"):
        return False
    
    return True


def extract_abstracts(filename: str) -> List[str]:
    # list of abstracts
    abstracts = []
    
    # read the file
    with open(filename, 'r') as infile:
        chunk = []  # chunk of lines to form a paragraph
        
        for cur_line in infile:
            
            # a newline means it's the end of a paragraph
            if cur_line == '\n':
                
                if is_abstract(chunk):  # if this chunk is an abstract
                    
                    chunk = ''.join(chunk)  # join strings to form a paragraph
                    abstracts.append(chunk)  # add it to abstracts
                    print(chunk)
                    
                chunk = []  # reset chunk
                
            else:
                chunk.append(cur_line)  # append each line to chunk
    return abstracts


if __name__ == '__main__':
    useful_info = extract_abstracts("data/pubmed_result2018_abstract(1).txt")
    print(len(useful_info))
    
    # write to a new file
    with open('data/cleaned_texts.txt', 'w+') as outfile:
        for info in useful_info:
            outfile.write(info)
            outfile.write('\n')
