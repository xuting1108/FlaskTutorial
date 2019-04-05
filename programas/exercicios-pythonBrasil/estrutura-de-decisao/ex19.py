# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

#     Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#     326 = 3 centenas, 2 dezenas e 6 unidades
#     12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 

n = int(input('informe um numero menor que 1000: '))

centena = int(n/100)
dezena = int((n-(centena*100))/10)
unidade = int(n - (centena*100 + dezena*10))


if n < 0:
	print('Informe um nŕmeo maior que 0')
elif n > 1000:
	print('O numero tem que ser menor que 1000')
else:
	print(f'O número {n} possui {centena} centenas, {dezena} dezenas e {unidade} unidades ' )