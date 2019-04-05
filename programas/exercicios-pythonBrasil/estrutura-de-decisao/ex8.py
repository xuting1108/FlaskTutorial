# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 
p1 = float(input('informe o preço do primeiro produto: '))
p2 = float(input('informe o preço do segundo produto: '))
p3 = float(input('informe o preço do terceiro produto: '))

lista = [p1,p2,p3]

print(f'Voce deve comprar o produto que custa {min(lista)} ')