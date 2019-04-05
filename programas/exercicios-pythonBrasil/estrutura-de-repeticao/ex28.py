#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um. 

cds = int(input('iforme a quantidade de cds: '))
cont = 1
soma = 0
media = 0
while cont <= cds:
	preco = float(input(f'informe o preco do {cont}º cd: '))
	soma += preco
	media = soma / cds
	cont += 1
print(f'são {cds} cds, e o valor médio de cada cd é: R${media:.2f}')