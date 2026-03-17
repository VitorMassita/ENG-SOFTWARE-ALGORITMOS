dia=int(input("DIGITE O TEMPO EM DIAS: "))
diamin=100000
while dia>0     :
    t=0.011*dia**3-0.3*dia**2+0.04*dia
    dia=dia-1
    if t<diamin:
        diamin=t
print(f"A TEMPERATURA MINIMA E {diamin:0.1f}")