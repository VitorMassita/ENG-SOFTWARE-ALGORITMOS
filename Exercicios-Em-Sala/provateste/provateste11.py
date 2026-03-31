pos=0
zerocinco=0
seisnove=0
frase=str(input("DIGITE UMA CADEIA DE CARACTERES NUMERICOS: "))
try: 
    while pos!=len(frase):
        if 0<=int(frase[pos]) <=5:
            zerocinco+=1
            pos+=1
        else:
            seisnove+=1
            pos+=1
except ValueError:
    print("VALOR INVALIDO")
print(f"NA CADEIA DE CARACTERES DIGITADOS HA {zerocinco:0.0f} CARACTERES ENTRE 0 E 5\nE HA {seisnove:0.0f} ENTRE 6 E 9")