# Condição para aumento salarial:
salaa = int (input ('Qual o seu sálario?'))

if salaa>=1250.00:
    print (f'O seu nome sálario será igual a: {salaa + (salaa * 0.1):.2f}')
else:
    print (f'O seu nome sálario será igual a: {salaa + (salaa * 0.15):.2f}')
