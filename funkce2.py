from math import sin, cos, tan, degrees, radians
from math import sqrt, floor, ceil
from random import randrange, uniform

print(1, 'dvě', False)
print(1, end=' ')
print(2, 3, 4, sep=', ')

#input('zadej vstup: ')

3 == int('3') == int(3.0) == int(3.141) == int(3)
8.12 == float('8.12') == float(8.12)
8.0 == float(8) == float('8') == float(8.0)
'3' == str(3) == str('3')
'3.141' == str(3.141) == str('3.141')

#int('blablabla')    # chyba!
#float('blablabla')  # chyba!
#int('8.9')          # chyba!

cislo = int(input('Zadej číslo: '))

cislo2 = 16
cislo3 = sqrt(cislo2) #2. odmocnina
print(cislo3)

cislo2 = 16.7
cislo3 = floor(cislo2) #zaokrouhleni dolu
print(cislo3)

cislo2 = 16.3
cislo3 = ceil(cislo2) #zaoukrouhleni nahoru
print(cislo3)

uhel = 2

sin(uhel)
cos(uhel)
tan(uhel)

degrees(uhel) #převod z radiánů na stupně
radians(uhel) #převod ze stupňů na radiány

a = 1
b = 4

randrange(a, b)   # náhodné celé číslo od a do b-1
uniform(a, b)     # náhodné reálné číslo od a do b

cislo = randrange(0, 3)  # číslo je 0, 1, nebo 2
if cislo == 0:
    print('Kolečko')
elif cislo == 1:
    print('Čtvereček')
else:  # tady musí být číslo 2
    print('Trojúhelníček')

