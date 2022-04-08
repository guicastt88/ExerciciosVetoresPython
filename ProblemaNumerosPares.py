N = int(input("Quantos numeros voce vai digitar? "))

num: [int] = [0 for x in range(N)]

for i in range(0, N, 1):
    num[i] = int(input("Digite um numero: "))

print("\nNUMEROS PARES:")

soma = 0
for i in range(0, N, 1):
    if num[i] % 2 == 0:
        print(f"{num[i]} ", end="")
        soma = soma + 1

print(f"\n\nQUANTIDADE DE PARES = {soma}")