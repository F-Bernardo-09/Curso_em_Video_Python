# Para calcular seno, cosseno e tangente com importação
from math import sin, cos, tan, radians
angulo = float (input ('Digite o ângulo que deseja? '))
seno = sin (radians (angulo))
cosseno = cos (radians (angulo))
tangente = tan (radians (angulo))

print ('O seno será {:.2f}.\nO cosseno {:.2f}.\nE a tangente {:.2f}.' .format(seno, cosseno, tangente))
