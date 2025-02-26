# Analisando preços de produtos com nomes:
custo = quant = acima = menor = 0
menorproduto = ''

print ('-='*20)
print ('LOJA BARATÃO MÓVEIS' .center(40))
print ('-='*20)

while True:
    produto = str (input ('Qual o nome: ')) .strip() .title()
    preço = float (input ('Qual o preço em R$: '))
    custo += preço
    quant += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str (input ('Quer continuar [S/N]: ')) .upper() .strip() [0]

    if preço > 1000:
        acima += 1

    if quant == 1:
        menor = preço
        menorproduto = produto
    else:
        if preço < menor:
            menor = preço
            menorproduto = produto

    if resposta == 'N':
        break

print (f'O custo total dos {quant} produtos é R$ {custo:.2f}. ')
print (f'O total de produtos acima de R$ 1000,00 é {acima}.')
print (f'O produto com o preço mais barato se chama {menorproduto}, custando R$ {menor:.2f}. ')
