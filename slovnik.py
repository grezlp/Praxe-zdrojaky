cisla = {
    'Maruška': '153 85283',
    'Terka': '237 26505',
    'Renata': '385 11223',
    'Michal': '491 88047',
}

barvy = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}
print(barvy['jablko'])

popisy_funkci = {'len' : 'délka', 'str' : 'řetězec', 'dict' : 'slovník'}
for klic in popisy_funkci:
    print(klic) 

for hodnota in popisy_funkci.values():
    print(hodnota)

for klic, hodnota in popisy_funkci.items():
    print('{}:{}'.format(klic, hodnota))

for klice in popisy_funkci.keys():
    print(klice)
print(" ")

barvy_po_tydnu = dict(barvy)
for klic in barvy_po_tydnu:
    barvy_po_tydnu[klic] = 'černo-hnědo-' + barvy_po_tydnu[klic]
print(barvy['jablko'])
print(barvy_po_tydnu['jablko'])
print(" ")

data = [(1, 'jedna'), (2, 'dva'), (3, 'tři')]
nazvy_cisel = dict(data)

popisy_funkci = dict(len='délka', str='řetězec', dict='slovník')
print(popisy_funkci['len'])