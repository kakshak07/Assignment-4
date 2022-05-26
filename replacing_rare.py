from collections import defaultdict
import count_freqs
import baseline
import train_t
from collections import defaultdict
def count_words(lines):
    dict_count_word=defaultdict()
    for i in range(len(lines)):
        line=lines[i].strip()
        if(line):
            a=line.split(" ")
            if(a[0] in dict_count_word):
                dict_count_word[a[0]]+=1
            else:
                dict_count_word[a[0]]=1
    return(dict_count_word)

def create_file_rare(lines,count_wor):
    rare_file=open("gene.train_rare","w")
    for i in range(len(lines)):
        line=lines[i].strip()
        if(line):
            app_line=line.split(" ")
            if(count_wor[app_line[0]]<5):
                rare_file.write("_RARE_ "+app_line[1]+"\n")
            else:
                rare_file.write(line+"\n")
        else:
            rare_file.write("\n")     


def create_file_rare_classes(lines,count_wor):
    rare_file=open("gene.train_rare","w")
    for i in range(len(lines)):
        line=lines[i].strip()
        if(line):
            app_line=line.split(" ")
            if(count_wor[app_line[0]]<5):
                if(count_wor[app_line[0]].isNumeric()):
                    rare_file.write("_NUME_ "+app_line[1]+"\n")
                elif(count_wor[app_line[0]].isLower()):
                    rare_file.write("_LOWER_ "+app_line[1]+"\n")
                elif(count_wor[app_line[0]].isUpper()):
                    rare_file.write("_UPPER_ "+app_line[1]+"\n")
                else:
                    rare_file.write("_RARE_ "+app_line[1]+"\n")
            else:
                rare_file.write(line+"\n")
        else:
            rare_file.write("\n")  

with open("gene.train") as f:
    lines = f.readlines()    
count_wor=count_words(lines)
create_file_rare(lines,count_wor)



