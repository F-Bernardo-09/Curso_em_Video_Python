ordem = []
for lista in range (0,5):
    variavel = int(input('Digite um número: '))
    if lista == 0 or variavel > lista [len(ordem)-1]:
        print ('Adicionado ao final da lista.')
        ordem.append(variavel)

    else:
        posicao = 0
        while posicao < len(ordem):
            if variavel < ordem [posicao]:
                ordem.insert(posicao, variavel)
                print (f'Adicionado na posição {posicao}.')
            posicao += 1

print ('-='*20)
print (f'Os valores digitados foram: {ordem}')
