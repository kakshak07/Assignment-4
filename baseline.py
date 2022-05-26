from collections import defaultdict
unique_words=[]
def read_gene_counts(lines,count_word_tag):
    for i in range(len(lines)):
        line=lines[i].strip()
        line=line.split(" ")
        if(line[1]=="WORDTAG"):
            count_word_tag[(line[2],line[3])]=int(line[0])
            unique_words.append(line[3])
        elif(line[1]=="1-GRAM" and line[2]=="O"):
            first_tag=int(line[0])
        elif(line[1]=="1-GRAM" and line[2]=="I-GENE"):
            second_tag=int(line[0])
    return(first_tag,second_tag,count_word_tag)
def emission_probabilites(emission_max_tag,first_tag,second_tag,count_word_tag):
    for i in range(len(unique_words)):
        first_tag_emission_prob=count_word_tag[("O",unique_words[i])]/first_tag
        second_tag_emission_prob=count_word_tag[("I-GENE",unique_words[i])]/second_tag
        if(second_tag_emission_prob>first_tag_emission_prob):
            emission_max_tag[unique_words[i]]="I-GENE"
        else:
            emission_max_tag[unique_words[i]]="O"
def create_file(lines1):
    base_dev_file=open("gene_train.p1.out","w")
    for i in range(len(lines1)):
        line=lines1[i].strip()
        if(line):
            if(line in emission_max_tag):
                base_dev_file.write(line+" "+emission_max_tag[line]+"\n")
            else:
                base_dev_file.write(line+" "+emission_max_tag["_RARE_"]+"\n")
        else:
            base_dev_file.write("\n")


def create_file_classes(lines1):
    base_dev_file=open("gene_train.p1.out","w")
    for i in range(len(lines1)):
        line=lines1[i].strip()
        if(line):
            if(line in emission_max_tag):
                base_dev_file.write(line+" "+emission_max_tag[line]+"\n")
            else:
                if(line.isNumeric()):
                    base_dev_file.write(line+" "+emission_max_tag["_ISNUME_"]+"\n")
                elif(line.isLower()):
                    base_dev_file.write(line+" "+emission_max_tag["_LOWER_"]+"\n")
                elif(line.isUpper()):
                    base_dev_file.write(line+" "+emission_max_tag["_UPPER_"]+"\n")
                else:
                    base_dev_file.write(line+" "+emission_max_tag["_RARE_"]+"\n")
emission_max_tag=defaultdict(int)
with open("gene.counts") as f:
    lines = f.readlines()
with open("gene.train_t") as f1:
    lines1 = f1.readlines()
count_word_tag=defaultdict(int)
first_tag,second_tag,count_word_tag=read_gene_counts(lines,count_word_tag)
emission_probabilites(emission_max_tag,first_tag,second_tag,count_word_tag)
create_file(lines1)