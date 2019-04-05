# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

cont=  1
lista_impar = []
lista_par = []
while cont <=10:
	n = int(input(f'informe o {cont}º numero: '))
	if n % 2 == 0:
		lista_par.append(n)
	else:
		lista_impar.append(n)

	cont+=1

print(f'lista impar {len(lista_impar)} elementos')
print(f'lista par {len(lista_par)} elementos')