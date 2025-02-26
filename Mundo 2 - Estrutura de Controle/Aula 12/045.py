# GAME: JOKENPÔ
from random import randint
from time import sleep
itens = ('Pedra' , 'Papel' , 'Tesoura')
cpu = randint (0, 2)

print ('Vamos brincar!')
print ('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')

jogada = int (input ('Qual a sua jogada? '))
print ('-=' * 20)

print (f'SUA JOGADA FOI: {itens [jogada]}')
print (f'A JOGADA DO SEU OPONENTE FOI: {itens [cpu]}')
print ('-=' * 20)

print ('JO')
sleep (2)
print ('KEN')
sleep (2)
print ('PÔ')
sleep (2)

print ('-=' * 20)

if jogada == 0:
    if cpu == 0:
       print ('EMPATE')
    elif cpu == 1:
        print ('VOCÊ PERDEU, O COMPIUTER VENCEU ESSA!')
    elif cpu == 2:
        print ('VOCÊ GANHOU DO COMPIUTER!')

elif jogada == 1:
    if cpu == 0:
        print ('VOCÊ GANHOU DO COMPIUTER!')
    elif cpu == 1:
        print ('EMPATE')
    elif cpu == 2:
        print ('VOCÊ PERDEU, O COMPIUTER VENCEU ESSA!')

elif jogada == 2:
    if cpu == 0:
        print ('VOCÊ PERDEU, O COMPIUTER VENCEU ESSA!')
    if cpu == 1:
        print ('VOCÊ GANHOU DO COMPIUTER!')
    if cpu == 2:
        print ('EMPATE')
