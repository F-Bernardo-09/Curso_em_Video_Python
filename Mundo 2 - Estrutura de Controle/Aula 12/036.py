# Exercicio de emprestimo
from colorama import Back, Fore
valor = float (input('Qual o valor da casa de seu interesse? '))
salario = float (input ('Qual o valor do seu sálario? '))
anos = float (input ('Você quer pagar em quantos anos? '))

mensalidade = valor / (anos * 12)
porcen = salario * 0.3

if mensalidade <= porcen:
    print (Fore.GREEN, 'Seu empréstimo foi ACEITO! ' '\033[m')
else:
    print (Back.RED, Fore.BLACK, 'Seu empréstimo foi NEGADO! ' '\033[m')
