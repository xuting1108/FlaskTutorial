#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. 
def calcular_idade():
	cont = 1
	media = 0
	soma = 0
	qtd = int(input('informe quantas pessoas serao: '))
	while cont <= qtd:
		n = int(input(f'informe a idade da {cont}ª pessoa: '))
		cont+= 1
		soma += n
		media = soma / qtd
	if media > 0 and media < 25:
		print('turma jovem') 
	elif media >= 25 and media < 60:
		print('turma adulta')
	else:
		print('turma idosa')
calcular_idade()
