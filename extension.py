from collections import defaultdict
tagwdict=defaultdict(int)
unidict=[]
word_of_tag=defaultdict(int)
def train_data(open_train):
    for l in open_train:
        line=l.strip().split(' ')
        if line[1] == 'WORDTAG':
            tagwdict[(line[3],line[2])]=int(line[0])
            unidict.append(line[3])
        else:
            if(line[1]=="1-GRAM"):
                word_of_tag[line[2]]=int(line[0])
            else:
                word_of_tag[line[2:]]=int(line[0])
def emissionprobs_rare_class(tagwdict,unidict,word_of_tag,x,y):
    if x in unidict:
        return(tagwdict[(x,y)]/word_of_tag[y])
    else:
        if(x.isNumeric()):
            return(tagwdict[('_NUME_',y)]/word_of_tag[y])
        elif(x.isLower()):
            return(tagwdict[('_LOWER_',y)]/word_of_tag[y])
        elif(x.isLower()):
            return(tagwdict[('_UPPER_',y)]/word_of_tag[y])
        else:
            return(tagwdict[('_RARE_',y)]/word_of_tag[y])
def extension_probabilities(tagwdict,unidict,word_of_tag,x,y):
    if x in unidict:
        return((tagwdict[(x,y)]+0.1)/(word_of_tag[y]+0.1*len(unidict)))
    else:
        return((tagwdict[('_RARE_',y)]+0.1)/(word_of_tag[y]+0.1*len(unidict)))
def viterbi_tri_hmm(tagwdict,unidict,word_of_tag,word_list):
    pi={(0,'*','*'): 1}
    word_list=['*','*']+word_list
    sequence_tags=('O','I-GENE')
    bi={}
    tag_list=('O','I-GENE')
    for k in range(1,len(word_list)):
        for u in tag_list:
            for v in tag_list:
                if word_list[k] in unidict:
                    emission=(tagwdict[(x,y)]+0.1)/(word_of_tag[y]+0.1*len(unidict))
                else:
                    emission=(tagwdict[('_RARE_',y)]+0.1)/(word_of_tag[y]+0.1*len(unidict))
                list_u_v_w=[]
                for w in tag_list:
                    list_u_v_w.append(((pi[k - 1,w,u] * ((word_of_tag[w,u,v]+0.1)/(word_of_tag[w,u]+0.1*len(unidict)))) * emission),w)
                p,b=sorted(list_u_v_w,lambda x: x[0])
                pi[k,u,v]=p
                bi[k,u,v]=b
    backtracing_tokens=[]
    for u in sequence_tags:
        for v in sequence_tags:
            backtracing_tokens.append((pi[len(word_list) - 1,u,v] * word_of_tag[u,v,"STOP"]/word_of_tag[u,v]),(u,v))
    rev_tag_first= p,b=sorted(backtracing_tokens,lambda x: x[0])[0][0]
    rev_tag_second=sorted(backtracing_tokens,lambda x: x[0])[0][1]
    tokens_tags_word=[0] * len(word_list)
    tokens_tags_word[-2]=rev_tag_first
    tokens_tags_word[-1]=rev_tag_second
    for i in range(len(tokens_tags_word)-1,0,-1):
        tokens_tags_word[i]=bi[i+2,tokens_tags_word[i+1],tokens_tags_word[i+2]]
    return(tokens_tags_word[2:])
def output_tags(gene_dev):
    word_list=[]
    output_file=open("gene_dev.p3.out","w")
    for l in gene_dev:
        line=l.strip()
        if line:
            word_list.append(line)
        else:
            tokens_tags_word=viterbi_tri_hmm(tagwdict,unidict,word_of_tag,word_list)
            for word in range(len(word_list)):
                output_file.write(word_list[word]+" "+tokens_tags_word[word]+"\n")
            output_file.write('\n')
            word_list=[]
open_train=open("gene.counts","r")
gene_dev=open("gene.dev",'r')
train_data(open_train)
output_tags(gene_dev)