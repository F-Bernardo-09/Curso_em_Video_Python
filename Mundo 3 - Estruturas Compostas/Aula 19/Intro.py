# Aula de teste
estado = {} #estado = dict()
brasil = [] #brasil = list()

for c in range (0, 3):
    estado['uf'] = str (input ('ESTADO BRASILEIRO: '))
    estado['sigla'] = str (input ('SIGLA DO ESTADO: '))
    brasil.append (estado.copy())

print ('-='*10)
for e in brasil:
    for v in e.values():
        print (v, end= ' ')
    print ()
