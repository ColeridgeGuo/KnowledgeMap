import re

# list of articles
articles = []

# read the file
with open("pubmed_result2018_abstract(1).txt", 'r') as file:
    i = 0
    prev = ''
    chunk = ''
    for line in file:
        if line == prev == '\n':
            print(i)
            print("chunk:\n",chunk.rstrip())
            articles.append(chunk)
            chunk = ''
        else:
            chunk += line
            
        prev = line
        i += 1
