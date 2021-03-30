import sys
from racunanje import Matrika
from matrika_input import VhodnaMatrika
from bottle import route, run, request


def glavni_meni():
    while True:
        print('''
        Pozdravljeni v Matričnem kalkulatorju. Kaj bi radi naredili?
        1) Transponiral matriko
        2) Izracunal determinanto matrike
        3) Izracunal prirejenko matrike
        4) Izracunal inverz matrike
        5) Mnozil matriko s skalarjem
        6) Sestel matriki
        7) Zmnozil matriki
        8) Izracunal enotski vektor
        9) Izracunal skalarni produkt
        10) Izracunal vektorski produkt
        11) Zapustil aplikacijo
        ''')
        izbira = input('>')
        if izbira == '1':
            Transponiraj()
        elif izbira == '2':
            Determinanta()
        elif izbira == '3':
            Prirejenka()
        elif izbira == '4':
            Inverzna()
        elif izbira == '5':
            SkalarnoMnozenje()
        elif izbira == '6':
            Sestevanje()
        elif izbira == '7':
            Mnozenje()
        elif izbira == '8':
            Enotski()
        elif izbira == '9':
            ProduktSkalarni()
        elif izbira == '10':
            ProduktVektorski()
        elif izbira == '11':
            print ('Nasvidenje.')
            break
        else:
            print ('Neveljavna izbira')

def Transponiraj():
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = Matrika(a)
    print (a.Transponiranje())

def Determinanta():
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = Matrika(a)
    print (a.DeterminantaMatrike())

def Prirejenka():
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = Matrika(a)
    print (a.PrirejenkaMatrike())

def Inverzna():
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = Matrika(a)
    print (a.InverzMatrike())

def SkalarnoMnozenje():
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = (VhodnaMatrika(m, n))
    a = Matrika(a)
    print('Vnesi vrednost skalarja ')
    skalar = int(input('> '))
    print (a.MnozenjeSSkalarjem(skalar))

def Sestevanje():
    print('Prva matrika: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = Matrika(a)
    print('Druga matrika: ')
    j = input('Vnesi stevilo vrstic matrike: ')
    k = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    b = VhodnaMatrika(j, k)
    b = Matrika(b)
    print (b.SestevanjeMatrik())

def Mnozenje():
    print('Prva matrika: ')
    m = input('Vnesi stevilo vrstic matrike: ')
    n = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    a = VhodnaMatrika(m, n)
    a = Matrika(a)
    print('Druga matrika: ')
    j = input('Vnesi stevilo vrstic matrike: ')
    k = input('Vnesi stevilo stolpcev matrike: ')
    print('Vnesi elemente matrike: ')
    b = VhodnaMatrika(j, k)
    b = Matrika(b)
    print (b.MnozenjeMatrik())

def Enotski():
    n = input('Vnesi dimenzijo vektorja: ')
    print('Vnesi elemente vektorja: ')
    a = (VhodnaMatrika(1, n))
    a = Matrika(a)
    print (a.EnotskiVektor)

def ProduktSkalarni():
    print('Prvi vektor: ')
    n = input('Vnesi dimenzijo vektorja: ')
    print('Vnesi elemente vektorja: ')
    a = VhodnaMatrika(1, n)
    a = Matrika(a)
    print('Drugi vektor: ')
    k = input('Vnesi dimenzijo vektorja: ')
    print('Vnesi elemente vektorja: ')
    b = VhodnaMatrika(1, k)
    b = Matrika(b)
    print (b.SkalarniProdukt())

def ProduktVektorski():
    print('Prvi vektor: ')
    print('Vnesi elemente tridimenzionalnega vektorja: ')
    a = VhodnaMatrika(1, 3)
    a = Matrika(a)
    print('Drugi vektor: ')
    print('Vnesi elemente tridimenzionalnega vektorja: ')
    b = VhodnaMatrika(1, 3)
    b = Matrika(b)
    print (b.VektorskiProdukt())

