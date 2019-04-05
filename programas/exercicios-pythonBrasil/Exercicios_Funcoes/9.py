#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721. 

def reverso(n):
    invert = str(n)[::-1]
    print(f'a forma inverso do numero {n} é: {invert}')

n = int(input('informe um numero: '))
reverso(n)