# if: Condição verdadeira, o que tiver recuado é o chamado bloco.
# else: Condição falsa, usada para substituir a condição if.
import emoji

# Exemplo:
veiculo = int (input ('Quantos anos tem seu carro? '))
if veiculo<=3:
        print ('Ta novinho, xará')
else:
        print ('Tá velhinho, ein xará')

# Simplificando em poucas linhas:
veiculo1 = int (input ('Quantos anos tem seu carro? '))
print ('Ta novinho, xará' if veiculo1 <=3 else 'ta velhinho, ein xará')
