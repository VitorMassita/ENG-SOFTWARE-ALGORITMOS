
try:
    nota1=float(input("DIGITE A NOTA 1: "))
    print("OPS, ALGO DEU ERRADO")
    try:
        nota2=float(input("DIGITE A NOTA 2: "))
    except ValueError:
        print("OPS, ALGO DEU ERRADO")
    media=(nota1+nota2)/2
    print("SUA MEDIA : ", media)
except ValueError:
    print("OPS, FUDEU")
        
           