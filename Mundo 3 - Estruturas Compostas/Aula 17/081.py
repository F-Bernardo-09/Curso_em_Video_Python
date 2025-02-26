lista = []

while True:
    valores = int (input ('Digite um valor: '))
    lista.append(valores)
    lista.sort (reverse=True)

    opcao = str (input ('Deseja continuar [S/N]: ')) .strip().upper()
    if opcao in 'SsNn':
        if opcao not in 'SsNn':
            print (opcao)
        if opcao in 'Nn':
            break

print ('-='*30)
print (f'Você digitou {len(lista)} números')
print (lista)
if 5 in lista:
    print ('Número 5 na lista...')
if 5 not in lista:
    print ('O número 5 não está na lista...')
