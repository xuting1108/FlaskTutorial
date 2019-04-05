#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n = float(input('insira um numero, pode ser positivo ou negativo: '))

if n < 0:
	print(f'o numero {n} é negativo')
else:
	print(f'o numero {n} é positivo')