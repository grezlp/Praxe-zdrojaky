pi = 3.1415926 #proměnná může být všude

def obsah_kruhu(polomer):
    return pi * polomer ** 2

print(obsah_kruhu(100))
"""
def nastav_x(hodnota):
    x = hodnota #lokální proměnná

nastav_x(40)
print('x =', x) - zde to skončí chybou, x je jen ve funkci
"""
"""
def zamen(slovo, pozice, novy_znak):
    zacatek = slovo[:pozice]
    konec = slovo[pozice + 1:]
    nove_slovo = zacatek + novy_znak + konec
    return nove_slovo

print(zamen('kočka', 1, 'a'))
print(zamen('kačka', 2, 'p'))

print(zacatek)  - zde to samé
"""

x = 0

def nastav_x(hodnota):
    x = hodnota  # Přiřazení do lokální proměnné!
    print('Ve funkci nastav_x: x =', x)

nastav_x(40)
print('Venku: x =', x)

from math import pi
obsah = 0
a = 30

def obsah_elipsy(a, b):
    obsah = pi * a * b  # Přiřazení do `obsah`
    a = a + 3  # Přiřazení do `a`
    return obsah

print(obsah_elipsy(a, 20))
print(obsah)
print(a)