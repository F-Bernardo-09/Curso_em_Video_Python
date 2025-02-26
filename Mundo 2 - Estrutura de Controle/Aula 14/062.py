# Super Progressão Aritmetica usando While:
num = int (input ('Digite um número: '))
razao = int (input ('Qual a razão? '))
termo = num
contagem = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while  contagem <= total:
        print (f' {termo} -', end='')
        termo += razao
        contagem += 1

    print (' PAUSA')
    mais = int (input ('Quantos termos você quer mostrar a mais? '))
print ('FIM')
