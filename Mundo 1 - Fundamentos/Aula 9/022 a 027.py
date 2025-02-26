# Testando as strings
nomecompleto = str (input ('Digite seu nome completo: ')) .upper() .strip()
letra = input ('Digite uma letra aleatória do seu nome: ').upper() .strip()

capi = nomecompleto.title()
separação = nomecompleto.split()
verificação = (separação [0])
verif = letra in verificação
variaveln = 'FRANCISCO' in nomecompleto
carat = len(nomecompleto)
quanta = nomecompleto.count(letra)
prim = nomecompleto.find(letra) + 1
ult = nomecompleto.rfind (letra) + 1
combinação1 = separação [0] .capitalize()
combinação2 = (separação [len(separação)-1]) .capitalize()


print (f'Sabendo que seu nome é {capi}, posso te chamar como: {combinação1} {combinação2}?')
print ('Será que a letra que você escolheu existe ou não no seu primeiro nome? A resposta é ',verif)
print ('Será que você é um "Francisco"?', variaveln)
print (f'O número total de caracteres é igual a {carat}, sendo a quantidade de letras "{letra}" é igual {quanta}, tendo a primeira localizada no caracter {prim} e a última no {ult}.')
