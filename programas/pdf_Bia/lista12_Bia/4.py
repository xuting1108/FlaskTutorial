# Crie uma função que recebe uma lista de strings e
# a. retorne o elemento com mais caracteres
# b. retorne a média de vogais nos elementos (  no de vogais de cada elemento/no de
# elementos)
# c. retorne o número de ocorrências do primeiro elemento da lista
# d. retorne a palavra lexicograficamente maior
# e. conte o número de ocorrências de palavras compostas
# f. retorne a quantidade de vizinhos iguais
# DESAFIO: exiba todas as sublistas de 2 elementos possíveis

#def recebe_lista():
lista = []
cont = 1
maior = 0
elementos = int(input('insira quantos elementos terão na lista: '))
while cont <= elementos:
    x = input(f'insira o {cont}º elemento da lista: ')
    if len(x) > maior:
        maior = x
    lista.append(x)
    cont+=1

