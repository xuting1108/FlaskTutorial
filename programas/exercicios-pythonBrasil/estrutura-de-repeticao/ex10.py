#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. 

n1 = int(input('informe o primeiro numero: '))
n2 = int(input('informe o segundo numero: '))

if n1 < n2:
	for n in range(n1,n2):
		print(n)
elif n2 < n1:
	for n in range(n2,n1):
		print(n)
else:
	print('os numeros sao iguais')