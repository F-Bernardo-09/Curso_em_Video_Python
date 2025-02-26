from math import trunc
#Calcular área e custo de tinta
pared1 = float (input ('Qual a altura da sua parede em metros? '))
pared2 = float (input ('Qual a largura da sua parede em metros? '))
litro = float (input ('Quantos litros de tinta no balde? '))
tinta = float (input ('Qual o valor do balde de tinta que deseja? '))
area = pared1 * pared2
tinta1 = area * 2
balde = tinta1 / litro
preço = balde * tinta

print ('Sabendo que a quantidade de metros quadrados é {}, serão necessarios {} litros de tinta, logo, {} baldes com o valor de {}, custando no total {} reais' .format(area, tinta1, trunc(balde), tinta, preço))
