# Fatiamento de String, tipos e exemplos:
frase = (' Quero ser programador em Python, estou aprendendo. ')

print (frase[3])
# Nessa situação acima, dentro daa frase escolhida, o quarta caracter aparecerá na tela, sempre acrescentando + 1.
# Essa soma se deve porque o primeiro caracter é zero, é um macete.

print (frase[3:8])
# Nessa situação, os caracteres escolhidos será do 3° caracter até o 8°.

print (frase[8:])
# Os caracteres selecionados será apartir do número selecionado, sem fim.

print (frase[:8])
# Os caracteres iniciarão do começo e somente vão parar no número selecionado.

print (frase[:37:2])
# Nessa situação, serão selecionados os números entre o caracter inicial e o último, pulando duas casas de caracteres.

print (frase[::])
# Nessa situação, terá desde o seu inicio até o seu final copiado.

print (frase.count('o'))
# Contará quantos "o" tem na frase, lembre-se que letras maiusculas e minusculas são diferentes.

print (frase.upper().count('AMADOR'))
# Dentro dos caracteres maisculas, encontrar as minusculas.

print (frase.upper().count('amador'))
# Esse código vai identificar zero, porque os caracteres selecionados está em minuscula, sendo que o código teria que estar em maiuscula.

print (len(frase))
# Identiifica quantos caracteres tem na frase.

print (len (frase.strip( )))
# Não será contado dentro dos caracteres os espaços ou caracteres selecionados.

print (frase.replace('programador', 'garoto de programa'))
# Substitui caracteres definidas no objeto por novos.

print ('Python' in frase)
# Faz a leitura de caracteres especificos para verificação na frase.

print (frase.find('Python'))
# Faz uma procura dos caracteres desejados para localizar na frase.
# OBS: Caso seja procurado uma palavra e não tendo ela na frase, aparecerá -1, porque estaria antes de zero. Identificando que não tem.

print (frase.lower().find('python'))
# Faz a identificação da posição da palavra na frase mesmo sendo escrita em letra minuscula.

dividido = frase.split()
# Separa os caracteres divididos pelo espaço, separando em grupos.
print (dividido[1])
# Seleciona o grupo especifico que você deseja.

print (dividido[::] [1] [0])
# Seleciona dentro da frase inteira o grupo e após, a letra na posição que deseja.

print (frase.upper())
# ESCREVE TODO EM MAISCULO

print (frase.lower())
# escreve todo em minusculo

print (frase.islower())
# Identifica se está todo em minusculo.

print (frase.isupper())
# Verifica se está todo em maisculo.

print (frase.capitalize())
# Coloca todas as letras em minusculo, exceto a primeira.

print (frase.title())
# Coloca todas as letras após os espaços em maiuscula.

print (frase.strip())
# Retira todos os espaços antes do caracter útil e após.
# Caso colocado .rstrip, somente os espaços da direita serão retirados, colocando l.strip, acontecerá com a esquerda.

print ('-'.join(frase))
# Separa todas os caracteres com travessão.

print ('-'.join(dividido))
# Separa todos os grupos criados em .join pelo caracter selecionado.

# Testando as strings 01
nome = input ('Digite seu nome completo: ')
maiusc = nome.upper ()
minus = nome.lower ()
caracterestotais = len (nome)
#caracteres = len (nome.strip())
caracteres = len(nome) - nome.count(' ')
nome1 = nome.split () [0]
nome2 = len (nome.split () [0])

print ('Seu nome em upper ficará igual a {}, em lower {}, o números de caracteres é igual a {}, sem contar os espaços, será igual a {} e por fim, o primeiro nome é: {}, tendo {} caracter.' .format(maiusc, minus, caracterestotais, caracteres, nome1, nome2))

# Testando as strings 02
#x = int (input ('Digite um número entre 0 e 9999: '))
#y = str (x)
#print (f'Milhar {y[0]}. \nCentena {y[1]}. \nDezena {y[2]}. \nUnidade {y[3]}.')

# Outra maneira mais inteligente a se fazer o "Testando as strings 02":
num = int (input ('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print (f'Unidade: {u}. \nDezena: {d}. \nCentena: {c}. \nMilhar: {m}.')
