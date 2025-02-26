lista_principal = []

while True:
    nome = str (input ('NOME: '))
    nota1 = float (input ('NOTA 1: '))
    nota2 = float (input ('NOTA 2: '))
    media = (nota1 + nota2) / 2
    lista_principal.append ([nome, [nota1, nota2], media])
    opção = str (input ('DESEJA CONTINUAR [S/N]? '))
    if opção in 'Nn':
        break

print (lista_principal)
print('-=' * 5, 'BOLETIM', '=-' * 5)
print(f'{"Nº":<4}{"NOME ":<10}{"NOTA":>8}')
print('-' * 25)

for posição, aluno in enumerate(lista_principal):
    print (f'{posição:<4}{aluno[0]:<10}{aluno[2]:>8}')
    
print ('-='*30)
while True:
    opção2 = int (input ('Dados individuais: (999 para interromper)'))
    if opção2 == '999': 
        break
    else:
        print (f'A nota do aluno(a) {lista_principal[opção2][0]} foi: {lista_principal[opção2][1]}')
        print ('-='*10)
