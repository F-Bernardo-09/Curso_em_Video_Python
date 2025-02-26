# Casos de sorteio de nomes e/ou ordem:
import random
nome1 = str (input ('Digite o aluno um: '))
nome2 = str (input ('Digite o aluno dois: '))
nome3 = str (input ('Digite o aluno três: '))
nome4 = str (input ('Digite o aluno quatro: '))

lista = [nome1, nome2, nome3, nome4]
sorteio = random.choice (lista)
random.shuffle (lista)

print ('O sorteado será:', sorteio)
print ('A ordem será a  seguinte: ', (lista))
