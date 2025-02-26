temporario = []
principal = []
soma_pesos = pessoas = 0

while True:
    temporario.append (str (input ('NOME:')))
    temporario.append (float (input ('PESO: ')))
    soma_pesos += temporario[1]
    pessoas += 1
    principal.append(temporario[:])
    temporario.clear()

    opcao = str (input ('Deseja continuar [S/N]? ')) .strip() .upper ()
    if opcao in 'N':
        break 

media = soma_pesos / pessoas

print ('-='*30)
print (f'O número de pessoas cadastradas foram iguais a: {pessoas}.')
print (f'A média de pesos foi igual a: {media}.')

print ('Está abaixo da média do peso: ', end='')
for p in principal:
    if p[1] < media:
        print (f'{p[0]}', end=', ')

print ()
print ('Está acima da média dos pesos: ', end='')
for p in principal:
    if p[1] > media:
        print (f'{p[0]}', end=', ')
