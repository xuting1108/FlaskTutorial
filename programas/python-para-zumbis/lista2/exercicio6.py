# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
# quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido.
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$ b. - IR (11%) : R$ c. - INSS (8%) : R$ d. - Sindicato ( 5%) :R$ e. = Salário Liquido : R

mes = input('qual o mes trabalhado: ')
ganha_por_hora = float(input('quanto vc ganha por hora: '))
horas_trabalhadas = int(input('quantas horas vc tabalhou no mes: '))
salario_bruto = ganha_por_hora * horas_trabalhadas
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto 
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print('*********************Salário*********************')
print(f'O salário bruto em {mes} é de {salario_bruto}R$;\nImposto de Renda {ir}R$;\nINSS {inss}R$;\nO sindicato {sindicato}R$;\n Salário Líquido {salario_liquido}R$' )
print('*************************************************')