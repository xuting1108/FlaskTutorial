# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 


while True:
	nome = input('informe seu nome: ')
	senha = input('informe sua senha: ')
	if nome in senha:
		print('a senha n pode ser a mesma que o nome')
	else:
		break
print(f'o nome é {nome} e a senha é {senha}')



