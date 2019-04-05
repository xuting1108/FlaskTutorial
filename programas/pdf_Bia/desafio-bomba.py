# Campo Minado é um jogo que se tornou muito popular por acompanhar o sistema
# operacional Microsoft Windows.
# Nesse jogo, o campo minado pode ser representado por uma matriz retangular.
# O jogador deve revelar todas as posições livres (sem bomba) da matriz, clicando
# em uma posição com conteúdo desconhecido. O jogo acaba quando o jogador
# clicar em uma posição com bomba, ou quando todas as posições livres forem
# abertas.
# Nesse exercício, você deve implementar algumas funções que podem ser
# utilizadas na implementação desse jogo.

# Escreva uma função que recebe como parâmetros uma matriz inteira A e
# uma posição (lin, col) da matriz, e conta quantas posições ao redor da
# posição (lin, col) contém o valor -1 (valor adotado para representar uma
# bomba)
# b) Escreva um programa que lê uma matriz A de 0’s (posições livres) e -1’s
# (bomba). Utilizando a função do item anterior, o programa deve computar
# e imprimir a quantidade de bombas ao redor de cada posição livre da matriz.

def conta_bomba(A, lin, col):
	posicoes_com_bomba = 0
	if lin > 0 and A[lin-1][col] == -1:
		posicoes_com_bomba += 1
	if lin < len(A) - 1 and A[lin+1][col] == -1:
		posicoes_com_bomba += 1
	if col > 0 and A[lin][col-1] == -1:
		posicoes_com_bomba += 1
	if col < len(A[0]) - 1 and A[lin][col+1] == -1:
		posicoes_com_bomba += 1
	return posicoes_com_bomba
3# b
def main():
	m = int(input("Numero de linhas: "))
	n = int(input("Numero de colunas: "))
	A = []
	for i in range(m):
		linha = []
		for j in range(n):
			linha.append(int(input("Digite A[%d][%d]: " % (i, j))))
		A.append(linha)
	for i in range(m):
		for j in range(n):
			print("Bombas ao redor de A[%d][%d]: %d" % (i, j, conta_bomba(A, i, j)))
main()

while tr:
	pass