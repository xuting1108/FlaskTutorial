#Faça um programa para imprimir:

#         1
#         2   2
#         3   3   3
#         .....
#         n   n   n   n   n   n  ... n
def imprimir_piramide(n):
    for i in range(n):
        i += 1
        print(f'{str(i)}  '* i)
n = int(input('informe um numeor: '))
imprimir_piramide(n)
