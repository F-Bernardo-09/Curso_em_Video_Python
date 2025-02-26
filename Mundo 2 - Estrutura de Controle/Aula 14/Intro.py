# Estrutura de Repetição: While

#Essa é a estrutura de repetição de contagem: FOR
for c in range (1, 10):
    print (c)
print ('Fim')

# Essa é a estrutura de repetição com lógica: WHILE
inicio = 0
while inicio < 10: #Enquanto o inicio for menor que 10: acrescentar sempre mais 1.
    inicio += 1
    print (inicio)
print ('Fim')

# Pergunta de permissão:
resposta = 'S'
while resposta == 'S':
    valor1 = int (input ('Digite um valor: '))
    resposta = str (input ('Quer continuar [S/N]? ')) .upper()
print ('Fim. ')

# Contagem de números usando while:
fechar = 1
contagempar = 0
contagemimpar = 0
subtotal = 0
total = 1
while fechar != 0:
    fechar = int (input ('Digite um número: '))
    if fechar % 2 == 0 and fechar != 0:
        contagempar += 1
    if fechar % 2 != 0:
        contagemimpar += 1
    if fechar != 0:
        subtotal += 1

print (f'A quantidade de números digitados foi igual a {subtotal}.')
if subtotal == 1:
    print (f'Sendo {contagempar} par e {contagemimpar} ímpar. ')
else:
    print (f'Sendo {contagempar} pares e {contagemimpar} ímpares. ')
