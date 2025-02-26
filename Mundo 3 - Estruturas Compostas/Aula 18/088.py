from random import randint
from time import sleep
tot = 1
lista = []
jogos = []

print ('-='*30)
print ('PALPITES DA MEGA CENA'.center(30))
print ('-='*30)
quant = int (input ('Quantos palpites deseja ter? ')) 

while tot <= quant:
    cont = 0 
    while True:
        num = randint (1, 60)
        if num not in lista:
            lista.append (num)
            cont += 1
        if cont >= 6:
            break

    tot += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print ('-='*30)
print ('POSSIVEIS RESULTADOS:'.center(30))
for i, l in enumerate (jogos):
    print (f'Resultado {i+1}: {l}')
    sleep (1)
