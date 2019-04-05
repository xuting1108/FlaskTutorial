#Faça um Programa que leia três números e mostre-os em ordem decrescente. 
n1 = float(input('informe o primeiro numero: '))
n2 = float(input('informe o segundo numero: '))
n3 = float(input('informe o terceiro numero: '))

lista = [n1, n2, n3]
lista.sort(reverse=True)
print(f'a ordem decrescente é {lista}')