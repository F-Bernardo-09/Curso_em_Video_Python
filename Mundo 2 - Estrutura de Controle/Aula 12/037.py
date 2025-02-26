# Conversão de valores em menu:
num = int (input ('Digite um número inteiro: '))
print ('''Para converter em:
       [ 1 ] Binário
       [ 2 ] Octal
       [ 3 ] Hexadecimal''')
opp = int (input ('Digite a opção que deseja: '))

if opp == 1:
    print (f'O número {opp} convertido em binário é igual a: {bin(num) [2:]}. ')
elif opp == 2:
    print (f'O número {opp} convertido em octal é igual a: {oct(num) [2:]}. ')
elif opp == 3:
    print (f'O número {opp} convertido em hexadecimal é igual a: {hex(num)[2:]}. ')
else:
    print ('Erro ao digitar opções do menu, tente novamente!')
