def zamen(slovo, pozice, novy_znak):
    """V daném slově zamění znak na dané pozici za daný nový znak."""
    zacatek = slovo[:pozice]
    konec = slovo[pozice+1:]
    nove_slovo = zacatek + novy_znak + konec
    return nove_slovo

print(zamen('kočka', 1, 'a'))
print(zamen('kačka', 2, 'p'))

def napis_hlasku(nazev, skore):
    """Popíše skóre. Název má být přivlastňovací přídavné jméno."""

    print(nazev, 'skóre je', skore)
    if skore > 1000:
        print('Světový rekord!')
    elif skore > 100:
        print('Skvělé!')
    elif skore > 10:
        print('Ucházející.')
    elif skore > 1:
        print('Aspoň něco')
    else:
        print('Snad příště.')

napis_hlasku('Tvoje', 1220)
napis_hlasku('Protivníkovo', 15)

def obsah(a, b):
    S = a*b
    return S

a2 = int(input('Zadej číslo: '))
b2 = int(input('Zadej číslo: '))
print('Obsah trojůhelníka je: ',obsah(a2, b2), 'cm2')

def ano_nebo_ne(otazka):
    """Vrátí True nebo False podle odpovědi uživatele"""
    while True:
        odpoved = input(otazka)
        if odpoved == 'ano':
            return True
        elif odpoved == 'ne':
            return False

        print('Nerozumím! Odpověz "ano" nebo "ne".')

# Příklad použití
if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')

from math import pi

def obsah_elipsy(a, b):
    print('Obsah je', pi * a * b)  # Pozor, `print` místo `return`!

obsah_elipsy(3, 5)   