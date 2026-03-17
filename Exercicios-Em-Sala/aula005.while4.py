import random
random.seed()
numcompu=int(random.uniform(0,99))
numjogador=-1000
count=0
while numcompu!=numjogador:
    numjogador=int(input("DIGITE SEU NUMEROOO!!: "))
    count=count+1
    if numcompu<numjogador:
        print("VOCE ERROUUU, O NUMERO E MENOR\nTENTE NOVAMENTE")
        print("*" *50)
    elif numcompu>numjogador:
        print("VOCE ERROUU, O NUMERO E MAIOR \nTENTE NOVAMENTE")
        print("*" *50)
    else:
        print(f"VOCE ACERTOUUU!!!!!!\nEM {count:0.0f} TENTATIVAS")
