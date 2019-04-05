# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.
import random 

primeiro_vetor_10 = []
segundo_vetor_10 = []
vetor_20 = []

for i in range(10):
	n = random.randint(1,100)
	primeiro_vetor_10.append(n)

for i in range(10):
	num = random.randint(1,100)
	segundo_vetor_10.append(num)

vetor_20 = primeiro_vetor_10 + segundo_vetor_10	
print(f'{primeiro_vetor_10}\n{segundo_vetor_10}\n{vetor_20}')

