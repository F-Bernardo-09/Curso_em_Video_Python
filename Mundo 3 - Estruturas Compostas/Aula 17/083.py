# Analisando expressão em válida e inválida através do números de parenteses.

expr = str (input ('Digite a expressão: '))
open = expr.count('(')
close = expr.count(')')
if expr.index(')') > expr.index('('):
    if open == close:
        print ('Expressão válida')
    else:
        print ('Expressão é inválida')

else:
    print ('Expressão inválida')
