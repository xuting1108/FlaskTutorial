#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. 
import sys
lista = []
conjunto = int(input('informe a quantidade de numeros que terá no conjunto: '))
cont = 1
n=1
while cont <= conjunto:
	if n > 0 or n < 100:
		n = int(input(f'insira o {cont}º numero: '))
		lista.append(n)
		cont += 1
		
	else:
		print('os numeros tem que ser entre 0 e 1000')
		sys.exit()
			
print(f'os numeros foram: {lista}')
print(f'o maior valor da lista é: {max(lista)}')
print(f'a soma dos valores é: {sum(lista)}')