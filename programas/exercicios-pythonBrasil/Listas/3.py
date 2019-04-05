#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 

notas = [5, 6, 4, 9]
total = 0
for i in notas:
    total += i
    media = total / len(notas)
if media >= 7:
    print(f'aprovado {media}')
if media >= 5 and media <7:
    print(f'recupracao {media}')
else:
    print(f'bomba {media}')