try:
    peso=float(input("DIGITE SEU PESO: "))
    print("**********************************")
    altura=float(input("DIGITE SUA ALTURA EM METROS: "))
    print("**********************************")
    imc=peso/altura**2
    if imc < 18.4:
        print(f"SEU IMC : {imc:0.2f} E ESTA ABAIXO DO PESO")
    elif (imc >= 18.5) and (imc<=24.9):
        print((f"SEU IMC : {imc:0.2f} E ESTA NORMAL"))
    elif (imc >=25) and (imc<= 29.9):
        print((f"SEU IMC : {imc:0.2f} E ESTA COM SOBREPESO"))
    else:
        print("VOCE ESTA COM OBESIDADE")
except ValueError:
    print("DIGITE VALORES NUMERICOS")
except ZeroDivisionError:
    print("NUNCA DIVIDIR POR 0")
