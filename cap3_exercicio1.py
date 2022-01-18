total_alimentos = int(input("Quantos alimentos você ingeriu hoje?"))
alimento = 0
calorias_total = 0
for x in range(total_alimentos):
    alimento = float(input("Digite o valor calórico de cada alimento: "))
    calorias_total = calorias_total + alimento
print(f"O gasto calórico total foi de {calorias_total}cal.")

