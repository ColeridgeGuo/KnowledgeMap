# Simple usage
from stanfordcorenlp import StanfordCoreNLP as NLP

nlp = NLP(r'stanford-corenlp-full-2018-10-05',
          memory='4g')

document = """The prospects for Britain’s orderly withdrawal from the European
Union on March 29 have receded further, even as MPs rallied to stop a no-deal
scenario. An amendment to the draft bill on the termination of London’s
membership of the bloc obliges Prime Minister Theresa May to renegotiate her
withdrawal agreement with Brussels. A Tory backbencher’s proposal calls on the
government to come up with alternatives to the Irish backstop, a central tenet
of the deal Britain agreed with the rest of the EU."""

props = {'annotators': 'tokenize,ssplit,pos,ner',
         'pipelineLanguage': 'en',
         'outputFormat': 'text'}

print(nlp.annotate(document, properties=props))

nlp.close()
