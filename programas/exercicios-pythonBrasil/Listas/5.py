#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 
from random import randint
cont = 0
x = 0
lista = []
par = []
impar = []
while cont <= 20:
    x = randint(0,100)
    lista.append(x)
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

    cont+=1
print(f'lista completa {lista}')
print(f'lista par {par}')
print(f'lista impar {impar}')

