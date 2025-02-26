# As variaveis que estarão abaixo serão uteis para exemplificar todas as operações
variavel1 = float (input ('Digite um número:'))
variavel2 = float  (input ('Digite outro número:'))
resultadodasoma = variavel1 + variavel2
resultadodasubtração = variavel1 - variavel2
resultadodamultiplicação = variavel1 * variavel2
resultadodadivisão = variavel1 / variavel2
resultadodamedia = (variavel1 + variavel2) / 2
resultadodapotencialização = variavel1 ** variavel2
resultadodadadivisãointeira = variavel1 // variavel2
resultadodorestantedadivisão = variavel1 % variavel2

print ('O resultado da soma entre os dois números será igual {}, da subtração será {}, da multiplicação {}, da divisão {:.3f}, da média {} e da por fim, o resultado da potencialização {}. \n Inclusive, o resultado da divisão inteira será {} e o restante dela igual {}.' .format(resultadodasoma, resultadodasubtração, resultadodamultiplicação, resultadodadivisão, resultadodamedia, resultadodapotencialização, resultadodadadivisãointeira, resultadodorestantedadivisão))
# O uso de {:.3f} significa que o limite será 3 casas flutuantes. Podendo ser substituida por outros números ou funções.
