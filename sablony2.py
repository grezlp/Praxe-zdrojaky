sablona = 'Ahoj {jmeno}! Tvoje číslo je {cislo}.'
print(sablona.format(cislo=7, jmeno='Hynku'))
print(sablona.format(cislo=42, jmeno='Viléme'))
print(sablona.format(cislo=3, jmeno='Jarmilo'))

vypis = '{} krát {} je {}'.format(3, 4, 3*4)
print(vypis)