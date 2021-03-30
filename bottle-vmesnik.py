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
        elif izbira == '2':
            m = input('Vnesi stevilo vrstic matrike: ')
            n = input('Vnesi stevilo stolpcev matrike: ')
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            a = Matrika(a)
            print (a.DeterminantaMatrike())
        elif izbira == '3':
            m = input('Vnesi stevilo vrstic matrike: ')
            n = input('Vnesi stevilo stolpcev matrike: ')
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            a = Matrika(a)
            print (a.PrirejenkaMatrike())
        elif izbira == '4':
            m = input('Vnesi stevilo vrstic matrike: ')
            n = input('Vnesi stevilo stolpcev matrike: ')
            print('Vnesi elemente matrike: ')
            a = VhodnaMatrika(m, n)
            a = Matrika(a)
            print (a.InverzMatrike())
        elif izbira == '5':
            m = input('Vnesi stevilo vrstic matrike: ')
            n = input('Vnesi stevilo stolpcev matrike: ')
            print('Vnesi elemente matrike: ')
            a = (VhodnaMatrika(m, n))
            a = Matrika(a)
            print('Vnesi vrednost skalarja ')
            skalar = int(input('> '))
            print (a.MnozenjeSSkalarjem(skalar))
        elif izbira == '6':
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
        elif izbira == '7':
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
        elif izbira == '8':
            n = input('Vnesi dimenzijo vektorja: ')
            print('Vnesi elemente vektorja: ')
            a = (VhodnaMatrika(1, n))
            a = Matrika(a)
            print (a.EnotskiVektor)
        elif izbira == '9':
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
        elif izbira == '10':
            print('Prvi vektor: ')
            print('Vnesi elemente tridimenzionalnega vektorja: ')
            a = VhodnaMatrika(1, 3)
            a = Matrika(a)
            print('Drugi vektor: ')
            print('Vnesi elemente tridimenzionalnega vektorja: ')
            b = VhodnaMatrika(1, 3)
            b = Matrika(b)
            print (b.VektorskiProdukt())
        elif izbira == '11':
            break

