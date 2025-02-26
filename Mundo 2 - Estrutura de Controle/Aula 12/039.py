# Alistamento Militar:
print ('Olá, patriota! \nEstamos sastifeitos pela sua presença aqui, siga as instruções abaixo: ')
nome = str (input ('Qual seu nome? ')) .strip() .title() .split()
idade = int (input ('Qual a sua idade {} {}? ' .format(nome [0], nome[-1])))
falta = 18 - idade

print (f'Ok, {nome[0]} {nome[-1]}, com base nisso, as orientações será as seguintes: ')

if idade < 18:
    print (f'Você é menor de idade, daqui a {falta} anos você volta aqui!')
elif idade >=18 and idade<45:
    print ('Você está na idade ideal de fazer seu alistamento! ')
else:
    print ('Você está velho, xará, vai aproveitar a aposentadoria... ')
