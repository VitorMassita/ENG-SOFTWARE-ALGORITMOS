pos=0
espaco_branco=""
frase=str(input("DIGITE UMA FRASE: "))
while pos < len(frase):
    if frase[pos] != " ":
        print("POS = ", pos,"\t",frase[pos]) 
        espaco_branco = espaco_branco+ frase[pos]    
    pos+=1

print(espaco_branco)