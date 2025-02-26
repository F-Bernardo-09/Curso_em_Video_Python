# Capturando váriaveis pares e somando-as:
somando = 0
contando = 0
for variavel in range (1,7):
    num = int (input (f'Digite o valor número {variavel}:'))
    if num % 2 == 0:
        somando += num
        contando += 1
print (f'A quantidade de números pares é {contando}, enquanto a soma deles é igual a {somando}.')
