#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 

def qtd_digitos(n):
    tot = len(n)
    print(f'a quantidade de digitos que o numero {n} posui é: {tot}')

n = input('informe um numero: ')
qtd_digitos(n)