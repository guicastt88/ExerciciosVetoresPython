
N = int(input("Quantos numeros voce vai digitar? "))

vet: [int] = [0 for x in range(N)]

for i in range(0, N, 1):
    vet[i] = int(input("Digite um numero: "))

print("NUMEROS NEGATIVOS: ")
for i in range(0, N, 1):
    if vet[i] < 0:
        print(vet[i])