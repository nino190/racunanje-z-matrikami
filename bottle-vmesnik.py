import sys
from racunanje import Matrika, Operacije
from matrika_input import VhodnaMatrika
from bottle import route, run, request


def glavn_meni():
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
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            a = Matrika(a)
            print (a.Transponiranje())
        if izbira == '2':
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            print (a.DeterminantaMatrike())
        if izbira == '3':
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            print (a.PrirejenkaMatrike())
        if izbira == '4':
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            print (a.InverzMatrike())
        if izbira == '5':
            print('Vnesi elemente prve matrike: ')
            a = (VhodnaMatrika(m, n))
            print('Vnesi vrednost skalarja ')
            skalar = input('> ')
            print (MnozenjeSSkalarjem(a, skalar))

