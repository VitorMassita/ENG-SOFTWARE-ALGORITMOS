frase=str(input("DIGITE UMA PALAVRA: "))
cont=0
contvogal=0
contconso=0
contspace=0
while cont != len(frase):
    print(cont,":","\t",frase[cont])
    if frase[cont] == "a" or frase[cont] =="e"or frase[cont] =="i"or frase[cont] =="o"or frase[cont] =="u":
        contvogal = contvogal + 1
    if frase[cont]== " ":
        contspace = contspace + 1
    cont +=1
print(f"TEM: {contvogal:0.0f} VOGAIS e {contspace:0.0f} ESPACOS EM BRANCO\nNESSA FRASE TEM {cont:0.0f}CARACTERES")