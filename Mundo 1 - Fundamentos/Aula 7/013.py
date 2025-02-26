#Conversão de valores em dinheiro e implementação de taxa de acrescismo e diminuição
salario = float (input ('Qual o seu sálario? '))
taxa = float (input ('Qual a porcentagem de acréscismo que gostaria de ter? '))
custo = float (input ('Quanto sobra do teu sálario? '))
dolar = salario / 5.27
aument = salario * taxa / 100
acresc = salario + aument
saldo  = (salario - custo) / salario
porcentagem = saldo * 100
print ('O seu sálario é {}, se converter em dólar, teria como valor {}, o seu sálario dos sonhos seria {} e o lucro do atual custo é {}%. ' .format(salario, dolar, acresc, porcentagem))
