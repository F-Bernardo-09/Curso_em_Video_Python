# Selecionando números múltiplos de 3, ímpares e somando seus valores:
soma = 0
variavel = 0

for multiplo in range (1,501, 2):
    if multiplo % 3 == 0:
        soma = soma + multiplo
        variavel = variavel + 1

print (f'O número múltiplos de 3 ímpares é igual a {variavel} e a soma deles todos é igual a {soma}.')

print('-=' * 10)
