# Contruindo uma tabuada com repetição e finalizando ela:
while True:
    print('-=' * 24)
    numero = int(input('Qual o número que você deseeja ver a tabuada? '))
    if numero <= 0:
        break
    print(f'A tabuada do número {numero} é:')
    for tab in range (1, 11):
        print (f'{numero} x {tab} = {numero*tab}')

print ('Ok, chegamos ao fim...')
