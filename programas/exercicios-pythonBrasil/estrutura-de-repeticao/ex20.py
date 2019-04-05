#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. 
import sys
n = int(input('informe um numero: '))
cont = n
if n < 16 and n > 0:
	while cont != 1:
		cont -= 1
		n = n*cont
else:
	print('o numero tem q ser >0 e <16')
	sys.exit()
	
print(n)
