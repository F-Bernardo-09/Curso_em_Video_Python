pairs = []
odd = []
list = []

while True:
    numbers = int (input ('Write un number: '))
    if numbers not in list:
        list.append(numbers)

    if numbers % 2 == 0 and numbers not in pairs:
        pairs.append(numbers)
    elif numbers % 2 == 1 and numbers not in odd:
        odd.append(numbers)
        odd.sort

    menu = str (input ('Do you want to continue? Yes or No? ')) .strip() .upper()
    if menu in 'Nn':
        break

pairs.sort()
odd.sort()
list.sort()

print ('-='*20)
print (f'The complete lista: {list}')
print (f'The even numbers written were: {pairs}')
print (f'The numbers odd written were: {odd}')
