idade=int
atividade=str
na=0
nm=0
nc=0
nidade=0
quantidade=0
npessoas=0
idademax=-1000
idademin=1000
try:
    while (atividade != 0) and (idade!=0):
        idade=int(input("DIGITE SUA IDADE: "))
        nidade=nidade+idade
        quantidade+=1
        if idade !=0:
            if idade>idademax:
                idademax=idade
            if idade<idademin:
                idademin=idade
            else:
                idademin=idademin
                idademax=idademax
        else:
            break
        atividade=str(input("[M]Montanha russa\n[A]Aventura(tirolesa,escalada, bungeejump)\n[C]Clásicos(Patinação,cavalgada,charrete, etc)\nDigite 0 para parar\nDIGITE SUA ATIVIDADE FAVORITA: "))
        npessoas+=1
        print("*" *100)
        print("OBRIGADO POR PARTICIPAR DA PESQUISA")
        print("*" *100)
        if atividade =="M":
            nm+=1
        elif atividade== "A":
            na+=1
        elif atividade=="C":
            nc+=1
        else:
            break
except ZeroDivisionError:
    print("DIGITE SOMENTE NUMEROS")
idademedia=nidade/quantidade
print((na/npessoas)*100,"porcento gostam de Aventura,", (nc/npessoas)*100,"porcento gostam de Classicos e ",(nm/npessoas)*100,"porcento gostam de Motanha Russa")
print("A MEDIA DE IDADE É DE ",idademedia)
print("A IDADE MAXIMA É DE: ", idademax)
print("A IDADE MINIMA É DE: ",idademin)