# Pedindo informações especificas:
pergunta = str(input('[M/F]')) .upper() .strip() [0]
while pergunta not in 'MF':
    pergunta = str (input ('Sexo invalidado, digite [M/F]: ')) .upper() .strip() [0]

print ('Sexo registrado!')
