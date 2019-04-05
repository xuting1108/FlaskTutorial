# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                           Até 5 Kg           Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#     Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 


kg_morango = float(input('informe quantos quilos de morango irá comprar: '))
kg_maca = float(input('informe quantos quilos de maca irá comprar: '))

preco_morango = 2.5
preco_maca = 1.8

total_quilos = kg_morango + kg_maca


preco = total_quilos

if total_quilos > 8 or  total_quilos > 25:
	total_quilos += total_quilos * 0.1
