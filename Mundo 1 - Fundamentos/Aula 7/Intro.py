# Operações matemáticas
numero1=input ('Agora que acertei o número que você pensou, diga um número:')
numero2=input ('Diga outro número, veja a mágica acontecer, irei somar os dois, mas claro, digite ele a frente: ')
print ('A soma desses dois números será igual a: ' + numero1 + numero2 )

n=input ('Valor um:')
print (type(n))

end1 = input ('Digite um valor qualquer')
end2 = input ('Digite outro valor')
print ('Agora uma outra função útil para continuidade é o , end=, pega a visão, esse é o valor que você citou primeiro {}. '.format(end1), end='')
print ('O segundo valor é esse outro {}, você citou em linhas de código distintas, entretanto elas se unem usando o , end=' .format(end2))
# O caso oposto do "end= '' " é o "n\" , ele faz a quebra da linha ao utilizar o código.

# Maior e Menor valor com vários números e opção de menu:
opcao = 'S'
contador = media = somador = maior = menor = 0

while opcao in 'S':
    numero = int (input ('Digite um número: '))
    contador += 1
    somador += numero

    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    opcao = str (input ('Quer continuar [S/N]? ')) .upper() .strip()

    if opcao != 'S' and opcao != 'N':
        opcao = str(input('Opção inválida. \nQuer continuar [S/N]? ')).upper().strip()

media = somador / contador

if contador == 1:
    print (f'Foi apenas digitado o número {numero}, então não existe outro para ser comparado. ')

if contador >= 2 and numero == menor and numero == maior:
    print (f'Você digitou {contador} números e a média foi igual a {media:.2f}.')
    print (f'Todos os números são iguais. ')

if contador > 1 and maior > menor:
    print (f'Você digitou {contador} números e a média foi igual a {media:.2f}.')
    print (f'O maior número foi {maior} e o menor {menor}. ')
