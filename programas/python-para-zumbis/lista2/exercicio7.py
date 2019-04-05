# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de
# 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Obs. : somente são vendidos um número inteiro de latas. 
import math    

area_pintada = float(input('informe em metros quadrados a área a ser pintada: '))
#1l de tinta faz 3m2 1 lata tem 18l e custa 80
#1lata de tinta = 54m2
litros = area_pintada / 3

latas_tinta = litros / 18
lata_total = math.ceil(latas_tinta)
tot = int(lata_total * 80)


print(f'serão usadas {lata_total} lastas de tinta e o preco total será de {tot}R$')