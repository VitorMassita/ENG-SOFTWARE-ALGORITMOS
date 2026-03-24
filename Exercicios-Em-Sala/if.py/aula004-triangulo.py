l1=float(input("DIGITE O VALOR DO PRIMEIRO LADO: "))
print("**************************")
l2=float(input("DIGITE O VALOR DO SEGUNDO LADO: "))
print("**************************")
l3=float(input("DIGITE O VALOR DO TERCEIRO LADO: "))
print("**************************")
if l1==l2==l3:
    print("O TRIANGULO É EQUILATERO")
elif l1==l2 or l1==l3 or l2==l3: 
    print("O TRIANGULO É ISOSCELES")
else:
    print("O TRIANGULO É ESCALENO")