quant=float(input("DIGITE QUANTOS PROFUTOS FORAM VENDIDOS: "))
valor=float(input("DIGITE QUANTO CUSTA ESSE PRODUTO: "))
bruto=quant*valor
if bruto >= 1000.00:
    desc=bruto*10/100
else: desc=0

liquid=bruto-desc

print(f"A COMPRA SAIRA POR: {liquid:0.2f}")