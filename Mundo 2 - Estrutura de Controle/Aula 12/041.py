# Distribuição de categorias de natação com base na idade:
from datetime import date
ano = int (input ('Em que ano você nasceu? '))

actual = date.today().year
result = actual - ano

if result < 9:
    print ('MIRIM')
elif 9 <= result < 14:
    print ('INFANTIL')
elif 14 <= result < 19:
    print ('JUNIOR')
elif result == 17 and 18:
    print ('JUNIOR')
elif result >= 19 and 20 == result:
    print ('SÊNIOR')
elif result > 20:
    print ('MASTER')
