#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores. 

lista = []
conjunto = int(input('informe a quantidade de numeros que terá no conjunto: '))
cont = 1
n=0
while cont <= conjunto:
	n = int(input(f'insira o {cont}º numero: '))
	lista.append(n)
	cont += 1	
print(f'os numeros foram: {lista}')
print(f'o maior valor da lista é: {max(lista)}')
print(f'a soma dos valores é: {sum(lista)}')