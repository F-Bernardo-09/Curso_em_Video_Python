# Notas de avaliação:
from pygame import init, mixer, event

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2

if media <= 5.00:
    print('Sua nota foi abaixo da média, melhore! ')
    init()
    mixer.music.load('burro.mp3')
    mixer.music.play()
    input()
    event.wait()
else:
    print('Parabéns, superou o que achei que fosse capaz. ')
    init()
    mixer.music.load('genio.mp3')
    mixer.music.play()
    input()
    event.wait()
