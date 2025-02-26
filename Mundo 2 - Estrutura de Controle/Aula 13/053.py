# Detector de Palíndromo:
nome = str (input ('Frase: ')) .upper() .strip()
separando = nome.split()
juntando = ''.join(separando)
inverso = ''

# Outra forma é a abaixo:
# inverso = juntando [::-1]

for letra in range (len(juntando) -1, -1, -1):
    inverso += juntando [letra]
print (f'O inverso de {juntando} é {inverso}.')

if inverso == juntando:
    print ('Essa palavra é Palidromo. ')

else:
    print ('Essa palavra não é um palidromo')
