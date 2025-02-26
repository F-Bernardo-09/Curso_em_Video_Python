# Tratamento de dados:
mulhermenor20 = totalhomens = totalmaior18 = 0

while True:
    print ('-='*20)
    print ('CADASTRE UMA PESSOA:')
    idade = int (input ('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
    # Esse 'While' é capaz de causa repetição enquanto não for digitado a resposta correta.
        sexo = str (input ('Sexo [M/F]: ')) .upper() .strip() [0]

    if idade < 20 and sexo == 'M':
        mulhermenor20 += 1

    if sexo == 'M':
        totalhomens += 1

    if idade > 18:
        totalmaior18 += 1

    print('-=' * 20)
    continuação = ' '
    while continuação not in 'SN':
        continuação = str(input('Quer continuar [S/N]: ')) .upper().strip() [0]

    if continuação == 'N':
        break

print('-=' * 20)
print (f'O número de mulheres menores de 20 anos foi igual a {mulhermenor20}.')
print (f'O total de homens igual a {totalhomens}.')
print (f'Enquanto o número de homens e mulheres maiores que 18 anos foi {totalmaior18}.')
