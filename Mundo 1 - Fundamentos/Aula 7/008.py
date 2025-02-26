# IMC e Conversão de tamanhos
altura = float (input ('Qual a sua altura em metros? '))
peso = float (input ('Qual o seu peso em kg? '))
cm = altura * 100
mm = altura * 1000
imc = peso / (altura ** 2)
print('O seu IMC será: {:.2f}' .format(imc))
print ('A sua altura em centimetros é {} e em milimetros {}' .format (cm, mm ))
