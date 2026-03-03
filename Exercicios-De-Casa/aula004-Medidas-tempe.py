celsius=str
fahrenheit=str
kelvin=str
reaumur=str
rankine=str
medida=(input("DIGITE QUAL MEDIDA VOCE QUER CONVERTER: "))
if medida == celsius:
    c=float(input("DIGITE QUANTOS GRAUS CELSIUS VOCE TEM: "))
    temp=str(input("DIGITE PARA QUAL MEDIDA VOCE QUER: "))
    if temp == "fahrenheit":
        resultado=5*(f-32)/9
        print(f"VOCE TERA {resultado:0.2f} fahrenheit")
    elif temp == "kelvin":
        resultado=(k-273.15)
        print(f"VOCE TERA {resultado:0.2f} Kelvin")
    elif temp == "reaumur":
        resultado=(5*r)/4
        print(f"VOCE TERA {resultado:0.2f} reaumur")
    elif temp == "rankine":
        resultado=(5*(rank/9))-273.15
        print(f"VOCE TERA {resultado:0.2f} rankine")
elif medida == "rankine":
    c=float(input("DIGITE QUANTOS GRAUS RANKINE VOCE TEM: "))
    temp=(input("DIGITE PARA QUAL MEDIDA VOCE QUER: "))
    if temp =="reaumur":
        resultado=(9/4*c)+491.67
    print(f"VOCE TERA {resultado:0.2f}")
    elif temp == "fahrenheit":
    resultado=4*(f-32)/9
    print(f"VOCE TERA {resultado:0.2f}")

    