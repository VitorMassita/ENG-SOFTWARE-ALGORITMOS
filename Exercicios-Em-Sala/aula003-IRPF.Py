salario=float(input("Digite o Valor do Salario Bruto: "))
if salario <= 1903.98:
    aliquid=0
    impost=0
elif (salario > 1903.98) and (salario <= 2826.65):
    aliquid=142.80
    impost=7.5
elif (salario > 2826.65) and (salario <= 3751.05):
    aliquid=354.80 
    impost=15
elif (salario > 3751.05) and (salario <= 4664.68):
    aliquid=636.80 
    impost=22.5
else:
    impost=27.5 
    aliquid=869.64
liquid=(salario-(salario*impost/100))-aliquid
print("************************************************************")
print("Seu Salario Liquido é de: R$", liquid)