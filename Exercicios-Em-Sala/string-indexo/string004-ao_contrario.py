frase=str(input("DIGITE UMA FRASE: "))
n = len(frase)
pos= n - 1
frase_con = ""
while pos >= 0:
    print("POS = ", pos,"\t",frase[pos])
    frase_con = frase_con+frase[pos]
    pos-=1
print(frase_con)