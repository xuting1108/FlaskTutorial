#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 

n = int(input('informe um numero: '))
cont = n
while cont != 1:
	cont -= 1
	n = n*cont
	
print(n)