#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
letra = input('digite uma letra: ')
vogal = ['a','e','i','o','u']

if letra in vogal:
	print('a letra é vogal')
else:
	print('a letra é consoante')