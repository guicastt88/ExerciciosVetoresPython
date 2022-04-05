N = int(input("Quantas pessoas serao digitadas? "))

altura: [float] = [0 for x in range(N)]
genero: [str] = [0 for x in range(N)]

for i in range(0, N, 1):
	altura[i] = float(input(f"Altura da {i+1}a pessoa: "))
	genero[i] = input(f"Genero da {i+1}a pessoa: ")

menorAltura = altura[0]
maiorAltura = altura[0]
for i in range(0, N, 1):
	if altura[i] < menorAltura:
		menorAltura = altura[i]
	if altura[i] > maiorAltura:
		maiorAltura = altura[i]
print(f"Menor altura = {menorAltura:.2f}")
print(f"Maior altura = {maiorAltura:.2f}")

homens = 0
alturaM = 0
div = 0
for i in range(0, N, 1):
	if genero[i] == 'F':
		alturaM = alturaM + altura[i]
		div = div + 1
	else:
		homens = homens + 1

print(f"Media das alturas das mulheres = {alturaM/div:.2f}")
print(f"Numero de homens = {homens}")