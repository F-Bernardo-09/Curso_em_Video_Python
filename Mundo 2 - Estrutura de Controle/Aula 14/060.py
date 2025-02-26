# Descobrindo o fatorial de um número, modelo 1:
from math import factorial
n = int (input ('Número para Fatorial: '))
f = factorial(n)

print (f'O Fatorial de {n} é {f}.')

# Descobrindo o fatorial de um número, modelo 2:
n = int (input ('Número para Fatorial: '))
c = n
f = 1
while c > 0:
    print (f'{c}', end=' ')
    print (' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print (f'{f}')
