from racunanje import DeterminantaMatrike, kofaktor, PrirejenkaMatrike, InverzMatrike, EnotskiVektor, print_matrix, Matrika, Operacije
from matrika_input import VhodnaMatrika

shranjene = []

def vnesi(ohayo):
    while True:
        stevilo = input(ohayo)
        if stevilo.isdigit():
            return int(stevilo)
        else:
            print ("Prosim vnesite veljavno število!")

def izbira(seznam):
    for indeks, (oznaka, _) in enumerate(seznam, 1):
        print (f'{indeks}) {oznaka}')
    while True:
        izb = vnesi(">>>")
        if 1 <= izb <= len(seznam):
            _, element = seznam[izb - 1]
            return element
        else:
            print(f"Prosim vnesite veljavno število med 1 in {len(seznam)}.")

def glavni_meni():
    while True:
        try:
            dejanja = [
                ("Transponiral matriko", Transponiraj),
                ("Izracunal determinanto matrike", Determinanta),
                ("Izracunal inverz matrike", Inverzna),
                ("Izracunal prirejenko matrike", Prirejenka),
                ("Mnozil matriko s skalarjem", SkalarnoMnozenje),
                ("Sestel matriki", Sestevanje),
                ("Zmnozil matriki", Mnozenje),
                ("Izracunal enotski vektor", Enotski),
                ("Izracunal skalarni produkt", ProduktSkalarni),
                ("Izracunal vektorski produkt", ProduktVektorski),
                ("Pregledal shranjene matrike", Prikaz)
                ]
            print('''
            Pozdravljeni v Matričnem kalkulatorju. Kaj bi radi naredili?
            ''')
            izbor = izbira(dejanja)
            izbor()
        except KeyboardInterrupt:
            print(" Nasvidenje!")
            break

def Transponiraj():
    ime = input('Vnesi ime matrike: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    shranjene.append((ime, Matrika(a)))
    shranjene.append((f"transponirana {ime}", Matrika(a).Transponiranje()))
    print_matrix(Matrika(a).Transponiranje())

def Determinanta():
    ime = input('Vnesi ime matrike: ')    
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    shranjene.append((ime, Matrika(a)))
    shranjene.append((f"determinanta {ime}", DeterminantaMatrike(a)))
    print_matrix(DeterminantaMatrike(a))

def Prirejenka():
    ime = input('Vnesi ime matrike: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    shranjene.append((ime, Matrika(a)))
    shranjene.append((f"prirejenka {ime}", PrirejenkaMatrike(a)))
    print_matrix(PrirejenkaMatrike(a))

def Inverzna():
    ime = input('Vnesi ime matrike: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    shranjene.append((ime, Matrika(a)))
    shranjene.append((f"inverzna {ime}", InverzMatrike(a)))
    print_matrix(InverzMatrike(a))

def SkalarnoMnozenje():
    ime = input('Vnesi ime matrike: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print('Vnesi vrednost skalarja ')
    skalar = int(input('> '))
    shranjene.append((ime, Matrika(a)))
    x = Operacije().MnozenjeSSkalarjem(Matrika(a), skalar)
    shranjene.append((f"{ime} skalarno pomnožena s {skalar}", x))
    print_matrix(Operacije().MnozenjeSSkalarjem(Matrika(a), skalar))

def Sestevanje():
    print('Prva matrika: ')
    ime = input('Vnesi ime prve matrike: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print('Druga matrika: ')
    ime2 = input('Vnesi ime druge matrike: ')
    j = input('Vnesi stevilo vrstic matrike: ')
    k = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    b = VhodnaMatrika(j, k)
    b = b.vhodna
    shranjene.append((ime, Matrika(a)))
    shranjene.append(ime2, Matrika(b))
    x = Operacije().SestevanjeMatrik(Matrika(a), Matrika(b))
    shranjene.append((f"seštevek matrik {ime} in {ime2}", x))
    print_matrix(Operacije().SestevanjeMatrik(Matrika(a), Matrika(b)))

def Mnozenje():
    print('Prva matrika: ')
    ime = input('Vnesi ime prve matrike: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print('Druga matrika: ')
    ime2 = input('Vnesi ime druge matrike: ')
    j = input('Vnesi stevilo vrstic matrike: ')
    k = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    b = VhodnaMatrika(j, k)
    b = b.vhodna
    shranjene.append((ime, Matrika(a)))
    shranjene.append(ime2, Matrika(b))
    x = Operacije().MnozenjeMatrik(Matrika(a), Matrika(b))
    shranjene.append((f"zmnožek matrik {ime} in {ime2}", x))
    print_matrix(x)

def Enotski():
    ime = input('Vnesi ime vektorja: ')
    n = input('Vnesi dimenzijo vektorja: ')
    print('Vnesi elemente vektorja: ')
    a = VhodnaMatrika(1, n)
    a = a.vhodna
    shranjene.append((ime, Matrika(a)))
    shranjene.append((f"enotski vektor za {ime}", EnotskiVektor(Matrika(a))))
    print_matrix(EnotskiVektor(Matrika(a)))

def ProduktSkalarni():
    print('Prvi vektor: ')
    ime = input('Vnesi ime prvega vektorja: ')
    n = input('Vnesi dimenzijo vektorja: ')
    print('Vnesi elemente vektorja: ')
    a = VhodnaMatrika(1, n)
    a = a.vhodna
    print('Drugi vektor: ')
    ime2 = input('Vnesi ime drugega vektorja: ')
    k = input('Vnesi dimenzijo vektorja: ')
    print('Vnesi elemente vektorja: ')
    b = VhodnaMatrika(1, k)
    b = b.vhodna
    shranjene.append((ime, Matrika(a)))
    shranjene.append(ime2, Matrika(b))
    x = Operacije().SkalarniProdukt(Matrika(a), Matrika(b))
    shranjene.append((f"skalarni produkt vektorjev {ime} in {ime2}", x))
    print_matrix(x)

def ProduktVektorski():
    print('Prvi vektor: ')
    ime = input('Vnesi ime prvega vektorja: ')
    print('Vnesi elemente tridimenzionalnega vektorja: ')
    a = VhodnaMatrika(1, 3)
    a = a.vhodna
    print('Drugi vektor: ')
    ime2 = input('Vnesi ime drugega vektorja: ')
    print('Vnesi elemente tridimenzionalnega vektorja: ')
    b = VhodnaMatrika(1, 3)
    b = b.vhodna
    shranjene.append((ime, Matrika(a)))
    shranjene.append(ime2, Matrika(b))
    x = Operacije().VektorskiProdukt(Matrika(a), Matrika(b))
    shranjene.append((f"vektorski produkt {ime} in {ime2}", x))
    print_matrix(x)

def Prikaz(seznam):
    for (oznaka, matrika) in enumerate(seznam, 1):
        print (f'{oznaka}')
        print_matrix(matrika)

glavni_meni()