# Condição para ultrapassagem e multa:
from emoji import emojize
velocidade1 = float (input ('Qual o limite de velocidade permitido nessa rua? '))
velocidade2 = float (input ('Qual a velocidade que você alcançou? '))
diferença= velocidade2 - velocidade1
resul = diferença * 7.00

print (f'Se a velocidade permitida é {velocidade1} km/h e você chegou a {velocidade2} km/m:')
if diferença>0:
    print (f'Você superou o limite de velocidade, como multa da diferença do limite permitido {velocidade1}, receberá R$ {resul} como multa.')
else:
    print (emojize ('Continue assim, respeitando as leis do trânsito :police_car_light:'))
