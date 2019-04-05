# Sabe-se o seguinte sobre os ingredientes que compõem os pratos de um restaurante:
# Nome
# Peso da porção (em gramas)
# Preço do Kg.

# a. Crie uma lista de ingredientes onde cada elemento armazena o nome do ingrediente, peso
# da porção (em g) e o preço do Kg
# b. crie uma lista de Pratos de um restaurante onde cada elemento armazena o nome do prato
# e uma lista de ingrediente com nome dos ingredientes que o prato utiliza e quantidade de
# porções necessárias para prepará-lo
# c. crie uma lista com a quantidade semanal vendida de cada prato

# d. Faça um programa que, utilizando as listas criadas nos itens a, b e c, mostre
 #i. o custo de cada prato e a quantidade que deverá ser comprada de cada ingrediente para sua produção semanal
# ii. a quantidade que deverá ser comprada de cada ingrediente para produzir todos os pratos por uma semana
# iii. o prato mais caro

#nome, peso da porcao em g, preco do kg
igredientes = [['Arroz', 100, 5.00],['Carne', 100, 16.00],['Batata Inglesa', 250, 3.50], ['Cenoura', 100, 3.00],['Queijo Minas', 150, 12.00]]
#print(igredientes)
total = []
for i in igredientes:
    n = i[0]
    x = i[2] / (i[1] / 10)
    total.append(n)
    total.append(x)
print(total)
#nome do prato, igredientes e porcoes necessarias
pratos = [['muito escodidinho', 'batata inglesa', 3, 'queijo minas', 1, 'cenoura',1],['pastelao de vento', 'batata inglesa', 4, 'carne', 1]]
#print(pratos)

#prato e a qtd semanl vendida
consumo = [['muito escondidinho', 12], ['pastelao de vento', 30]]
#print(consumo)