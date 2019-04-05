# 2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.

import random

numeros_sorteados = []
numeros_pares = []
numeros_impares = []

for i in range(20):
	n = random.randint(1,100)
	numeros_sorteados.append(n)

	if n % 2 == 0:
		numeros_pares.append(n)
	else:
		numeros_impares.append(n)

print(f'os numeros sorteados foram: {numeros_sorteados},\nos pares são: {numeros_pares}\nos impares: {numeros_impares} ')