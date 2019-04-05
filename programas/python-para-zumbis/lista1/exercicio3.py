# -*- coding: utf-8 -*-
d = int(input('insira quantos dias são: '))
h = int(input('insira quantas horas são: '))
m = int(input('insira quantos minutos são: '))
s = int(input('insira quantos segundos são: '))

# dia = 24 * h
# hora = 60 * m
# minuto = 60 * s
# if h > 23:
# 	d+=1
# elif m > 59:
# 	h+=1
# elif s > 59:
# 	m+=1
# else:
# 	print("")
total_segundos = (d*24*60*60) + (h*60*60) + (m*60) + s
print(f'São: {d} dias e {h}:{m}:{s} horas e o total de segundos são:{total_segundos}')

