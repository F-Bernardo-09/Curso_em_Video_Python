# Condição para cobrança de custos de viajem:
kilometragem = float (input ('Qual a distância da sua viajem em km? '))

if kilometragem<=200:
    print (f'O custo da sua viajem será igual a R$ {kilometragem*0.50}.')
else:
    print (f'O custo da sua viajem será igual a R$ {kilometragem*0.45}.')
