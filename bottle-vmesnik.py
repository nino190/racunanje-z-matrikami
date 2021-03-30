import sys
from racunanje import Matrika
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
            m = input('Vnesi stevilo vrstic matrike: ')
            n = input('Vnesi stevilo stolpcev matrike: ')
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            a = Matrika(a)
            print (a.Transponiranje())
        if izbira == '2':
            m = input('Vnesi stevilo vrstic matrike: ')
            n = input('Vnesi stevilo stolpcev matrike: ')
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            a = Matrika(a)
            print (a.DeterminantaMatrike())
        if izbira == '3':
            m = input('Vnesi stevilo vrstic matrike: ')
            n = input('Vnesi stevilo stolpcev matrike: ')
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            a = Matrika(a)
            print (a.PrirejenkaMatrike())
        if izbira == '4':
            m = input('Vnesi stevilo vrstic matrike: ')
            n = input('Vnesi stevilo stolpcev matrike: ')
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            a = Matrika(a)
            print (a.InverzMatrike())
        if izbira == '5':
            m = input('Vnesi stevilo vrstic matrike: ')
            n = input('Vnesi stevilo stolpcev matrike: ')
            print('Vnesi elemente matrike: ')
            a = (VhodnaMatrika(m, n))
            a = Matrika(a)
            print('Vnesi vrednost skalarja ')
            skalar = int(input('> '))
            print (a.MnozenjeSSkalarjem(skalar))

