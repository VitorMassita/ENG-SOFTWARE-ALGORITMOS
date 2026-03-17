n=int(input("DIGITE O NUMERO FATORIAL: "))
contador=n
resultado=1
while contador>0:
    resultado=resultado*contador
    contador=contador-1
print(f"Fatorial = {resultado:0.1f}")