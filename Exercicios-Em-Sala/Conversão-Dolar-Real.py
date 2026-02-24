print("CALCULADORA DE CONVERSAO DOLAR-REAL")

dolar=float(input("QUANTOS DOLARES VOCE TEM: "))
cot=float(input("QUANTO ESTA A COTAÇAO DO DOLAR: "))
real=dolar*cot
print(f"VOCE TERA: {real:0.2f}")

print("VAMOS CALCULAR DE DOLARES PARA REAIS: ")

real=float(input("DIGITE QUANTOS REAIS VOCE TEM: "))
cot=float(input("QUANTO ESTA A COTACAO DO DOLAR: "))
dolar=real/cot
print(f"VOCE TERA: {dolar:0.2f}")
