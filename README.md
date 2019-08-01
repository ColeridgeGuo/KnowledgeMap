# KnowledgeMap
Creating knowledge maps using StanfordCoreNLP

## text_processing.py
Process the list of articles to remove unuseful info, leave only abstracts for entity-relation extraction.

## sentence_core_extraction.py
Extract sentence cores to build relations between entities.

## stanford_ner_demo.py

A demo for Named-Entity Recognition parsing using `StanfordNERTagger` in the 
`nltk` package.

TO-DO: Stanford NER or POS taggers from `nltk.tag`, and avoid tokenizer from 
`nltk.tokenize` for they will be soon deprecated.

Instead use the new `nltk.parse.corenlp.CoreNLPParser` which can be found 
[here](https://github.com/nltk/nltk/wiki/Stanford-CoreNLP-API-in-NLTK).