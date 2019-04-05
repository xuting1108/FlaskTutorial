# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal. 

n1 = float(input('informe o primeiro numero: '))
n2 = float(input('informe o segundo numero: '))

escolha = int(input('Escolha qual operação deseja realizar\n1- Par ou ímpar\n2- Positivo ou negativo\n3- Inteiro ou Decimal: '))

def par_impar():
	if n1 % 2==0 and n2 % 2==0:
	    print(f'os numeros {n1} e {n2} são pares')

	elif n1 % 2==0 and n2 % 2!=0:
		print(f'o numero {n1} é par e o {n2} é ímpar')

	elif n1 % 2!=0 and n2 % 2==0:
		print(f'o numero {n1} é impar e o {n2} é par')
	else:
		print(f'os numeros {n1} e {n2} sao impares')

def positivo_negativo():
	if n1 < 0 and n2 < 0:
		print(f'oS numeros {n1} e {n2} são negativos')

	elif n1 < 0 and n2 >0:
		print(f'o numero {n1} é negativo e o numero {n2} é positivo')

	elif n1 > 0 and n2 < 0:
		print(f'o numero {n1} é positivo e o numeor {n2} é negativo')

	else:
		print(f'oS numeros {n1} e {n2} são positivos')

def decimal():
	if n1 == round(n1) and n2 == round(n2):
    	print('**** Os numeros sao inteiros ****')

    elif n1 == round(n1) and n2 != round(n2):
    	print(f'o numer {n1} é inteiro e o {n2} é decimal')

    elif n1 != round(n1) and n2 == round(n2):
    	print(f'o {n1} é decimal e o {n2} é inteiro')

	else:
	    print('**** Decimais ****')
	    print('Arredondado pra baixo: ', round(n1-0.5), round(n2-0.5) )
	    print('Arredondado pra cima : ', round(n1+0.5) ), round(n2-0.5)

if escolha == 1:
	par_impar()

elif escolha == 2:
	positivo_negativo()

elif escolha == 3:
	decimal()



