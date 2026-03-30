nvirgula=0
nponto=0
ninterro=0
nhash=0
conttotal=0
pos=0
palavra=str(input("DIGITE A PALAVRAA SER UTILIZADA: "))
print("*"*100)
frasealuno=str(input("DIGITE A FRASE COM A PALAVRA: "))

while conttotal!=len(frasealuno):
    conttotal+=1
    if frasealuno[pos]==",":
        nvirgula+=1
    elif frasealuno[pos]==".":
        nponto+=1
    elif frasealuno[pos]=="?":
        ninterro+=1
    elif frasealuno[pos]=="#":
        nhash+=1
    pos+=1
print("A VIRGULA REPRESENAa: ",nvirgula/len(frasealuno)*100)
print("O PONTO REPRESENTA: ",nponto/len(frasealuno)*100)
print("A INTERROGACAO REPRESENTA: ",ninterro/len(frasealuno)*100)
print("A HASHTAG REPRESENTA: ",nhash/len(frasealuno)*100)