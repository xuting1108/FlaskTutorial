#Determine se um ano é bissexto. Verifique no Google como fazer isso... 
# Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
# Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
# Pode ser que seja divisível por 400.
ano = int(input('informe um ano: '))

if ano%4 == 0 and ano%100 !=0:
 	print('o ano é bissexto')
else: 
 	print('o ano n é bissexto')
