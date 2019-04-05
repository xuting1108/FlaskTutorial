# 7. Faça um programa que percorre uma lista com o seguinte formato: [['Brasil', 'Italia', [10, 9]],
# ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez
# em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9.
# O programa deve imprimir na tela:
# a) o total de faltas do campeonato
# b) o time que fez mais faltas
# c) o time que fez menos faltas
lista = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]
faltas = 0
time = []

#print(len(lista[2][2]))
for i in lista:
    faltas += i[2][0] + i[2][1] 
    # x = i[2][0] + i[2][1]
    # time.append(x)

print(f'Numero total de faltas: {faltas}')

#x = [i.split('[]',1)[2] for i in lista]
# print(x)

#sempre o i[2][0] vai pertencer ao i[0] e o i[2][1] ao i[1]
for i in lista:
    time.append(i[0])
    time.append(i[2][0])
    time.append(i[1])
    time.append(i[2][1])
print(time)

