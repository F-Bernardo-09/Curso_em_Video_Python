# Tratando números:
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número: [999 pra parar] '))
    if num != 999:
        soma += num
        cont += 1

print(f'Você digitou {cont} números e a soma foi {soma}')
