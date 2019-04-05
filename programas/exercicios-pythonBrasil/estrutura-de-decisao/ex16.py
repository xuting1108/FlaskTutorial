# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#     Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#     Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 
import math
import sys
print('A euqação do segundo grau é ax2 + bx + c')

a = float(input('informe o valor de a: '))
b = float(input('informe o valor de b: '))
c = float(input('informe o valor de c: '))

delta = b**2 - (4*a*c)
	
if a == 0:
	print('A equação nao é do segundo grau')
	break

elif delta < 0:
	print('a equacao nao possui raizes reais')
	break
	
elif delta == 0:
	raiz_delta = math.sqrt(delta)
	x1 = (-b - raiz_delta) / 2*a
	print(f'possui apenas uma raiz real: {x1}')

else:
	raiz_delta = math.sqrt(delta)
	x1 = (-b - raiz_delta) / 2*a
	x2 = (-b + raiz_delta) / 2*a
	print(f'as raizes sao: {x1} e {x2}')
