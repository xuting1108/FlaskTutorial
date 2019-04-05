# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. 

ano = int(input('informe um ano: '))

if ano%4 == 0 and ano%100 !=0:
 	print('o ano é bissexto')
else: 
 	print('o ano n é bissexto')