lista = [[], []]
numero = 0
print ('A seguir, digite números aleatórios: ')

for l in range (1, 8):
    numero = (int (input (f'{l}º: ')))

    if numero % 2 == 0:
        lista[0].append (numero)
    else: 
        lista[1].append (numero)

lista[0].sort()
lista[1].sort()
print (f'Os números pares digitados foram: {lista[0]}')
print (f'Enquanto aos números ímpares: {lista[1]}')
