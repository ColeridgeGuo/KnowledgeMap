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
Cardiac channelopathies, mainly Long QT and Brugada syndromes, are genetic
disorders for which genotype/phenotypes relationships remains to be improved. To
provide new insights into the Brugada syndrome pathophysiology, a mutational
study was performed on a 64-year-old man presented with isolated exertional
dyspnea (NYHA class: II-III), hypertension, chronic kidney disease, coronary
disease, an electrocardiogram suggesting a Brugada type 1-like pattern with
ST-segment elevation in leads V1-V2. Molecular diagnosis study was performed
using molecular strategy based on the sequencing of a panel of 19
Brugada-associated genes. The proband was carrier of 2 TRPM4 null alleles
[IVS9+1G > A and p. Trp525X] resulting in the absence of functional hTRPM4
proteins. Due to this unexpected genotype, meta-analysis of previously reported
TRPM4 variations associated with cardiac pathologies was performed using ACMG
guidelines. All were detected in a heterozygous status. This additional
meta-analysis indicated that most of them could not be considered definitely as
pathogen. In conclusion, our study reports, for the first time, identification of
compound heterozygous TRPM4 null mutations in a proband with, at an
arrhythmogenic level, only a Brugada type 1-like electrocardiogram. By combining
the genotype/phenotype relationship of this case and analysis of previously
reported TRPM4 variations, we suggest that loss-of-function TRPM4 variations, in
a heterozygous status, could not be considered as pathogenic or likely pathogenic
mutations in cardiac channelopathies such as Long QT syndrome or Brugada
syndrome.
"""

# tokenize into tokens
tokenized_text = word_tokenize(text)

# NER-tag each token
classified_text = st.tag(tokenized_text)

for ner in classified_text:
    if ner[0] == '.':
        print('\n')
    else:
        print(*ner, end=' ')
