#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. 

def soma_imposto(taxa_imposto, custo):
    result = (taxa_imposto / 100)*custo + custo
    print(f'o novo valor do produto é: {result}')

taxa_imposto = float(input('informe a taxa de imposto: '))
custo = float(input('informe o custo: '))
soma_imposto(taxa_imposto,custo)