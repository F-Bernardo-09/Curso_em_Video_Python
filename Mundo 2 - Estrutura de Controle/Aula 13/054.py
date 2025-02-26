# Maior idade e menor idade:
soma18 = 0
soma17 = 0
for x in range (1,7):
    ano = int (input (f'Em que ano a {x}° pessoa nasceu?'))
    if 2024 - ano >=18:
        soma18 = soma18 +1
    else:
        soma17 = soma17 +1
print (f'O número de pessoas maior de idade é igual a {soma18}. \nEnquanto aos menores de idade {soma17}.')
