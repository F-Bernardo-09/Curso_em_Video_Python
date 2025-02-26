numero = 0
soma = 0
contagem = 0

while True:
    numero = int (input ('Digite um numero: '))
    if numero == 999:
        break
    soma += numero
    contagem += 1

print (f'Você digitou {contagem} número e a soma entre eles é igual a {soma}')
