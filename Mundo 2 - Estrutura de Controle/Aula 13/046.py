# Contagem regressiva: fogos de artificio
from time import sleep
from emoji import *

for cont in range (3, 0, -1):
    print (cont)
    sleep(1)
print (emojize (':bomb:'))

print('-=' * 10)

# Seleção de números pares:
for par in range (0 , 51):
    if (par % 10 == 0):
        print (par)
