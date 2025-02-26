# Números sortidos entre chance de acerto e erro
from random import randint
x = randint (0, 5)
y = int (input('Entre 0 e 5, qual o número que estou imaginando? '))
print('O número pensado foi: ', x)
if y==x:
    print ('Acertou, mizeravi')
else:
    print ('Tu perdeu para uma máquina, seu animal!')
