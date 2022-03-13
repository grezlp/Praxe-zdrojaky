"""strana = float(input('Zadej stranu čtverce v centimetrech: '))
pravda = strana > 0
if pravda:
    print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
    print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
else:
    print("Strana musí být kladná, jinak z toho nebude čtverec!")

print("Děkujeme za použití geometrické kalkulačky.")

"""

"""cislo = int(input('Zadej číslo, přičtu k němu 3: '))
if cislo == 0:
    print('Jé, to je jednoduché!')
print(cislo, '+ 3 =', cislo + 3)

"""

"""vek = int(input('Kolik ti je let? '))
if vek >= 150:
    print('Tak ale jebe ti?')
elif vek >= 18:
    # Tahle větev se např. pro "200" už neprovede.
    print('Můžeme nabídnout: pivo, rum, nebo vodku.')
elif vek >= 1:
    print('Můžeme nabídnout: mléko, čaj, nebo vodu')
elif vek >= 0:
    print('Sunar už bohužel došel LMAO.')
else:
    # Nenastala ani nedna ze situací výše – muselo to být záporné
    print('Pro návštěvy z budoucnosti bohužel nemáme nic v nabídce.')

"""

"""stastna = input('Jsi šťastná?')
bohata = input('Jsi bohatá?')

if stastna == 'ano':
    # Tenhle kus kódu se provede, když je "šťastná"
    if bohata == 'ano':
        print('Gratuluji!')
    else:
        print('Zkus míň utrácet.')
else:
    # Tenhle kus kódu se provede, když není "šťastná"
    if bohata == 'ano':
        print('Zkus se víc usmívat!')
    else:
        print('To je mi líto.')

"""

"""a = float(input("Zadej první stranu obdélníka: "))
b = float(input("Zadej druhou stranu obdélníka: "))

if a <= 0 or b <= 0:
    print("Délka nemůže být záporná!")

"""

print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano' or stastna_retezec == 'Ano':
    stastna = True
elif stastna_retezec == 'ne' or stastna_retezec == 'Ne':
    stastna = False
else:
    print('Nerozumím!')

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano' or bohata_retezec == 'Ano':
    bohata = True
elif bohata_retezec == 'ne' or bohata_retezec == 'Ne':
    bohata = False
else:
    print('Nerozumím!')

if bohata and stastna:
    # Je bohatá a zároveň štǎstná, ta se má.
    print('Gratuluji!')
elif bohata:
    # Je bohatá, ale není „bohatá a zároveň šťastná“,
    # takže musí být jen bohatá.
    print('Zkus se víc usmívat.')
elif stastna:
    # Tady musí být jen šťastná.
    print('Zkus míň utrácet.')
else:
    # A tady víme, že není ani šťastná, ani bohatá.
    print('To je mi líto.')