# Ordem númerica: Qual o maior e menor número
n1 = int (input ('Número 1: '))
n2 = int (input ('Número 2: '))
n3 = int (input ('Número 3: '))
lista = (n1, n2, n3)

# Verificando quem é o menor:
'''menor = n1
if n1 < n2 and n2 < n3:
    menor = n2
if n2 < n1 and n2 < n3:
    menor = n3
if n3 < n1 and n3 < n2:

# Verificando quem é o maior:
    maior = n1
if n1 > n2 and n1 > n3:
    maior = n2
if n2 > n1 and n2 > n3:
    maior = n3
if n3 > n1 and n2 < n3:

print (f'O maior número é: {maior}.')
print (f'O menor número é: {menor}.')'''

# Verificando de forma muito mais simples:
print (f'O maior número é: {max(lista)}.')
print (f'O menor número é: {min(lista)}.')
