# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

fibo = [1,1]
i = 0
num = int(input("Entre com um número: "))

while num > len(fibo):
	fibo.append(fibo[i] + fibo[i+1])
	i+=1

print ('Fibonacci(%d): %d' %(num,fibo[num-1]))