p = float(input('peso:'))
a = float(input('altura'))

def calcularIMC(p,a):
	imc = p/(a**2)
	if imc<20:
		print('baixo')
	elif imc <= 25:
		print('normal')
	elif imc < 30:
		print('obeso')
	else:
		print('gordo pra cacete')
calcularIMC(p,a)	 


