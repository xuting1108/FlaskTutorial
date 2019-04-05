#Faça um programa que leia 5 números e informe o maior número.

cont= 0
lista = []
while cont <=4:
	cont+=1
	n = float(input(f'informe o {cont}º numero: '))
	lista.append(n)

print(lista)
print(f'o maior numero é: {max(lista)}')