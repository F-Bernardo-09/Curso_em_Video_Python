armazenamento = {}

print ('Olá, bom dia!')
armazenamento['Nome'] = str (input ('Seu nome: '))
armazenamento['Média'] = float (input (f'Qual a sua média {armazenamento["Nome"]}: '))

if armazenamento['Média'] <= 5: 
    armazenamento['Situação'] = 'reprovado.'
elif armazenamento['Média'] >= 6:
    armazenamento['Situação'] = 'aprovado.'
    
print ('-='*20)
for k, v in armazenamento.items():
    print (f'{k} é igual a {v}')
