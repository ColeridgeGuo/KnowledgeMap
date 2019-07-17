from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

"""
Specify model file in the STANFORD_MODELS environment varialbe:
    STANFORD_MODELS=/Users/yingxuanguo/Documents/BioTecan/KnowledgeMap/
    stanford-ner-2018-10-16/classifiers
    
Specify jar file in the CLASSPATH environment variable:
    CLASSPATH = /Users/yingxuanguo/Documents/BioTecan/KnowledgeMap/
    stanford-ner-2018-10-16/stanford-ner.jar
"""

# initialize NER-tagger with pre-trained model
st = StanfordNERTagger('english.muc.7class.distsim.crf.ser.gz')

text = """
While in France, Christine Lagarde discussed short-term stimulus
efforts in a recent interview with the Wall Street Journal.
"""

# tokenize into tokens
tokenized_text = word_tokenize(text)

# NER-tag each token
classified_text = st.tag(tokenized_text)

print(classified_text)
