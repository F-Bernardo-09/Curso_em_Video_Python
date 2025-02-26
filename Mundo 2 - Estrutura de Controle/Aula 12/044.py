# Condição de pagamento de produtos:
reais = float (input ('Qual o valor do produto que você deseja em R$? '))
print ('''[ 1 ] PAGAMENTO A VISTA DINHEIRO/CHEQUE.
[ 2 ] Á VISTA NO CARTÃO.
[ 3 ] DUAS VEZES NO CARTÃO.
[ 4 ] TRÊS VEZES NO CARTÃO.''')

menu = int (input ('Entre as opções acima, qual a forma de pagamento que deseja? '))

if menu == 1:
    print (f'Você recebeu 10% de desconto, alcançando como valor R$ {reais - (reais * 0.1)}')
elif menu == 2:
    print (f'Você recebeu 5% de desconto, alcançando como valor R$ {reais - (reais * 0.05)}')
elif menu == 3:
    print (f'Você pagará em duas parcelas de R$ {reais / 2}.')
elif menu == 4:
    print (f'Você pagará em três parcelas de R$ {reais + (reais * 0.2)}, já incluso nelas o acréscimo de 20%, sendo R$ {reais * 0.2}.')
else:
    print ('Essa forma de pagamento não exite. Tente novamente. ')
