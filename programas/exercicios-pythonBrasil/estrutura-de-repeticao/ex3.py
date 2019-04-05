# Faça um programa que leia e valide as seguintes informações:

#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd'; 

nome = ''
idade = 0
salario = 0
sexo = ''
relacionamento = ''

while True:
	nome = input('informe seu nome: ')
	idade = int(input('informe sua idade: '))
	salario = float(input('informe seu salario: '))
	sexo = input('informe qual seu sexo--> M-Masculino ou F-Feminino: ')
	relacionamento = input('informe seu estado civil--> S-Solteiro(a), C-Casado(a), V-Viuva(a), D-Divorciado(a): ')

	if len(nome)<=3:
		print('informe um nome com mais de 3 caracteres')
		break
	elif idade < 0 or idade > 150:
		print('a idade tem que ser maior que 0 e menor que 150')

	elif salario <= 0:
		print('o salario tem que ser maior que 0')

	elif sexo.lower() != 'm' and sexo.lower() != 'f':
		print('M-Masculino ou F-Feminino')

	elif relacionamento.lower() != 's' and relacionamento.lower() != 'c' and relacionamento.lower() !='v' and relacionamento.lower() !='d':
		print('estado civil--> S-Solteiro(a), C-Casado(a), V-Viuva(a), D-Divorciado(a)')
	else:	
		break

print(f'Nome: {nome.upper()}')
print(f'Idade: {idade}')
print(f'Salario: {salario}')
print(f'Sexo: {sexo.upper()}')
print(f'Estado-civil: {relacionamento.upper()}')
