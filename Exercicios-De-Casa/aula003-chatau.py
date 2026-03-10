print("VAMOS CALCULAR SEUS GASTOS DE COMIDA NO CHÂteau COusin Botyn?")
quant=float(input("DIGITE QUANTAS PORÇOES VOCE COMEU: "))
valor=float(input("DIGITE QUAL O VALOR DE CADA PORÇÃO: "))
bruto=quant*valor
desc=bruto*(quant*2/100)
couver=(bruto-desc)+20
garc=couver*110/100
print(f"VALOR TOTAL:RP$ {garc:0.2f}")