import stanfordnlp

# Simple demo of StanfordNLP Python package
nlp = stanfordnlp.Pipeline(processors='tokenize,pos,depparse',
                           use_gpu=True)

doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")

for sentence in doc.sentences:
    sentence.print_dependencies()
