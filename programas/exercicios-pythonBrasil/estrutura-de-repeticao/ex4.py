# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

cidade_a = 80000
cidade_b = 200000
cont = 0

while cidade_a <= cidade_b:
	cidade_a += cidade_a * 0.03
	cidade_b += cidade_b * 0.015
	cont += 1
print(f'{cont} anos para cidade b alcancar a cidade a')