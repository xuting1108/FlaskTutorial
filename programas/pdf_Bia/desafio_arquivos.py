#Complete o programa, sendo que o que ele faz é: 1. Ler em um arquivo csv os seguintes dados de Nome, Peso e Altura 2. Calcular o imc() e avaliar o valor do imc(). 3. Escrever um novo arquivo csv com os dados originais mais os dados calculados: imc e a avaliação
 
import csv
  
caminho = '/home/filipe/programas/pdf_Bia'
 
 
def get_nome():
    nome = input('Qual o seu nome? ')
    return nome
 
 
def get_peso():
    peso = float(input('Qual o seu peso? '))
    return peso
 
 
def get_altura():
    altura = float(input('qual a sua altura? '))
    return altura


def calcular_IMC():
	imc = peso / (altura ** 2)
	if imc < 18.5:
		return '{:.2f}'.format(imc), 'abaixo do peso'
	elif imc >= 18.5 and imc < 24.9:
		return '{:.2f}'.format(imc), 'normal'
	elif imc >= 25 and imc <29.9:
		return '{:.2f}'.format(imc), ('sobrepeso')
	elif imc >= 30 and imc < 34.9:
		return '{:.2f}'.format(imc), ('obesidade grau 1')
	elif imc >= 35 and imc < 39.9:
		return '{:.2f}'.format(imc), ('obesidade grau 2')
	else:
		return '{:.2f}'.format(imc), ('gordo pra cacete')

 	
quantidade = int(input('informe quantos nomes serao escritos: '))
indice = 0
pessoas = []
while indice < quantidade:
    nome = get_nome()
    peso = get_peso()
    altura = get_altura()
    imc = calcular_IMC()
 
    pessoas.append({'nome': nome, 'peso': peso, 'altura': f'{altura:.2f}', 'imc': imc})
 
    indice = indice + 1
 
with open(f'{caminho}/pessoas.csv', 'w', newline='') as arquivo:
    colunas = ['nome', 'peso', 'altura', 'imc']
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    for pessoa in pessoas:
        escritor.writerow(pessoa)
 
 
caminho = '/home/filipe/programas/pdf_Bia'
path = f'{caminho}/pessoas.csv'
 
with open(path, 'r') as arquivo: 
    reader = csv.DictReader(arquivo)
    for linha in reader:
        print(
            f"nome: {linha['nome']}, peso: {linha['peso']}, altura: {linha['altura']}, imc: {linha['imc']}"
        )


