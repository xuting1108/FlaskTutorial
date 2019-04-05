# Faça uma função que:
# a. receba duas listas e exiba a união destas listas
# b. receba duas listas e exiba a interseção destas listas
# c. receba duas listas e exiba a intercalação destas listas, isto é, 1o da 1a lista, 1o da 2a lista, 2o
# da 1a lista, 2o da 2a lista...

signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
result = signos + numeros
print(result)

intercaladas = result[::2], result[1::2]
print(intercaladas)

nomes = ['filipe', 'roberta', 'igor', 'fernanda', 'katia']
chefes = ['filipe', 'fernanda']

lista_final = [i for i in nomes if i in chefes]
print(lista_final)

