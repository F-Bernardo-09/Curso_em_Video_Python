# Progressão aritmética:
print ('OS 10 TERMOS DA PA: ')
primeiro = int (input ('Primeiro termo: '))
razao = int (input ('Razão: '))
decimo = primeiro + (11 - 1) * razao

for pa in range (primeiro, decimo, razao):
    print (pa, end = ' + ')
print ('Fim')

print('-=' * 10)
