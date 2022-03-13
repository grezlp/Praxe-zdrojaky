def count(retezec, znak):
    pocet = 0
    for c in retezec:
        if c == znak:
            pocet = pocet + 1
    return pocet

trida_retezcu = type("abc")
print(trida_retezcu(8))
print(trida_retezcu([1,2,3])) #chovají se stejně jako 'str'

class Kotatko:
    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

#kotatko = Kotatko() #vytvoření konkrétního objektu
#kotatko.zamnoukej() #volání metody

mourek = Kotatko()
mourek.jmeno = 'Mourek'

micka = Kotatko()
micka.jmeno = 'Micka'

mourek.zamnoukej()
micka.zamnoukej()

class Kotatko:
    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

    def snez(self, jidlo):
        print(f"{self.jmeno}: Mňau mňau! {jidlo} mi chutná!")

mourek = Kotatko()
mourek.jmeno = 'Mourek'
mourek.snez('ryba')

class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return f'<Kotatko jmenem {self.jmeno}>'

    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

    def snez(self, jidlo):
        print(f"{self.jmeno}: Mňau mňau! {jidlo} mi chutná!")

mourek = Kotatko('Mourek')
micka = Kotatko(jmeno='Micka')
mourek.zamnoukej()
micka.zamnoukej()
mourek.snez('rohlík')

print(mourek)

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")

class Stenatko:
    def __init__(self,jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")

    def zastekej(self):
        print(f"{self.jmeno}: Haf!")

micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.zamnoukej()
azorek.zastekej()
micka.snez('myš')
azorek.snez('kost')

class Kotatko(Zviratko):
    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi vůbec nechutná!")

micka = Kotatko('Micka')
micka.snez('granule')


class Kotatko(Zviratko):
    def snez(self, jidlo):
        print(f"({self.jmeno} na {jidlo} chvíli fascinovaně kouká)")
        super().snez(jidlo)


micka = Kotatko('Micka')
micka.snez('granule')

class Had(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')
        super().__init__(jmeno)


standa = Had('Stanislav')
standa.snez('myš')

zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.snez('flákota')

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")


class Kotatko(Zviratko):
    def udelej_zvuk(self):
        print(f"{self.jmeno}: Mňau!")


class Stenatko(Zviratko):
    def udelej_zvuk(self):
        print(f"{self.jmeno}: Haf!")


zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.udelej_zvuk()
    zviratko.snez('flákota')
