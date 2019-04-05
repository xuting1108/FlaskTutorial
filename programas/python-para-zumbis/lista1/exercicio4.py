s = float(input('informe seu salário: '))
p = float(input('informe a porcentagem do aumento: '))

porcentagem = p/100

novo_salario = (porcentagem * s) + s
print(f'Seu novo salário é: {novo_salario}')