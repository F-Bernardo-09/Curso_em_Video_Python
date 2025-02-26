# Brincado de par ou ímpar:
from random import randint
from time import sleep

print('Vamos brincar de par ou ímpar! ')
nome = str(input('Qual o seu primeiro nome, jogador? ')).title()
vitoria = 0

print('-=' * 20)
print('REGRAS:')
print('''1. Você escolhe se quer 'Par' ou 'Ímpar';
2. Eu e você pensaremos em um número e digitamos sem o outro saber;
3. Em 3 segundos soltamos o resultado; 
4. Se você ganhar, o jogo continua, se você perder, paramos e veremos os resultados. 
5. Lembrando que é entre 1 e 10. ''')
print('-=' * 20)

while True:
    print('MENU: ')
    print('[ 1 ] Par \n[ 2 ] Ímpar')
    resposta = int(input(f'Vai em qual, {nome}? '))
    print('-=' * 20)

    if resposta == 1 or resposta == 2:
        dedos = int(input('Digite quantos dedos você pensou: '))
        print('Pronto, resultado ein... ')
        cpu = randint(1, 11)

        # Conferindo a soma dos dedos...
        resultado = (dedos + cpu) % 2

        # Contagem regressiva para resultado...
        print('3')
        sleep(1)
        print('2')
        sleep(1)
        print('1')
        sleep(1)

        # Condição para quantidades de dedos inexistentes...
        if dedos == 0:
            print('-=' * 20)
            print('Você tem dedos nas mãos, né? ')
            dedos = int(input('Digite quantos dedos você pensou: '))
            print('-=' * 20)

        # Condição para quantidades de dedos inexistentes...
        if dedos > 10:
            print('-=' * 20)
            print('Você não tem mais dedos que 10, né? ')
            dedos = int(input('Digite quantos dedos você pensou: '))
            print('-=' * 20)

        # Condição entre par que eu ganho...
        if resposta == 1 and resultado == 0:
            print('Ok, essa partida foi sua, continuemos...')
            print(f'Eu pensei em {cpu} dedos, e você {dedos}, somando é um número par.')
            print('-=' * 20)
            vitoria += 1

        # Condição entre par que eu ganho...
        if resposta == 2 and resultado != 0:
            print('Ok, essa partida foi sua, continuemos...')
            print(f'Eu pensei em {cpu} dedos e você {dedos}, somando é um número ímpar. ')
            print('-=' * 20)
            vitoria += 1

        # Condição entre par e ímpar que eu perco...
        if resposta == 1 and resultado != 0:
            print(
                f'Ihh, pelo que parece você perdeu... \nEu pensei em {cpu} dedos e você {dedos}, somando é um número ímpar. ')
            break

        if resposta == 2 and resultado == 0:
            print(
                f'Ihh, pelo que parece você perdeu... \nEu pensei em {cpu} dedos e você {dedos}, somando é um número par. ')
            break

    else:
        resposta = int(input(f'Hummm, escolha um número que esteja no menu, {nome}? '))

print(f'O número de vitórias que você obteve foi igual a {vitoria}. ')

# FIM
