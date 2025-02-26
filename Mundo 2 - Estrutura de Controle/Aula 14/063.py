# Sequência de Fibonacci
print ('SEQUÊNCIA DE FIBONACCI')
print ('-='*25)
r1 = 0
r2 = 1

variavel = int (input ('Qual a quantidade de números que deseja? '))
print (f'{r1} - {r2} - ', end='')
contador = 3
while contador <= variavel:
    r3 = r1 + r2
    contador += 1
    print (f'{r3} - ', end='')
    r1 = r2
    r2 = r3

print ('Fim')
