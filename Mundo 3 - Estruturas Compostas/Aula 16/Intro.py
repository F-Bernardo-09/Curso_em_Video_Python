# Existe três tipos de tuplas, a ideia de tupla é criar uma lista, a primeira é usando parenteses.
# Tuplas são imutaveis.

# lista = 'suco', 'arroz', 'feijão'
lista = ('suco', 'arroz', 'feijão')
print (lista)
print (lista [1])

#Lembrando que começa do zero enumeração.
# Use os conceitos de Fatiamento de Strings.

for comida in lista:
    print (f'Eu vou comer {comida}; ')

print ('Showw')

for ordem in range (0, len(lista)):
    print (lista [ordem])

a = (1, 2 , 3, 5)
b = (5, 6, 7)
c = a + b
# Resumindo, são duas tuplas e quando 'a' mais 'b' juntas, elas se unem, mas não se somam. Inclusive, a ordem alterá os resultados.
# Para apagar os dados dessa Tupla, usa del
del (c)
