# Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da média dos valores
# da lista.
# Exemplo:
# lista = [2.5, 7.5, 10.0, 4.0]
# (média = 6.0)
# Valor mais próximo da média = 7.5

cont = 0 
lista = [2.5, 7.5, 10.0, 4.0]
soma = 0
for item in lista:
    soma += item
    media = soma / len(lista)
    
print(soma, media)

    