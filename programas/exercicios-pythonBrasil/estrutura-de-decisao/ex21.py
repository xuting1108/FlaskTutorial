# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#     Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#     Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print('***** Caixa eletronico *****')

print('as notas disponiveis para saque sao as de 1, 5, 10, 50, 100')
saque = int(input('informe o valor do saque: '))

# valor_min = 10
# valor_max = 600

# centena = int(saque/100)
# dezena = int((saque-(centena*100))/10)
# unidade = int(saque - (centena*100 + dezena*10))

# print(f'O número {n} possui {centena} centenas, {dezena} dezenas e {unidade} unidades ' )

cem = int(saque / 100)
saque = saque - (cem*100)

cinquenta = int(saque/50)
saque = saque - (cinquenta*50)

dez = int(saque/10)
saque = saque - (dez*10)

cinco = int(saque/5)
saque = saque - (cinco*5)

um = saque

print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  1,00 = ',um)