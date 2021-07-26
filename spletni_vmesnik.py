from racunanje import DeterminantaMatrike, kofaktor, PrirejenkaMatrike, InverzMatrike, EnotskiVektor, print_matrix, Matrika, Operacije
from matrika_input import VhodnaMatrika
from bottle import route, run, request
from tekstovni_vmesnik import Prikaz, shranjene, Transponiraj, Determinanta, Inverzna, Prirejenka, SkalarnoMnozenje, Sestevanje, Mnozenje, Enotski, ProduktSkalarni, ProduktVektorski, Prikaz
import bottle

@bottle.get('/')
def meni():
    return bottle.template('prva-stran.html')

@bottle.get('/transponiranje/')
def trans():
    return bottle.template('transponiranje.html')

@bottle.post('/transponiranje/')
def trans2():
    Transponiraj()

@bottle.get('/determinanta/')
def deter():
    return bottle.template('determinanta.html')

@bottle.post('/determinanta/')
def deter2():
    Determinanta()

@bottle.get('/inverz/')
def inv():
    return bottle.template('inverz.html')

@bottle.post('/inverz/')
def inv2():
    Inverzna()

@bottle.get('/prirejenka/')
def prir():
    return bottle.template('prirejenka.html')

@bottle.post('/prirejenka/')
def prir2():
    Prirejenka()

@bottle.get('/skalarno-mnozenje/')
def sk_mn():
    return bottle.template('skalarno-mnozenje.html')

@bottle.post('/skalarno-mnozenje/')
def sk_mn2():
    SkalarnoMnozenje()

@bottle.get('/sestevanje/')
def ses():
    return bottle.template('sestevanje.html')

@bottle.post('/sestevanje/')
def ses2():
    Sestevanje()

@bottle.get('/mnozenje/')
def mno():
    return bottle.template('mnozenje.html')

@bottle.post('/mnozenje/')
def mno2():
    Mnozenje()

@bottle.get('/enotski/')
def enotski():
    return bottle.template('enotski.html')

@bottle.post('/enotski/')
def enotski2():
    Enotski()

@bottle.get('/skalarni-produkt/')
def sk_pro():
    return bottle.template('skalarni.html')

@bottle.post('/skalarni-produkt/')
def sk_pro2():
    ProduktSkalarni()

@bottle.get('/vektorski-produkt/')
def vek_pro():
    return bottle.template('vektorski.html')

@bottle.post('/vektorski-produkt/')
def vek_pro2():
    ProduktVektorski()

@bottle.get('/zgodovina/')
def zgo():
    return bottle.template('pregled.html')

@bottle.post('/zgodovina/')
def zgo2():
    Prikaz(shranjene)