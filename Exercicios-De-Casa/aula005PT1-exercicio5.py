x=int(input("DIGITE O NUMERO PARA A TABUADA: "))
contador=10
resultado=0
while contador>0:
    resultado=x*contador
    contador=contador-1
    print(f"{resultado:.0f}")