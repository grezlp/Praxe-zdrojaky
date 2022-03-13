slovo = input('Slovo: ')
pozice = int(input('Které písmeno zaměnit (od nuly)? '))
novy_znak = input('Nové písmeno: ')

zacatek_slova = slovo[:pozice]
konec_slova = slovo[pozice + 1:]
nove_slovo = zacatek_slova + novy_znak + konec_slova

print(nove_slovo)