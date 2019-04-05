#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
#assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

km = float(input('km percorridos: '))
dias = int(input('dias de aluguel do carro: '))

preco = 60 * dias + 0.15 * km

input(f'o preco total a ser pago é: {preco}')