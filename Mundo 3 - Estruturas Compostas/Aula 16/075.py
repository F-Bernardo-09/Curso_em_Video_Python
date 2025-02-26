# Adicionando valores em Tuplas:
valores = tuple (int(input('Digite valores: ')) for c in range(1, 5))

print(f'O numero nove aparece {valores.count(9)} vezes;')

if 3 in valores:
    print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição;')

else:
      print ('Não foi digitado valor 3;')

print('Valores pares digitados foram: ', end=' ')
for pares in valores:
    if pares % 2 == 0:
        print (pares, end=', ')
