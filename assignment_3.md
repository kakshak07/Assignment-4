In the baseline and HMM Trigram model there are different files:

Baseline.py
Baseline Model: It contains two functions, one function to just simply generate the tokens with categories _RARE_. 
We predict emission probabilities for words in the test data that do not occur in the training data. In the baseline,
there is a function to deal with creating files gene_dev.p1.out

count_freqs.py:
To create the count. gene, once we replace with categories we can run this file to generate counts, this takes two arguments.


Eval_gene_tagger.py:

This takes two files as an argument generates precision, recall, and F-1 Score

Replacing_rare.py:
In this file, you need to write for which file you need to replace with rare. In this file, there is also a function that explicitly handles creating subcategories like numeric, lower, upper, and rare.

Train_t.py:

This file is to convert the train. gene to corresponding words, to check scores on the train, this will generate a train tokens file.

viterbi_hmm_tri.py:
In the start of viterbi implementation file I have imported few files which are required for running the code. This import function from other files. This file contains the Viterbi implementation. There is a function for computing joint probability distribution, emission probability. In this, two functions handle both cases for infrequent words. emissionprobs_rare_class: which handles trigram with normal RARE. This file import functions from other files, which are required for running the file. Count dict of trained data is built with replacin_rare.py file.

Extension.py:
In extension.py I am using Laplace smoothing which applies smoothing on trigram implementation. In this file there are two files which handles both RARE and subcategories of RARE.

Different .txt files

gene_dev.p1.out: This file contains tags of predicted tags of gene.dev with baseline model

gene_dev.p3.out: This file contains tags of predicted tags of gene.dev with viterbi model

gene_rare.counts: This file containes information of word tags, counts and ngrams

gene_train.p1.out:  This file contains tags of predicted tags of gene.train with baseline model

gene.counts: Continas original counts

gene.dev: Conatins words for which tags need to be predicted

gene.key: Contains original tags of gene.dev

gene.train: contains word and tags for training

gene.train_rare: This file contains tags of predicted tags of gene.train with baseline model

gene.train_t: contains tags for testing the train file