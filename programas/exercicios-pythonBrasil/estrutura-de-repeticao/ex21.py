#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. 

n = int(input('informe um numero: '))
if n % n == 0 and n % 1 == n:
	print('é primo')
else:
	print('n é primo')