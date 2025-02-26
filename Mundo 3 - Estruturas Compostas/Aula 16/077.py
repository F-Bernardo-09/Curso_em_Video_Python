# Atividade relacionada a encontrar vogais na Tupla:
palavras = ('eu', 'quero', 'aprender', 'python', 'nao', 'vou', 'desistir',
            'programacao', 'massa', 'provedor', 'de', 'oportunidades')

for p in palavras:
    print (f'\nNa palavra {p.upper()} temos: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print (letras, end=', ')
