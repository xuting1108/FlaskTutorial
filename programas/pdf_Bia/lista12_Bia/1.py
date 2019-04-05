# Crie uma função que recebe uma lista de números e
# a. retorne o maior elemento
# b. retorne a soma dos elementos
# c. retorne o número de ocorrências do primeiro elemento da lista
# d. retorne a média dos elementos
# e. retorne o valor mais próximo da média dos elementos
# f. retorne a soma dos elementos com valor negativo
# g. retorne a quantidade de vizinhos iguais

cont = 1
soma = 0
lista = []
media = 0

n = int(input('informe quantos elementos terao na lista: '))

while cont <= n:
	num = int(input(f'informe o {cont}º numero:'))
	cont += 1
	lista.append(num)
	soma += num
	media = soma / n

print(f'{soma}, {media:.2f}')