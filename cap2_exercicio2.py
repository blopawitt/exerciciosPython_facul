assinatura = input("Qual é a assinatura do cliente?")
faturamento_anual = float(input("Digite o faturamento anual do cliente:"))
if assinatura.upper() == "BASIC":
    print(f"O valor a ser pago é R${faturamento_anual * 0.3}")
elif assinatura.upper() == "SILVER":
    print(f"O valor a ser pago é R${faturamento_anual * 0.2}")
elif assinatura.upper() == "GOLD":
    print(f"O valor a ser pago é R${faturamento_anual * 0.1}")
elif assinatura.upper() == "PLATINUM":
    print(f"O valor a ser pago é R${faturamento_anual * 0.05}")

