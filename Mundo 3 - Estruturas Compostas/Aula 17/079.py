lista = []
opcao = ''

while True:
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        lista.append(numero)
        lista.sort()
        print ('Armazenado com sucesso!')
    else:
        print('Número já existente na lista, não vou adicionar.')

    opcao = str(input('Quer continuar [S/N]?')).strip().upper()
    if opcao not in 'NnSs':
        opcao = str(input('[S/N]?')).strip().upper()
    if opcao in 'Nn':
        break

print ('-='*25)
print (f'Você digitou {lista}')


