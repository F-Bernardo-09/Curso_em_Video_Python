# Sistema de Emprestimo:
print ('-='*20)
print ('Bem vindo!')
print ('-='*20)

valor = int (input ('Você deseja sacar quanto? '))
print ('-='*20)

total = valor
ced = 50
quant = 0

while True:
    if total >= ced:
        total -= ced
        quant += 1
    else:
        if quant > 0:
            print (f'{quant} cédulas de R$ {ced:.2f}. ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        quant = 0
        if total == 0:
            break

print ('-='*20)
print ('Volte sempre! ')
