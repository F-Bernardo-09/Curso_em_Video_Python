# Coleta de dados e Verificação de informações:
somaidade = 0
mediaidade = 0
nomemaisvelho = ''
idademaisvelho = 0
idademulher = 0

for vezes in range (1, 4):
    print ('=-'*5, f'{vezes}ª Pessoa', '=-'*5)
    nome = str (input ('Seu nome: ')) .strip()
    idade = int (input ('Sua idade: '))
    sexo = str (input ('Seu sexo [M/F]: ')) .strip()
    somaidade += idade
    if vezes == 1 and sexo in 'Mm':
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > idademaisvelho:
        idademaisvelho = idade
        nomemaisvelho = nome

    if sexo in 'Ff' and idade <= 18:
        idademulher += +1

mediaidade = somaidade / vezes
print (f'A média de idade é {mediaidade:2} anos.')
print (f'O homem mais velho é {nomemaisvelho}, tendo {idademaisvelho} anos.')
print (f'Ao todo são {idademulher} mulheres menores de idade.')
