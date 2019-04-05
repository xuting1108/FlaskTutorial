#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

cont = 1
turmas = int(input('informe a quantidade de turmas: ')) 
soma = 0
media = 0
while cont <= turmas: 
	alunos = int(input(f'informe a quantidades de alunos da {cont}ª turma: '))
	if alunos > 0 and alunos <= 40:
		cont += 1
		soma += alunos
		media = soma / turmas
	else:
		print('as turmas tem que ter mais de 0 e menos de 40 alunos!')	
print(media)