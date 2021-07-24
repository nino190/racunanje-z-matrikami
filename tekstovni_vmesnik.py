import sys
from racunanje import DeterminantaMatrike, kofaktor, PrirejenkaMatrike, InverzMatrike, EnotskiVektor, print_matrix, Matrika, Operacije
from matrika_input import VhodnaMatrika
from bottle import route, run, request

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
                ("Izracunal prirejenko matrike", Prirejenka),
                ("Izracunal inverz matrike", Inverzna),
                ("Mnozil matriko s skalarjem", SkalarnoMnozenje),
                ("Sestel matriki", Sestevanje),
                ("Zmnozil matriki", Mnozenje),
                ("Izracunal enotski vektor", Enotski),
                ("Izracunal skalarni produkt", ProduktSkalarni),
                ("Izracunal vektorski produkt", ProduktVektorski)
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
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print_matrix(Matrika(a).Transponiranje())

def Determinanta():
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print_matrix(DeterminantaMatrike(a))

def Prirejenka():
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print_matrix(PrirejenkaMatrike(a))

def Inverzna():
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print_matrix(InverzMatrike(a))

def SkalarnoMnozenje():
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print('Vnesi vrednost skalarja ')
    skalar = int(input('> '))
    print_matrix(Operacije().MnozenjeSSkalarjem(Matrika(a), skalar))

def Sestevanje():
    print('Prva matrika: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print('Druga matrika: ')
    j = input('Vnesi stevilo vrstic matrike: ')
    k = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    b = VhodnaMatrika(j, k)
    b = b.vhodna
    print_matrix(Operacije.SestevanjeMatrik(Matrika(a), Matrika(b)))

def Mnozenje():
    print('Prva matrika: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = a.vhodna
    print('Druga matrika: ')
    j = input('Vnesi stevilo vrstic matrike: ')
    k = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    b = VhodnaMatrika(j, k)
    b = b.vhodna
    print_matrix(Operacije.MnozenjeMatrik(Matrika(a), Matrika(b)))

def Enotski():
    n = input('Vnesi dimenzijo vektorja: ')
    print('Vnesi elemente vektorja: ')
    a = VhodnaMatrika(1, n)
    a = a.vhodna
    print_matrix(EnotskiVektor(Matrika(a)))

def ProduktSkalarni():
    print('Prvi vektor: ')
    n = input('Vnesi dimenzijo vektorja: ')
    print('Vnesi elemente vektorja: ')
    a = VhodnaMatrika(1, n)
    a = a.vhodna
    print('Drugi vektor: ')
    k = input('Vnesi dimenzijo vektorja: ')
    print('Vnesi elemente vektorja: ')
    b = VhodnaMatrika(1, k)
    b = b.vhodna
    print_matrix(Operacije().SkalarniProdukt(Matrika(a), Matrika(b)))

def ProduktVektorski():
    print('Prvi vektor: ')
    print('Vnesi elemente tridimenzionalnega vektorja: ')
    a = VhodnaMatrika(1, 3)
    a = a.vhodna
    print('Drugi vektor: ')
    print('Vnesi elemente tridimenzionalnega vektorja: ')
    b = VhodnaMatrika(1, 3)
    b = b.vhodna
    print_matrix(Operacije.VektorskiProdukt(Matrika(a), Matrika(b)))

glavni_meni()