#Faça um programa que calcule e mostre a média aritmética de N notas. 
cont = 1
media = 0
soma = 0
notas = int(input('informe quantos notas serao: '))
while cont <= notas:
	n = float(input(f'informe a {cont}ª nota: '))
	cont+= 1
	soma += n
	media = soma / notas
print(media)