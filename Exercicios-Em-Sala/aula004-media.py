p1=float(input("DIGITE A PRIMEIRA NOTA: "))
p2=float(input("DIGITE A SEGUNDA NOTA: "))

pp1=float(input("DIGITE O PESO DA PRIMEIRA PROVA: "))
pp2=float(input("DIGITE O PESO DA SEGUNDA PROVA: "))

media=((p1*pp1 + p2*pp2) / (pp1+pp2))
if media <5:
    print("REPROVADO")
elif (media >= 5) and (media<8):
    print("APROVADO")
elif (media>=8) and (media<9):
    print("PARABENS SEU DESEMPENHO FOI MUIT BOM!")
else:
    print("PARABENS,VOCE FOI APROVADO COM LOUVOR")
print(f"SUA MEDIA É DE {media:0.2f}")