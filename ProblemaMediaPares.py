N = int(input("Quantos elementos vai ter o vetor? "))

num: [int] = [0 for x in range(N)]

for i in range(0, N, 1):
	num[i] = int(input("Digite um numero: "))

div = 0
soma = 0
for i in range(0, N, 1):
	if num[i] % 2 == 0:
		soma = soma + num[i]
		div = div + 1

if div != 0:
	print(f"MEDIA DOS PARES = {soma/div:.1f}")
else:
	print("NENHUM NUMERO PAR")

