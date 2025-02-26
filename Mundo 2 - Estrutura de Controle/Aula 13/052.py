# Condição para números primos:
num = int (input ('Número: '))
total = 0
for x in range (1, num +1):

    if num % x == 0:
        print ('\033[33m', end= ' ')
        total += 1

    else:
        print ('\033[31m', end= ' ')

    print (f'{x}', end=' ')
print (f'\033[m \nO número {num} foi dividido {total} vezes, logo: ')

if total ==2:
    print ('É PRIMO. ')
else:
    print ('NÃO É PRIMO. ')
