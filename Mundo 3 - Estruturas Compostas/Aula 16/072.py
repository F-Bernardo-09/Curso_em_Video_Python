# Criando uma tupla por extenso:
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int (input ('Digite um número entre 0 e 20: '))

    while numero not in range(0, 21):
        numero = int(input('Tente novamente. Digite um número entre 0 a 20: '))

    print (f'O número {numero} por extenso é: {extenso [numero]}. ')
    print ('-='*20)

    resposta = str (input ('Quer continuar [S/N]: ')) .upper() .strip() [0]
    if resposta == 'S':
        numero = int(input('Digite um número entre 0 e 20: '))

    if resposta == 'N':
            break
