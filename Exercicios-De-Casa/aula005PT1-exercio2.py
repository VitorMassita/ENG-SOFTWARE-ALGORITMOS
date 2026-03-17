soma=0
count=0
num=int(input("DIGITE A QUANTIDADE DE NUMEROS: "))
while count!=num:
    x=int(input("DIGITE UM NUMERO: "))
    soma=soma+x
    count=count+1
media=soma/num
print(f"A MEDIA DOS NUMEROS E {media:0.2f}")