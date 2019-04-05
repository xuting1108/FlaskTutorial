# Foram anotadas as idades e alturas dos alunos de uma turma e armazenados em uma lista cujos
# elementos são sublistas com dois elementos: o primeiro é a idade do aluno e o segundo a sua altura. Faça
# uma função que receba esta lista e utilizando as funções abaixo, determina e mostra quantos alunos com
# mais de 13 anos possuem altura inferior à média de altura desses alunos.
# a) Faça a função MediaTurma (lista) que recebe a lista com idade e altura de cada um dos aluno e retorna a
# média de altura da turma
# b) Faça a função Conta_Baixinhos (lista, media), que recebe a lista com idade e altura de cada um dos alunos e a
# média de altura da turma, retornando quantos alunos com mais de 13 anos estão abaixo da média de altura da
# turma

lista = [[26,1.8],[20,1.69]]
print(lista[1][1])
cont = 0
#vai ter que ser [cont][1]
for iten in lista:
    print(iten)