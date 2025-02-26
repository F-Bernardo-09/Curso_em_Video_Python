from random import randint
from _operator import itemgetter
from time import sleep

jogadas = {'jogador1': randint(1, 6), 
           'jogador2': randint(1, 6), 
           'jogador3': randint(1, 6), 
           'jogador4': randint(1, 6) }
tabela = list ()

print ('-='*20)
print ('VALORES SORTEADOS:')
print ('-='*20)

for jogadores, valor in jogadas.items():
    print (f'O {jogadores} tirou {valor} no dado.')
    sleep (1)

tabela = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print ('-='*20)
for posição, resultado in enumerate (tabela): 
    print (f'{posição + 1}º está {resultado[0]} que tirou {resultado[1]} no dado.')
    sleep (1)
    