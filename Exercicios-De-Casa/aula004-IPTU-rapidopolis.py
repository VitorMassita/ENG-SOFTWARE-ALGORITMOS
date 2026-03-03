anoc=int(input("DIGITE O ANO EM QUE O IMOVEL FOI CONSTRUIDO: "))
anoat=int(input("DIGITE O ANO ATUAL: "))
idade=anoat-anoc
if idade < 5:
    desconto= 0
elif (idade >= 5) and (idade <20):
    desconto = 15/100
elif (idade >=20) and (idade<40):
    desconto = 25/100
else:
    desconto=30/100
valor=float(input("DIGITE O VALOR DO IMOVEL: "))
iptu= valor - (valor*desconto)
print(f"VOCE PAGARA {iptu:0.2f} RP$")