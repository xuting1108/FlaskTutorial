# O Zodíaco chinês é composto por animais com ciclo de 12 anos. Uma maneira simplificada de
# identificá-lo é verificando-se apenas o ano de seu nascimento do seguinte modo:
# ano do nascimento % 12
# 0 1 2 3 4 5 6 7 8 9 10 11
# Signo
# Macaco Galo Cão Porco Rato Boi Tigre Coelho Dragão Serpente Cavalo Carneiro
# a) Crie uma lista com os signos
# b) Crie uma lista com a data de aniversário dos membros de sua família
# c) Faça uma função que, usando as listas criadas nos itens a e b, mostre o signo de cada membro de
# sua família
def mostrar_signos(list):
    signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
    #faz o split dadata de aniversario
    data = [i.split('/') for i in aniversarios] 
    #print(data)

    ano = [item[2] for item in data]
    #vai pegar o indice 2 (que é o ano) de cada item
    # for item in data:
    #     ano.append(item[2])
    #print(ano)

    #transformo os itens en inteiros para poder fazer as comparacoes
    for item in range(0, len(ano)): 
        ano[item] = int(ano[item]) 
        if ano[item] % 12 == 0:
            print(signos[0])

        elif ano[item] % 12 == 1:
            print(signos[1])

        elif ano[item] % 12 == 2:
            print(signos[2])

        elif ano[item] % 12 == 3:
            print(signos[3])

        elif ano[item] % 12 == 4:
            print(signos[4])

        elif ano[item] % 12 == 5:
            print(signos[5])

        elif ano[item] % 12 == 6:
            print(signos[6])

        elif ano[item] % 12 == 7:
            print(signos[7])

        elif ano[item] % 12 == 8:
            print(signos[8])

        elif ano[item] % 12 == 9:
            print(signos[9])

        elif ano[item] % 12 == 10:
            print(signos[10])

        elif ano[item] % 12 == 11:
            print(signos[11])
aniversarios = ['27/03/2000','11/08/1992', '23/09/2003', '15/07/2013', '18/09/1997']
mostrar_signos(aniversarios)

#mostrar_signos('11/08/1992')        
# print(ano)
# cont = 0
# #transformo os itens en inteiros para poder fazer as comparacoes
# for item in range(0, len(ano)): 
#     ano[item] = int(ano[item])
# # print(len(ano))
#     if ano[item] % 12 == cont:
#         print(signos[cont])
#         cont+=1 
# print(len(ano))