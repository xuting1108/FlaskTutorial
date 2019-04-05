#Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos da primeira metade.
l = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']

n = 2
splited = []
len_l = len(l)
for i in range(n):
    start = int(i*len_l/n)
    end = int((i+1)*len_l/n)
    splited.append(l[start:end])
    
print(splited)



