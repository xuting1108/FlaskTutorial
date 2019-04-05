#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 

cont = 1
medias = []

while cont <= 10:
    print(f'*** notas do {cont}º aluno ***')
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    nota3 = float(input("Digite a sua terceira nota: "))
    nota4 = float(input("Digite a sua quarta nota: "))
    print('***************************************')

    media = (nota1+nota2+nota3+nota4)/4
    medias.append(media)
    
    cont+=1