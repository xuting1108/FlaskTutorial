#aça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321 

n = input('insira um numero inteiro: ')
# n1 = input('insira um numero inteiro: ')

# listan = [n, n1]
# listan.reverse()
# print(type(listan))
invert = n[::-1]

print(f'o numero invertido é:{invert}')