def area():
    largura = float(input('informe a largura em (m): '))
    comprimento = float(input('informe o comprimento em (m): '))
    area = largura * comprimento
    print(f'a area do terreno {largura}x{comprimento} é de {area}')

area()