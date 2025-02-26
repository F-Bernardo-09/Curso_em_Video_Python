# Jogo de adivinhação entre números:
from random import randint
print ('Olá, eu sou seu computador... Vamos brincar de adivinhação. ')
numero = int (input ('Entre 0 e 10, qual o número que pensei? '))
adivinhacao = randint (1, 10)
tot = 0

while numero != adivinhacao:
    tot += 1
    if numero > adivinhacao:
        print ('Diminua mais, quase lá! ')
        numero = int(input('Qual o número que pensei? '))
    else:
        print ('Aumente mais, quase lá! ')
        numero = int(input('Qual o número que pensei? '))

print (f'Você percisou de {tot} tentativa para acertar. ')
print ('Mas isso não tira o seu acerto, acertou miseraví...')
