from datetime import datetime
dados = {}

dados ['Nome'] = str (input ('Digite o seu nome: '))
Ano = int (input ('Ano de nascimento: '))
dados ['Idade'] = datetime.now().year - Ano
dados ['CLT'] = int (input ('Carteira de Trabalho (0 caso não tenha): '))

if dados ['CLT'] != 0:
    dados ['Contrato'] = int (input ('Ano de contratação: '))
    dados ['Salario '] = float (input ('Sálario: '))
    dados ['Aposetadoria'] = dados ['Idade'] + ((dados ['Contrato'] + 35 ) - datetime.now().year)

print ('-='*25)
for itens, valores in dados.items():
    print (f'   - {itens} tem o valor de {valores}')
