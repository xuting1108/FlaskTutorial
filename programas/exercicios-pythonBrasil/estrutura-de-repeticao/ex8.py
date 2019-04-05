#Faça um programa que leia 5 números e informe a soma e a média dos números. 

cont = 0
soma = 0
lista = []
while cont <=4:
	cont+=1
	n = float(input(f'informe o {cont}º numero: '))
	lista.append(n)
	soma += n
	media = soma / 5
print(f'os numeros foram: {lista}')
print(f'a soma dos numeros foi: {soma}')
print(f'a media é: {media}')