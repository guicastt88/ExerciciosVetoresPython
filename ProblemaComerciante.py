N = int(input("Serao digitados dados de quantos produtos? "))

compra: [float] = [0 for x in range(N)]
venda: [float] = [0 for x in range(N)]

abaixo = 0
entre = 0
acima = 0
for i in range(0, N, 1):
    print(f"Produto {i+1}")
    nome = input("Nome: ")
    compra[i] = float(input("Preco de compra: "))
    venda[i] = float(input("Preco de venda: "))

    lucro = ((venda[i] - compra[i]) / compra[i]) * 100

    if lucro < 10:
        abaixo = abaixo + 1
    elif lucro <= 20:
        entre = entre + 1
    else:
        acima = acima + 1

totalCompra = 0
totalVenda = 0
lucroTotal = 0
for i in range(0, N, 1):
    totalCompra = totalCompra + compra[i]
    totalVenda = totalVenda + venda[i]
    lucroTotal = lucroTotal + (venda[i] - compra[i])

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {abaixo}")
print(f"Lucro entre 10% e 20%: {entre}")
print(f"Lucro acima de 20%: {acima}")
print(f"Valor total de compra: {totalCompra:.2f}")
print(f"Valor total de venda: {totalVenda:.2f}")
print(f"Lucro total: {lucroTotal:.2f}")

