N = int(input("Quantos numeros voce vai digitar? "))

vet: [float] = [0 for x in range(N)]

for i in range(0, N, 1):
    vet[i] = float(input("Digite um numero: "))

soma = 0
print("VALORES = ", end="")
for i in range(0, N, 1):
    print(f"{vet[i]:.1f} ", end="")
    soma = soma + vet[i]

media = soma / N
print(f"\nSOMA = {soma:.2f}")
print(f"MEDIA = {soma/N:.2f}")
