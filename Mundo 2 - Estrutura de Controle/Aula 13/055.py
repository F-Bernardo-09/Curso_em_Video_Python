# Identificando o maior e menor peso:
maior = 0
menor = 0
lista = [] #Criar uma lista vazia é mais fácil.

for peso in range (1,5):
    peso1 = float (input (f'{peso}° pessoa peso: '))
    lista += [peso1] #Lista vazia recebendo os pesos

    if peso ==1:
        maior = peso1
        menor = peso1
    else:
        if peso1 > maior:
            maior = peso1
        if peso1 < menor:
            menor = peso1

print (f'A pessoa mais pesada, pesa {maior} kgs. \nEnquanto a mais leve {menor} kgs.')
print (f'A pessoa mais pesada, pesa {max(lista)} kgs. Enquanto a mais leve {min(lista)} kgs.')
