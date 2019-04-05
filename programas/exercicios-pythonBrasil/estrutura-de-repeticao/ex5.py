# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. 

def calcular_tempo():	
	cidade_a = input('informe o nome da primeira cidade: ') 
	populacao_a = int(input(f'informe a populacao de {cidade_a}: '))
	taxa_a = float(input(f'informe a taxa de crescimento de {cidade_a}: '))

	print('')
	print('')

	cidade_b = input('informe o nome da segunda cidade: ') 
	populacao_b = int(input(f'informe a populacao de {cidade_b}: '))
	taxa_b = float(input(f'informe a taxa de crescimento de {cidade_b}: '))

	cont = 0
	if populacao_a < populacao_b:
		while populacao_a < populacao_b:
			populacao_a += populacao_a * (taxa_a / 100)
			populacao_b += populacao_b * (taxa_b / 100)
			cont += 1
		print(f'{cont} anos para {cidade_a} alcancar {cidade_b}')

	elif populacao_b <= populacao_a:
		while populacao_b <= populacao_a:
			populacao_a += populacao_b * (taxa_b / 100)
			populacao_a += populacao_a * (taxa_a / 100)
			cont += 1
		print(f'{cont} anos para {cidade_b} alcancar {cidade_a}')

	else:
		print('as cidades tem o mesmo numeor de habitantes!')
calcular_tempo()

