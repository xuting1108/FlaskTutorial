# #Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 

# lista = [10.6,36.9,2.8,3.5,2.4,7.8,24.35,84.3,15.96,28.05]

# invert = str(lista)[::-1]

# print(invert)

listaNumerosReais = []
print ('Informe os 10 numeros reais')
for i in range(10):
	listaNumerosReais.append(float(input('Numero '+ str(i+1) + ':\n')))
listaNumerosReais.reverse()
print (listaNumerosReais) 