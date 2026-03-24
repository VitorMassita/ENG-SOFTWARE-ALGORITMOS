vogais=""
consoantes=""
pos=0
nome=str(input("DIGITE UM NOME: "))
while pos != len(nome):
    print("POS = ", pos,"\t",nome[pos])
    if nome[pos] == "a" or nome[pos]=="e"or nome[pos] =="i"or nome[pos] =="o"or nome[pos] =="u":
        vogais=vogais+nome[pos]
        pos+=1
    else:
        consoantes=consoantes+nome[pos]
        pos+=1
print(f"A FRASE TEM: ", consoantes,"\ne", vogais)
