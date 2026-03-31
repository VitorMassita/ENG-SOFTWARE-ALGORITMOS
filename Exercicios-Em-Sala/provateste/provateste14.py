pos=0
ncodigo=7
numero=0
codigo=input("DIGITE SEU CODIGO: ")
try:
    while len(codigo) == ncodigo:
        numero=numero+int(codigo[pos])
        verificador=codigo[6]
        pos+=1
        if numero%10 == verificador:
            print("CODIGO VALIDO")
            break
        else:
            print("CODIGO INVALIDO")
            break
except:
    print("OCORREU ALGUM ERRO")