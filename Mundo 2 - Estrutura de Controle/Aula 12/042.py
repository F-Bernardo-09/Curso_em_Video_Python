# Segmentos de reta para formar triângulo:
# Condição de existência: a soma de dois lados é sempre menor que o terceiro lado.

r1 = float(input('Reta um: '))
r2 = float(input('Reta dois: '))
r3 = float(input('Reta três: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar esse triângulo.')
    if r1 == r2 and r2 == r3 and r1 == r3:
       print ('Inclusive, é um triângulo Equilátero.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
       print ('Inclusive, é um triângulo Isósceles.')
    elif r1 != r2 and r1 != r3 and r3 != r2:
       print ('Inclusive, é um triângulo Escaleno. ')
else:
    print('Esses três segmentos de reta não favoreecm a construção de um triângulo.')
