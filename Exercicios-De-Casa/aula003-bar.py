print("VAMOS CALCULAR A CONVERSAR RAPID-DOLAR ")
rapid=float(input("DIGITE A COTACAO DO RAPID EM RELACAO AO DOLAR: "))
volum=float(input("DIGITE QUANTOS DOLARES VOCE QUER COMPRAR: "))
total=volum/rapid
print("***********************************************")
print(f"VOCE PRECISARA DE {total:0.2f}, E MAIS RP$10,00 PARA REGISTROS")
bruto=total+10
print("***********************************************")
print("FORA ISSO E NECESSARIO MAIS 0,6% para taxas admnistrativas")
brutotot=bruto*1.06
print("***********************************************")
print(f"TOTAL A PAGAR: {brutotot:0.2f}")
