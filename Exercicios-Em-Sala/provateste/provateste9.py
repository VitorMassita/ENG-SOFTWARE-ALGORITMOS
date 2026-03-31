x=0
quant=0
try: 
    while x <=99:
        if x % 3 == 0:
            quant+=1
        x+=1     
    print(f"{quant:0.0f} NUMEROS SAO DIVISIVEIS POR 3")
except:
    print("OCORREU ALGUM ERRO")