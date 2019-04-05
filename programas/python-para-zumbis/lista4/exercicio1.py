 # Lista de Exercícios IV 1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
import random
from random import shuffle
#print(random.randint(1,100))
# for i in range(10):
# 	n = random.randint(1,100)
# print(n)0

numeros_sorteados = []
maior = 0 
menor = 100

for i in range(10):
	n = random.randint(1,100)
	numeros_sorteados.append(n)

	if n < menor: 
		menor = n
	if n > maior:
	    maior = n
	    
print(f'os numeros foram {numeros_sorteados} o menor numero é {menor} e o maior numero é {maior}')