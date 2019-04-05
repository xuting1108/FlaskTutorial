#Altere o programa anterior para mostrar no final a soma dos números. 

soma = 0
n1 = int(input('informe o primeiro numero: '))
n2 = int(input('informe o segundo numero: '))

if n1 < n2:
	for n in range(n1,n2):
		soma += n
		print(n)
	print(soma)
elif n2 < n1:
	for n in range(n2,n1):
		soma += n
		print(n)
	print(soma)
else:
	print('os numeros sao iguais')