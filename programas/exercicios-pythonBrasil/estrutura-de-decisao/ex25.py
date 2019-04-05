# #Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 

print('Responda as perguntas com (1-Sim ou 0-Não)')

p1 = int(input('Telefonou para a vítima?: '))
p2 = int(input('Esteve no local do crime?: '))
p3 = int(input('Mora perto da vítima?: '))
p4 = int(input('Devia para a vítima?: '))
p5 = int(input('Já trabalhou com a vítima?: '))

resposta = p1 + p2 + p3 + p4 + p5

if resposta == 2:
	print('Suspeita')
elif resposta == 3 or resposta == 4:
	print('Cúmplice')	
elif resposta == 5:
	print('Assassino')
else:
	print('Inocente')