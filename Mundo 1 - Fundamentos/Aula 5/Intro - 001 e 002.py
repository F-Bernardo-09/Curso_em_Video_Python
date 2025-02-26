# Aprendendo um pouco sobre os códigos
print('Olá, amigo!')
nome=input ('Qual o seu nome?')
idade=input ('Qual a sua idade,' + nome + ' ?' )
print('O seu nome é ' + nome + ', e sua idade é ' + idade + ', correto?')
numero=input ('Bom, podemos brincar um pouco? Eu vou adivinhar o número que você pensou, mas antes disso, digite ele:')
resultado=input ('O número que você pensou foi: ' +  numero)
print('Acertei, não foi? HEHEHEHE')

x=input ('Digite algo uma palavra com números e veja a sua classificação:')
print (x.isalnum())
#isalnum: Company12, exemplo

print (x.isalpha())
#isalpha: CompanyX, exemplo

print (x.isascii())
#isascii: Company123, exemplo

print (x.isdigit())
#isdigit: 50800, exemplo

print (x.islower())
#islower: hello word, exemplo

print (x.isdecimal())
#isdecimal: 0123456789, exemplo

print (x.isidentifier())
#isidentifier:

print (x.isnumeric())
#isnumeric: \u0030, exemplo

print (x.isspace())
#isspace: '   '

print (x.istitle())
#istitle: Hello, Word, exemplo

print (x.isupper())
#isupper: HELLO, WORD, exemplo