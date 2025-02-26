# Aprendendo módulos padrão do Python:
import math
x = float (input ('Digite um valor para descobrir raiz quadrada: '))
raiz = math.sqrt(x)
print ('A raiz será igual a {:.2f}' .format(raiz))

# Para ter acesso a muitas bibliotecas padrões, apertar ctrl e espaço.
# Para ter acesso a muitas bibliotecas feitas por desenvolvedores, acessar site oficial.

# Aprendendo módulos do site do Python:
import emoji
print (emoji.emojize ('Python is :thumbs_up:'))
print(emoji.emojize('Python es :pulgar_hacia_arriba:', language='es'))
# Caso o arquivo importado seja em outra lingua que não seja o inglês, acessar o manual de como usar.

print (emoji.demojize('🌎 🏄‍♀️'))
print (emoji.emojize ('Olá, mundo!:globe_showing_Americas:'))
print (emoji.emojize ('Olá, mundo!:woman_surfing:'))
# Caso a importação esteja dando problema, ir nas configurações, Python Interpreter e baixar a importação por lá.
