peso=float(input("DIGITE SEU PESO: "))
altura=float(input("DIGITE SUA ALTURA EM METROS: "))
imc=peso/(altura**2)
if imc <18.5:
    print(f"SEU IMC E {imc:0.2f} - VOCE ESTA ABAIXO DO PESO")
elif imc >18.5 and imc <=24.99:
    print(f"SEU IMC E {imc:0.2f} - VOCE ESTA COM O PESO NORMAL")
elif imc>=25 and imc <29.99:
    print(f"SEU IMC E {imc:0.2f}- VOCE ESTA COM SOBREPESO")
else:
    print(f"SEU IMC E {imc:0.2}- VOCE ESTA COM OBESIDADE")