SH=float(input("DIGITE QUAL O SALARIO HORA: "))
HT=float(input("DIGITE QUANTAS HORAS VOCE TRABALHOU: "))
SB=SH*HT
quant=float(input("DIGITE QUANTOS FILHOS VOCE TEM: "))
if quant >= 3:
    abono=quant*10/100
    abonoLiquid=SB*abono
else:
    abono=quant*5/100
    abonoLiquid=SB*abono
SL=SB+abonoLiquid
print(f"SEU SALARIO BRUTO E DE: {SL:0.2f}")
if SL >= 15000:
    IR=SL*27.5/100
else:
    IR=0
L=float(SL-IR)
print(f"SEU SALARIO LIQUIDO E DE {L:0.2f}")
