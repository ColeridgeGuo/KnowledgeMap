# Simple usage
from stanfordcorenlp import StanfordCoreNLP as NLP

props = {'annotators': 'tokenize,ssplit,pos',
         'pipelineLanguage': 'en',
         'outputFormat': 'json'}

nlp = NLP(r'stanford-corenlp-full-2018-10-05',
          memory='4g')

sentence = 'GDUFS is active in a full range of international cooperation and exchanges in education.'
print()
print('Tokenize:', nlp.word_tokenize(sentence))
print()
print('Part of Speech:', nlp.pos_tag(sentence))
print()
print('Named Entities:', nlp.ner(sentence))
print()
print('Constituency Parsing:\n', nlp.parse(sentence))
print()
print('Dependency Parsing:', nlp.dependency_parse(sentence))

nlp.close()
