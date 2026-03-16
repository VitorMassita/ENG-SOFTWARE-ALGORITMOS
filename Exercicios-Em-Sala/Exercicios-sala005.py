x=int(input("DIGITE O VALOR DE X: "))
xmax=-1000
ymax=-1000
while (x<10):
    print("*" * 30)
    y = -4*x**2 + 40*x 
    if (y>ymax):
        ymax=y
        xmax=x
    print(f"PARA X = {x:0.2f}, Y= {y:0.2f}") 
    x=x+1
print(f"O MAIOR VALOR DE Y É {ymax:0.1f}")
    