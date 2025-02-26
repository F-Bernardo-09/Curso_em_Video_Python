# Buscando dados em Tuplas:
classificação = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético - Mg', 'Athletico - Pr',
                 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthias', 'Chapecoense', 'Ceará',
                 'Vasco da Gama', 'Sport', 'América - Mg', 'Vitoria', 'Paraná')
# Parte 1:
for cinco in range (0, 6):
    print (f'O {cinco + 1}º colocado foi {classificação[cinco]}. ')
print ('-='* 20)

# Parte 2:
print (f'Enquanto aos últimos 4 colocados: {classificação [-4:]}')
print ('-='* 20)

# Parte 3:
print (f'Em ordem analfabetica, fica assim: \n{sorted(classificação)}')
print ('-='* 20)

# Parte 4:
print (f'O Chapecoense está na posição: {classificação.index('Chapecoense') +1}º.')
