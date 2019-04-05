# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento. 

salario = float(input('informe seu salario: '))

def calcular_salario():
	if salario <= 280:
		percent = 0.2
		aumento = (salario * percent)
		novo_salario = salario + aumento
		print(f'o salário antes do reajuste: {salario}\no percentual de aumento aplicado: {percent}\no valor do aumento: {aumento}\n novo salario: {novo_salario}')

	elif salario > 280 or salario <= 700:
		percent = 0.15
		aumento = (salario * percent)
		novo_salario = salario + aumento
		print(f'o salário antes do reajuste: {salario}\no percentual de aumento aplicado: {percent}\no valor do aumento: {aumento}\n novo salario: {novo_salario}')


	elif salario > 700 or salario <= 1500:
		percent = 0.1
		aumento = (salario * percent)
		novo_salario = salario + aumento
		print(f'o salário antes do reajuste: {salario}\no percentual de aumento aplicado: {percent}\no valor do aumento: {aumento}\n novo salario: {novo_salario}')

	else:
		percent = 0.05
		aumento = (salario * percent)
		novo_salario = salario + aumento
		print(f'o salário antes do reajuste: {salario}\no percentual de aumento aplicado: {percent}\no valor do aumento: {aumento}\n novo salario: {novo_salario}')
calcular_salario()