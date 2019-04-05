#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 
def operacoes_listas(a,b,c,d,e):
    soma = 0
    multi = 1
    for i in numeros:
        soma += i
        multi *= i
    print(f'Os numeros foram {numeros} a soma é {soma} a multiplicacao é {multi}')

a = int(input('informe um numero: '))
b = int(input('informe um numero: '))
c = int(input('informe um numero: '))
d = int(input('informe um numero: '))
e = int(input('informe um numero: '))
numeros = [a,b,c,d,e]
operacoes_listas(a,b,c,d,e,)