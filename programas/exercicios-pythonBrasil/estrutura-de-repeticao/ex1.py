# Faça um programa que peça uma n, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

# n = ""

# while n < 0 or n > 10:
# 	n = float(input('informe uma n entre zero e dez: '))
# 	print('valor invalido')
# print(f'a n é {n}')

while True:
	n = float(input("Digite uma nota entre 0 e 10: "))
	if n > 0 and n < 10:
		break
	else:
		print ("nota invalida")

print(f'a nota é {n}')