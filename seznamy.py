cisla = [0,1,2,9,46,69,450]
print(cisla)

for cislo in cisla:
    print(cislo)

seznam = [1, 'abc', True, None, range(10), len]
print(seznam)

print(cisla[3])
print(cisla[2:-3])

prvocisla = [2, 3, 5 ,7, 11, 13, 17]
print(prvocisla)
prvocisla.append(19)
print(prvocisla)

a = [1,2,3]
b = a

print(b)
a.append(4)
print(b)

dalsi_prvocila = [23,29,31]
prvocisla.extend(dalsi_prvocila)
print(prvocisla)

seznam = []
seznam.extend('abcdef')
seznam.extend(range(10))
print(seznam)
seznam.clear()

cisla = [1,0,3,4]
cisla[1] = 2
print(cisla)

cisla = [1,2,3,4]
cisla[1:-1] = [6,5]
print(cisla)

cisla = [1, 2, 3, 4]
cisla[1:-1] = [0, 0, 0, 0, 0, 0]
print(cisla)
cisla[1:-1] = []
print(cisla)

cisla = [1,2,3,4,5,6]
del cisla[-1]
print(cisla)
del cisla[3:5]
print(cisla)

cisla = [1, 2, 3, 'abc', 4, 5, 6, 12]
posledni = cisla.pop()
print(posledni)
print(cisla)

cisla.remove('abc')
print(cisla)

cisla.clear()
print(cisla)

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort()
print(seznam)

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort(reverse=True)
print(seznam)

melodie = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
print(melodie)

print("D" in melodie)

if seznam:
    print('V seznamu něco je!')
else:
    print('Seznam je prázdný!')

abeceda = list('abcdefghijklmnopqrstuvwxyz')
cisla = list(range(100))
print(abeceda)
print(cisla)

a = [1, 2, 3]
b = list(a)

print(b)
a.append(4)
print(b)

mocniny_dvou = []
for cislo in range(10):
    mocniny_dvou.append(2 ** cislo)
print(mocniny_dvou)

balicek = []
for barva in '♠', '♥', '♦', '♣':  # (Na Windows použij textová jména)
    for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        balicek.append(str(hodnota) + barva)
print(balicek)

slova = 'Tato věta je složitá, rozdělme ji na slova!'.split()
print(slova)

veta = ' '.join(slova)
print(veta)

def vyber_chybne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if jmeno[0].islower() or prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

def vyber_spravne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if not jmeno[0].islower() and not prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

def oprav_zaznamy(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        vysledek.append(jmeno.capitalize() + ' ' + prijmeni.capitalize())
    return vysledek

zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

chybne_zaznamy = vyber_chybne(zaznamy)
print(chybne_zaznamy) # → ['pepa novák', 'Ivo navrátil', 'jan Poledník']

spravne_zaznamy = vyber_spravne(zaznamy)
print(spravne_zaznamy) # → ['Jiří Sládek']

opravene_zaznamy = oprav_zaznamy(zaznamy)
print(opravene_zaznamy) # → ['Pepa Novák', 'Jiří Sládek', 'Ivo Navrátil', 'Jan Poledník']
import random

balicek = []
for barva in '♠', '♥', '♦', '♣':
    for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        balicek.append(str(hodnota) + barva)
print(balicek)

random.shuffle(balicek)
print(balicek)

mozne_tahy = ['kámen', 'nůžky', 'papír']
tah_pocitace = random.choice(mozne_tahy)
print(tah_pocitace)

seznam_seznamu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
prvni_seznam = seznam_seznamu[0]
print(prvni_seznam)

prvni_prvek_druheho_seznamu = seznam_seznamu[1][0]
print(prvni_prvek_druheho_seznamu)

def vytvor_tabulku(velikost=11):
    seznam_radku = []
    for a in range(velikost):
        radek = []
        for b in range(velikost):
            radek.append(a * b)
        seznam_radku.append(radek)
    return seznam_radku

nasobilka = vytvor_tabulku()

print(nasobilka[2][3])  # dva krát tři
print(nasobilka[5][2])  # pět krát dva
print(nasobilka[8][7])  # osm krát sedm

# Vypsání celé tabulky
for radek in nasobilka:
    for cislo in radek:
        print(cislo, end=' ')
    print()