#Solicite o preço de uma mercadoria e o percentual de desconto. 
#Exiba o valor do desconto e o preço a pagar.

mercadoria = float(input('preco da mercadoria: '))
desconto = float(input('informe o percentual do desconto: '))

porcentagem = desconto/100
novo_preco = mercadoria - (porcentagem * mercadoria) 
print(f'o desconto foi de {desconto} e o preco a pagar é: {novo_preco}')