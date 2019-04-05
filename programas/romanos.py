# -*- coding: utf-8 -*-

# n = int(input('Digite um numero a ser convertido: '))
# def converte_numero(n):
# 	if n == 1:
# 		print('I')
# 	elif n == 4:
# 		print('IV')
# 	elif n == 5:
# 		print('V')
# 	elif n == 9:
# 		print('IX')
# 	elif n == 10:
# 		print('X')
# 	elif n == 40:
# 		print('XL')
# 	elif n == 50:
# 		print('X')
# 	else:
# 		print('digite um numero com dois digitos')
# converte_numero(n)


"""
*************************************exemplo em js do git do problema**************************************************************
module.exports = (number) => {

    if (typeof number !== 'number' || number < 0 || !Number.isInteger(number)) {
        throw new Error();
    }

    const numberToRomanTable = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }, keys = Object.keys(numberToRomanTable).reverse();

    let result = "";

    keys.forEach(key => {
        while (number >= key) {
            number -= key
            result += numberToRomanTable[key]
        }
    });

    return result;
}
************************************************************************************************************************************************
"""
# Não há necessidade de converter números maiores que 3000. (Os próprios romanos não tendem a subir mais)
num = int(input('Digite um numero a ser convertido em número Romano: '))
def converter_romano(num):
	#lista de numeros inteiros
    valor_inteiro = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    #lista de simbolos romanos
    simbolo = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    #o numero romano comeca vazio,  depois vai receber um valor dentro do while
    numero_romano = ''
    #funciona como um "contador"
    i = 0
    #n existe representacao para o numero 0 
    while  num > 0:
    	#Valor de i aumenta com cada passagem
    	#fazer a divisao para obter um resultado inteiro
        for n in range(num // valor_inteiro[i]):
        	#vai concatenar
            numero_romano += simbolo[i]
            num -= valor_inteiro[i]
        i += 1
    print(numero_romano)

converter_romano(num)


