"""odpoved = input('Řekni Ááá! ')
while odpoved != 'Ááá!':
    print('Špatně, zkus to znovu')
    odpoved = input('Řekni Ááá! ')

from random import randrange

while True:
    print('Číslo je', randrange(10000))
    print('(Počkej, než se počítač unaví...)')


while True:
    odpoved = input('Řekni Ááá! ')
    if odpoved == 'Ááá':
        print('Béé')
        break
    print('Špatně, zkus to znovu')

print('Hotovo, ani to nebolelo.')

for i in range(10):  # Vnější cyklus
    for j in range(10):  # Vnitřní cyklus
        print(j * i, end=' ')
        if i <= j:
            break
    print()


from random import randrange, uniform

body = 0
odpoved = 'ano'
while odpoved == 'ano':
    body = body + round(uniform(2,10))
    if body > 21:
        print("Prohráli jste (",body,")")
        odpoved = 'ne'
    else:
        print(body)
        odpoved = input("Chcete pokračovat? ")
"""
celkem = 0

delka_trasy = 8
print('Jdu', delka_trasy, 'km do další vesnice.')
celkem = celkem + delka_trasy

delka_trasy = 45
print('Jdu', delka_trasy, 'km do další vesnice.')
celkem = celkem + delka_trasy

delka_trasy = 9
print('Jdu', delka_trasy, 'km do další vesnice.')
celkem = celkem + delka_trasy

delka_trasy = 21
print('Jdu', delka_trasy, 'km do další vesnice.')
celkem = celkem + delka_trasy

print('Celkem jsem ušla', celkem, 'km')

    

