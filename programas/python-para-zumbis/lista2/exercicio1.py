# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado_a = float(input('informe a medida do lado a: '))
lado_b = float(input('informe a medida do lado b: '))
lado_c = float(input('informe a medida do lado c: '))

if lado_a == lado_b == lado_c:
	print('o triangulo é equilátero')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
	print('o triangulo é isósceles')
else:
	print('o triangulo é escaleno')