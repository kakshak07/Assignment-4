from collections import defaultdict
import count_freqs
import baseline
import train_t
open_train=open("gene.train","r")
train_t=open("gene.train_t","w")
for i in open_train:
    word=i.strip().split(" ")
    if(word):
        train_t.write(word[0])
    train_t.write("\n")