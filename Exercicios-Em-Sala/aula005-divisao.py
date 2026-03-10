try:
    x = float(input("Digite o valor de x: "))
    y = (4 * x**2 - 3 * x + 9) / x
    print(f"O valor de y é: {y}")
except ValueError: 
    print("OPS! PORFAVOR DIGITE SOMENTE VALORES NUMERICOS")
except ZeroDivisionError:
    print("NUNCA DIVIDIR POR ZERO")