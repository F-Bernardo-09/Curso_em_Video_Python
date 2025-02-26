# Progressão Aritmetica usando While:
num = int (input ('Digite um número: '))
razao = int (input ('Qual a razão? '))
termo = num
contador = 1

while contador <= 10:
    print (f'{termo} - ', end='')
    termo += razao
    contador += 1

print ('Fim')
