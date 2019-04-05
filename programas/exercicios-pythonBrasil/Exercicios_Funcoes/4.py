#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo. 

def positivo_negativo(n):
    if n > 0:
        print(f'O numero {n} é positivo')
    else:
        print(f'O numero {n} é negativo')
n = int(input('informe um numero, podendo ser positivo ou negativo: '))
positivo_negativo(n)