# Listas 2:

grupo1 = []
grupo1.append ('Bernardo')
grupo1.append ('19 anos')

grupogeral = []
grupogeral.append(grupo1[:])

grupo1 [0] = 'Maria'
grupo1 [1] = '17 anos'
grupogeral.append(grupo1 [:])

print (grupogeral)
for g in grupogeral:
    print (f'{g[0]} tem {g[1]}.')

    