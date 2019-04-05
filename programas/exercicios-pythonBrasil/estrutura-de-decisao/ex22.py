# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão). 

n = int(input('informe um numero inteiro: '))

if n % 2 == 0:
	print(f'o numero {n} é par')

else:
	print(f'o numero {n} é impar')