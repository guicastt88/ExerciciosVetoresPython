N = int(input("Quantos valores vai ter cada vetor? "))

vetA: [int] = [0 for x in range(N)]
vetB: [int] = [0 for x in range(N)]
vetC: [int] = [0 for x in range(N)]

print("Digite os valores do vetor A:")
for i in range(0, N, 1):
    vetA[i] = int(input())

print("Digite os valores do vetor B:")
for i in range(0, N, 1):
    vetB[i] = int(input())

for i in range(0, N, 1):
    vetC[i] = vetA[i] + vetB[i]

print("VETOR RESULTANTE:")
for i in range(0, N, 1):
    print(vetC[i])