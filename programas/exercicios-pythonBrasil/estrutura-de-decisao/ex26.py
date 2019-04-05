# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#     Álcool:
#     até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 


print('*****  Posto  *****')
tipo = input('Informe qual tipo de combustível deseja A-álcool (R$ 1,90), G-gasolina (R$ 2,50): ')
litros = float(input('informe quantos litros vc deseja: '))

valor_al = litros * 1.9
valor_gas = litros * 2.5


def escolher_tipo():
	if tipo.lower() == 'a': 
		print('Voce escolheu alcool')
		if litros <= 20:
			total = valor_al * 0.97 #já calcula o velor total
			print(f'vc vai gastar R${total:.2f} e colocou {litros} litros')
		else:
			total = valor_al * 0.95
			print(f'vc vai gastar R${total:.2f} e colocou {litros} litros')

	elif tipo.lower() == 'g': 
		print('Voce escolheu gasolina')
		if litros <= 20:
			total = valor_gas * 0.96
			print(f'vc vai gastar R${total:.2f} e colocou {litros} litros')
		else:
			total = valor_gas * 0.94
			print(f'vc vai gastar R${total:.2f} e colocou {litros} litros')
	else:
		print('nao existe esse tipo de combustivel')
escolher_tipo()
