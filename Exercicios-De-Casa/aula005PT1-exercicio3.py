soma=0
count=0
nmax=0
nmin=100000
num=int(input("DIGITE A QUANTIDADE DE NUMEROS: "))
while count!=num:
    x=int(input("DIGITE UM NUMERO: "))
    soma=soma+x
    count=count+1
    if x > nmax:
        nmax = x
    elif x < nmin:
        nmin = x
    media=soma/num
print(f"A MEDIA DOS NUMEROS E {media:0.2f}, O MAIOR NUMERO E {nmax:0.0f} E O MENOR NUMERO E {nmin:0.0f}")