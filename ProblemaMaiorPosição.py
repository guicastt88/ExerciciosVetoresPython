N = int(input("Quantos numeros voce vai digitar? "))

num: [float] = [0 for x in range(N)]

for i in range(0, N, 1):
	num[i] = float(input("Digite um numero: "))

maior = num[0]
posMaior = 0
for i in range(0, N, 1):
	if num[i] >= maior:
		maior = num[i]
		posMaior = i + 1

print(f"\nMAIOR VALOR = {maior:.1f}")
print(f"POSICAO DO MAIOR VALOR = {posMaior}")