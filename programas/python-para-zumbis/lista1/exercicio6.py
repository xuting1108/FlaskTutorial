#Calcule o tempo de uma viagem de carro. 
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem

d = float(input('Qual a distancia a ser percorrida em Km: '))
v = float(input('Qual a velociadade média esperada em Km/h: '))

tempo_medio = d/v

print(f'O tempo médio da viagem é de {tempo_medio}h')