# Estrutura de Repetição
for x in range (0, 4):
    print ('Olá, Mundo!')
    print ('Fim')

for y in range (4, 0, -1):
    print (y)

for z in range (0, 4):
    print (z)

for a in range (0, 7, 2):
    print (a)

print('-=' * 10)

num = int (input ('Digite um número: '))
for c in range (0, num +1):
    print (c)

# Pedindo notas para calculo de média:
for n in range (0,3):
    nota = float (input ('Digite sua nota: '))

print (f'Sua média foi igual a:  {(nota * 3) / 3}')
