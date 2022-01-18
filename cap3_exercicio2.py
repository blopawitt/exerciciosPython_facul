transacoes_diarias = int(input("Quantas transações você fez hoje?"))
valor_transacao = 0
total_gasto = 0
for x in range(transacoes_diarias):
    valor_transacao = float(input("Digite o valor de cada transacao: "))
    total_gasto = total_gasto + valor_transacao
media = total_gasto / transacoes_diarias
print(f"O valor total gasto foi R${total_gasto} e a média foi R${round(media)}.")