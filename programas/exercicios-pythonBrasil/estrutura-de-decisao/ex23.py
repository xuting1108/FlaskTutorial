#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento. 

n = float(input('informe um numero: '))
# round(1.41421356237309, 2)

# O código acima vai lhe devolver 1.41. =)

if n == round(n):
    print('**** Inteiro ****')
else:
    print('**** Decimal ****')
    print('Arredondado pra baixo: ', round(n-0.5) )
    print('Arredondado pra cima : ', round(n+0.5) )