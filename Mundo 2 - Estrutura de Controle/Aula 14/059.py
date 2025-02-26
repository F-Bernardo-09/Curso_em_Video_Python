# Construindo um menu de opções:
from random import randint
valor1 = int (input ('Digite um valor: '))
valor2 = int (input ('Digite outro valor: '))
opcao = 0
print ('-='*20)

while opcao != 5:
    print ('OPÇÕES: \n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] FECHAR PROGRAMA')
    opcao = int (input ('Qual opção você deseja? '))
    print('-=' * 20)
    if opcao == 1:
        soma = valor1 + valor2
        print (f'A soma entre os números {valor1} e {valor2} é igual a {soma}. ')
        print('-=' * 20)
    if opcao == 2:
        multi = valor1 * valor2
        print(f'A multiplicação entre os números {valor1} e {valor2} é igual a {multi}. ')
        print('-=' * 20)
    if opcao == 3 and valor1 == valor2:
        print (f'Os dois valores são iguais. ')
        print('-=' * 20)
    if opcao == 3 and valor1 > valor2:
        print (f'O valor {valor1} é maior que o valor {valor2}. ')
        print('-=' * 20)
    if opcao == 3 and valor1 < valor2:
        print (f'O valor {valor2} é maior que o valor {valor1}. ')
        print('-=' * 20)
    if opcao == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))
        print('-=' * 20)
    if opcao > 5:
        print ('Essa opção não existe, digite uma opção válida. ')
        print('-=' * 20)
    if opcao == 5:
        print ('Ok, fechamos nossas atividades. ')
        print('-=' * 20)
