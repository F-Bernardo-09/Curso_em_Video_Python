lista = []
maior_posicao = []
menor_posicao = []
soma1 = soma2 = 0

for c in range (1, 5):
    valores = int (input (f'Digite um valor para posição {c}º: '))
    lista.append(valores)

for c, numero in enumerate(lista):
    if numero == max(lista):
        soma1 = maior_posicao.append(c +1)

    if numero == min(lista):
        menor_posicao.append(c+1)

print ('-='*20)
print (f'Os valores digitados foram: {lista}')
print (f'O maior valor digitado é {max(lista)}, estando na {maior_posicao}º posição.')
print (f'O menor valor digitado foi {min(lista)}, estando na {menor_posicao}º posição.')
