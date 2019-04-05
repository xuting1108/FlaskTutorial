# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

#     A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#     A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#     A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = float(input('informe a primeira nota: '))
n2 = float(input('informe a segunda nota: '))
n3 = float(input('informe a terca nota: '))

media = (n1 + n2 + n3) / 3

if media >= 7:
	input(f'APROVADO média: {media}')
elif media == 10:
	input(f'APROVADO com DISTINÇÃO média: {media}')
else:
	input(f'REPROVADO média: {media}')