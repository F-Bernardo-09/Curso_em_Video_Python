# Listas
# Listas são mutaveis, existe comandos para adicionar, remover e substituir, além de organizar em ordem crescente e descrecente.

# Nesse comando  número que estava na posição 2: 1, foi substituído pelo número 4.
lista = [2, 6, 1, 5]
lista[2] = 4
print (lista)

print (' ')

# Nesse comando, vou adicionar primeiramente na ultima e segunda posição.
lista.append(10)
lista.insert(1,6)
print (lista)

print (' ')

# Nesse comando irei excluir o primeiro e último termo.
lista.pop(0)
lista.pop()
print (lista)

print (' ')

# Agora irei excluir um termo especifico:
lista.remove(6)
print (lista)

print (' ')

# Alterarei a ordem:
lista.sort()
print (lista)

lista.sort(reverse=True)
print (lista)

print (' ')

# Criando uma cópia da lista:
a = [1, 2, 3, 5]
'''b = a # Nessa função estabeleci uma relação, tudo que eu fizer na lista 'a' e/ou 'b', ambas serão alteradas.'''
b = a[:] #Criei uma cópia que as modificações não alterará a original.

