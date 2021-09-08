from racunanje import *
from tekstovni_vmesnik import *
from matrika_input import *
import bottle
from bottle import route, request

@bottle.get('/')
def meni():
    bottle.redirect('/prva-stran')

#@bottle.post('/prva-stran')
#def generiraj():
    

@bottle.get('/prva-stran')
def prvastran():
    return bottle.template('izgled/prva-stran.html')

@bottle.get('/transponiranje')
def trans():
    return bottle.template('izgled/transponiranje.html')

@route('/transponiranje', method='Post')
def trans2():
    ime_matrike = request.forms.ime
    matrika = request.forms.matrika
    lines = matrika.split(' ')
    matrika = [[int(i) for i in line.split(',')] for line in lines]
    transponirana = Matrika(matrika).Transponiranje()
    ime_transponirane = f"transponirana {ime_matrike}"
    shranjene.append((f"{ime_matrike}", matrika))
    shranjene.append((ime_transponirane, transponirana))
    return str(transponirana)

@bottle.get('/determinanta')
def deter():
    return bottle.template('izgled/determinanta.html')

@route('/determinanta', method='Post')
def trans2():
    ime_matrike = request.forms.ime
    matrika = request.forms.matrika
    lines = matrika.split(' ')
    matrika = [[int(i) for i in line.split(',')] for line in lines]
    determinanta = DeterminantaMatrike(matrika)
    ime_determinante = f"det({ime_matrike})"
    shranjene.append((f"{ime_matrike}", matrika))
    shranjene.append((ime_determinante, determinanta))
    return str(determinanta)

@bottle.get('/inverz')
def inv():
    return bottle.template('izgled/inverz.html')

@route('/inverz', method='Post')
def inv2():
    ime_matrike = request.forms.ime
    matrika = request.forms.matrika
    lines = matrika.split(' ')
    matrika = [[int(i) for i in line.split(',')] for line in lines]
    inverz = InverzMatrike(matrika)
    ime_inverza = f"inverzna {ime_matrike}"
    shranjene.append((f"{ime_matrike}", matrika))
    shranjene.append((ime_inverza, inverz))
    return str(inverz)

@bottle.get('/prirejenka')
def prir():
    return bottle.template('izgled/prirejenka.html')

@bottle.get('/skalarno-mnozenje')
def sk_mn():
    return bottle.template('izgled/mnozenje-s-skalarjem.html')

@route('/skalarno-mnozenje', method='Post')
def sk_mn2():
    ime_matrike = request.forms.ime
    matrika = request.forms.matrika
    skalar = int(request.forms.skalar)
    lines = matrika.split(' ')
    matrika = [[int(i) for i in line.split(',')] for line in lines]
    skalarno = Operacije().MnozenjeSSkalarjem(matrika, skalar)
    ime_nove = f"{ime_matrike} pomnožena s {skalar}"
    shranjene.append((f"{ime_matrike}", matrika))
    shranjene.append((ime_nove, skalarno))
    return str(skalarno)

@bottle.get('/sestevanje')
def ses():
    return bottle.template('izgled/sestevanje.html')

@route('/sestevanje', method='Post')
def ses2():
    ime_matrike1 = request.forms.ime1
    matrika1 = request.forms.matrika1
    ime_matrike2 = request.forms.ime2
    matrika2 = request.forms.matrika2
    lines = matrika1.split(' ')
    matrika = [[int(i) for i in line.split(',')] for line in lines]
    lines2 = matrika2.split(' ')
    matrika2 = [[int(i) for i in line.split(',')] for line in lines2]
    sestevek = Operacije().SestevanjeMatrik(matrika, matrika2)
    ime_nove = f"Seštevek {ime_matrike1} in {ime_matrike2}"
    shranjene.append((f"{ime_matrike1}", matrika1))
    shranjene.append((f"{ime_matrike2}", matrika2))
    shranjene.append((ime_nove, sestevek))
    return str(sestevek)

@bottle.get('/mnozenje')
def mno():
    return bottle.template('izgled/mnozenje.html')

@route('/mnozenje', method='Post')
def ses2():
    ime_matrike1 = request.forms.ime1
    matrika1 = request.forms.matrika1
    ime_matrike2 = request.forms.ime2
    matrika2 = request.forms.matrika2
    lines = matrika1.split(' ')
    matrika = [[int(i) for i in line.split(',')] for line in lines]
    lines2 = matrika2.split(' ')
    matrika2 = [[int(i) for i in line.split(',')] for line in lines2]
    zmnozek = Operacije().MnozenjeMatrik(matrika, matrika2)
    ime_nove = f"Zmnožek {ime_matrike1} in {ime_matrike2}"
    shranjene.append((f"{ime_matrike1}", matrika1))
    shranjene.append((f"{ime_matrike2}", matrika2))
    shranjene.append((ime_nove, zmnozek))
    return str(zmnozek)

@bottle.get('/enotski')
def enotski():
    return bottle.template('izgled/enotski.html')

@route('/enotski', method='Post')
def enotski2():
    ime_vektorja = request.forms.ime
    vektor = request.forms.vektor
    vektor = [int(i) for i in vektor.split(',')]
    enotski = EnotskiVektor(vektor)
    ime_enotskega = f"enotski vektor od {ime_vektorja}"
    shranjene.append((f"{ime_vektorja}", vektor))
    shranjene.append((ime_enotskega, enotski))
    return str(enotski)

@bottle.get('/skalarni')
def sk_pro():
    return bottle.template('izgled/skalarni.html')

@route('/skalarni', method='Post')
def sk_pro2():
    ime_vektorja1 = request.forms.ime1
    vektor1 = request.forms.vektor1
    ime_vektorja2 = request.forms.ime2
    vektor2 = request.forms.vektor2
    vektor1 = [int(i) for i in vektor1.split(',')]
    vektor2 = [int(i) for i in vektor2.split(',')]
    zmnozek = Operacije().SkalarniProdukt(vektor1, vektor2)
    ime_nove = f"Skalarni produkt {ime_vektorja1} in {ime_vektorja2}"
    shranjene.append((f"{ime_vektorja1}", vektor1))
    shranjene.append((f"{ime_vektorja2}", vektor2))
    shranjene.append((ime_nove, zmnozek))
    return str(zmnozek)

@bottle.get('/vektorski')
def vek_pro():
    return bottle.template('izgled/vektorski.html')

@route('/vektorski', method='Post')
def sk_pro2():
    ime_vektorja1 = request.forms.ime1
    vektor1 = request.forms.vektor1
    ime_vektorja2 = request.forms.ime2
    vektor2 = request.forms.vektor2
    vektor1 = [int(i) for i in vektor1.split(',')]
    vektor2 = [int(i) for i in vektor2.split(',')]
    zmnozek = Operacije().VektorskiProdukt(vektor1, vektor2)
    ime_nove = f"Vektorski produkt {ime_vektorja1} in {ime_vektorja2}"
    shranjene.append((f"{ime_vektorja1}", vektor1))
    shranjene.append((f"{ime_vektorja2}", vektor2))
    shranjene.append((ime_nove, zmnozek))
    return str(zmnozek)

@bottle.get('/pregled')
def zgo():
    return bottle.template('izgled/pregled.html')

bottle.run(debug=True, reloader=True)