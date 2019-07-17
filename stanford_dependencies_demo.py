import stanfordnlp

# Simple demo of StanfordNLP Python package
nlp = stanfordnlp.Pipeline(processors='tokenize,pos,depparse',
                           use_gpu=True)

doc = nlp("""
Tuberculosis, disease caused by Mycobacterium tuberculosis, is currently the
leading cause of death by a single infectious agent worldwide. Early, rapid and
accurate identification of M. tuberculosis and the determination of drug
susceptibility is essential for the treatment and management of this disease.
Tuberculosis diagnosis is mainly based on chest radiography, smear microscopy and
bacteriological culture. Smear microscopy has variable sensitivity, mainly in
patients co-infected with the human immunodeficiency virus (HIV). Conventional
culture for M. tuberculosis isolation, identification and drug susceptibility
testing requires several weeks owning to the slow growth of M. tuberculosis. The
delay in the time to results drives the prolongation of potentially inappropriate
antituberculosis therapy contributing to the emergence of drug resistance,
reducing treatment options and increasing treatment duration and associated
costs, resulting in increased mortality and morbidity. For these reasons, novel
diagnostic methods are need for timely identification of M. tuberculosis and
determination of the antibiotic susceptibility profile of the infecting strain.
Molecular methods offer enhanced sensitivity and specificity, early detection and
the capacity to detect mixed infections. These technologies have improved
turnaround time, cost effectiveness and are amenable for point-of-care testing.
However, although these methods produce results within hours from sample
collection, the phenotypic susceptibility testing is still needed for the
determination of drug susceptibility and quantify the susceptibility levels of a
given strain towards individual antibiotics. This review presents the history,
advances and forthcoming promises in the molecular diagnosis of tuberculosis. An
overview on the general principles, diagnostic value and the main advantages and
disadvantages of the molecular methods used for the detection and identification
of M. tuberculosis and its associated disease, is provided. It will be also
discussed how the current phenotypic methods should be used in combination with
the genotypic methods for rapid antituberculosis susceptibility testing.""")

# write dependencies to a file
with open("output/dependencies.txt", 'w+') as outfile:
    for sentence in doc.sentences:
        
        # print dependencies to the file
        sentence.print_dependencies(file=outfile)
        print(file=outfile)  # print a line to separate each sentence
