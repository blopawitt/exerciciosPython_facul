peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = float(peso /(altura ** altura))
print(f"Seu IMC é {imc:.2f}")
if imc < 16:
    print("Baixo peso Grau III")
elif imc >= 16 and imc <= 16.99:
    print("Baixo peso Grau II")
elif imc >= 17 and imc <= 18.49:
    print("Baixo peso Grau I")
elif imc >= 18.5 and imc <= 24.99:
    print("Peso ideal")
elif imc >= 25 and imc <= 29.99:
    print("Sobrepeso")
elif imc >= 30 and imc <= 34.99:
    print("Obesidade Grau I")
elif imc >= 35 and imc <= 39.99:
    print("Obesidade Grau II")
elif imc >= 40:
    print("Obesidade Grau III")