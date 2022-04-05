N = int(input("Quantas pessoas serao digitadas? "))

nome: [str] = [0 for x in range(N)]
idade: [int] = [0 for x in range(N)]
altura: [float] = [0 for x in range(N)]

for i in range(N):
	print(f"Dados da {i+1}a pessoa:")
	nome[i] = str(input("Nome: "))
	idade[i] = int(input("Idade: "))
	altura[i] = float(input("Altura: "))

print()
soma = 0
cont = 0
for i in range(0, N, 1):
	soma = soma + altura[i]
	if idade[i] < 16:
		cont = cont + 1

print(f"Altura media = {soma/N:.2f}")
print(f"Pessoas com menos de 16 anos: {cont/N*100:.1f}%")

for i in range(0, N, 1):
	if idade[i] < 16:
		print(nome[i])