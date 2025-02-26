# Cores no terminal

'''
# Style:
0 = None, ou simplesmente nem usar.
1 = Bold
4 = Underline
7 = Reverso das cores:

# Cores das letras:
30 = letra branca
31 = letra vermelha
32 = letra verde
33 = letra amarela
34 = letra azul claro
35 = letra lilás
36 = letra ciano
37 = letra cinza

# Cores do Fundo:
40 = Fundo branco
41 = fundo vermelho
42 = fundo verde
43 = fundo amarelo
44 = fundo azul claro
45 = fundo lilás
46 = fundo ciano
47 = fundo cinza
'''

# Como usar:
nome = 'Nome pintado'

print ('\33[0;30;47m {}' .format(nome))
print ('\033[0;30;47m {} \033[m' .format(nome))
print ('\33[4;37;44m {} \033[m' .format(nome))
print ('\33[7;37;44m {} \033[m' .format(nome))

# Organizando as cores:
'''cores = {
    'azulclarobold' : '\033[40',
    'fundovermelho' : '\033[41',
    'limite' : '\033[m'
}

print (f'{(cores['azulclarobold'])}{nome}{(cores['limite'])}')'''

from colorama import init, Fore, Back
init()
print (Fore.MAGENTA, Back.LIGHTBLACK_EX,'Testando o Colorama' '\033[m' )
