# Refazer a tabuada usando for:
numero = int (input ('Digite um valor para calcularmos sua tabuada: '))
for tab in range (1, 11):
   print (f'{numero} x {tab} = {tab*numero} ')
