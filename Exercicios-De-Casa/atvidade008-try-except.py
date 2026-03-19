nfunc=0
quant=0
nfuncmin=0
nfuncacima=0
total_folha=0
pec_extra=0
nivel=0
bonus=0
quant=int(input("DIGITE O NUMERO DE FUNCIONARIOS: "))
while quant != 0:
    nivel=str(input("DIGITE O NIVEL DO FUNCIONARIO: \nPARA PARAR A REPETICAO DIGITE 0"))
    if nivel==0:
        break
    elif nivel == "N1":
        salario_base = 1000
        minimo = 20
        bonus = 100
        pec_extra=int(input("DIGITE QUANTAS PECAS EXTRAS ELE FABRICOU: "))
        total_folha=salario_base+pec_extra*bonus
        nfunc +=1
        nfuncmin +=1
        quant -=1
    elif nivel=="N2":
        salario_base = 3000
        minimo = 40
        bonus = 400
        pec_extra=int(input("DIGITE QUANTAS PECAS EXTRAS ELE FABRICOU: "))
        total_folha=salario_base+pec_extra*bonus
        nfunc +=1
        nfuncacima +=1
        quant -=1
    elif nivel == "N3":
        salario_base = 7000
        minimo = 60
        bonus = 900
        pec_extra=int(input("DIGITE QUANTAS PECAS EXTRAS ELE FABRICOU: "))
        total_folha=salario_base+pec_extra*bonus
        nfunc +=1
        nfuncacima +=1
        quant -=1
    else:
        print("CASO QUEIRA PARAR DIGITE 0, OU COLOQUE OS NIVEIS NOVAMENTE")
        porcentmais=(nfunc/nfuncacima) *100
        porcentmenos=(nfunc/nfuncmin)*100
print(f"O TOTAL DA FOLHA DE PAGAMENTO E DE:R${total_folha:0.0f}")
print(f"{nfuncmin:0.0f} FUNCIONARIO(S) TIVERAM A PRODUCAO IGUAL OU MENOR A MINIMA, REPRESENTANDO {porcentmenos:0.2f}%")
print(f"{nfuncacima:0.0f} FUNCIONARIO(S) TIVERAM A PRODUCAO IGUAL OU MENOR A MINIMA,REPRESENTANDO {porcentmais:0.2f}%")