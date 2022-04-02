N = int(input("Quantas pessoas voce vai digitar? "))

nome: [str] = [0 for x in range(N)]
idade: [int] = [0 for x in range(N)]

for i in range(0, N, 1):
	print(f"Dados da {i+1}a pessoa: ")
	nome[i] = input("Nome: ")
	idade[i] = int(input("Idade: "))

nom = 0
soma = idade[0]
for i in range(0, N, 1):
	if idade[i] > soma:
		soma = idade[i]
		nom = nome[i]
print(f"PESSOA MAIS VELHA: {nom}")