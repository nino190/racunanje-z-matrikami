class Matrika:

    def __init__(self, matrika):
        self.matrika = matrika
    
    def dim(self, dimenzija):
        if dimenzija == "vrs":
            return len(self.matrika)
        elif dimenzija == "sto":
            return len(self.matrika[0])
    
    def vrstica(self, vrs):
        return self.matrika[vrs-1]
    
    def stolpec(self, sto):
        x = []
        for i in self.matrika:
            x.append(i[sto-1])
        return x
    
    def dodaj_vrstico(self, vrs):
        self.matrika.append(vrs)

    def dodaj_stolpec(self, sto):
        x = 0
        for i in self.matrika:
            i.append(sto[x])
            x += 1
    
    def zbrisi_vrstico(self, vrs):
        m = self.matrika
        del m[vrs-1]
        return m

    def zbrisi_stolpec(self, sto):
        m = self.matrika
        for i in m:
            del i[sto-1]
        return m

    def element(self, vrs, sto):
        return int(Matrika(self.matrika).vrstica(vrs)[sto-1])

    def KopijaMatrike(self):
        kopija = []
        for i in range(len(self.matrika)):
            kopija.append(self.matrika[i])
        return kopija
        
    def Transponiranje(self):
        transponirana = []
        for i in range(1, Matrika(self.matrika).dim("sto") + 1):
            transponirana.append(Matrika(self.matrika).stolpec(i))
        return transponirana

def DeterminantaMatrike(a):

    indeksi = list(range(Matrika(a).dim("vrs")))
    
    determinanta = 0
    
    if Matrika(a).dim("vrs") == Matrika(a).dim("sto"):
        if Matrika(a).dim("vrs") == 2:
            mala = Matrika(a).element(1, 1) * Matrika(a).element(2, 2) - Matrika(a).element(2, 1) * Matrika(a).element(1, 2)
            return mala

        for i in indeksi:
            minor = Matrika(a).KopijaMatrike()
            minor.zbrisi_vrstico(1)
            SteviloVrstic = len(minor)
    
            for j in range(SteviloVrstic): 
                minor[j] = minor[j][0:i] + minor[j][i + 1:]
    
            kofaktor = (-1) ** (i % 2) * minor.DeterminantaMatrike()
            determinanta += a[0][i] * kofaktor
        return determinanta
    else:
        raise ArithmeticError("Determinanta ne obstaja ker matrika ni kvadratna")

def kofaktor(a, vrs, sto):

    kofaktor = 0
    a = Matrika(a).KopijaMatrike()
    a.zbrisi_vrstico(vrs)
    a.zbrisi_stolpec(sto)
    kofaktor = Matrika(a).DeterminantaMatrike
    return kofaktor

def PrirejenkaMatrike(a):

    if Matrika(a).dim("vrs") != Matrika(a).dim("sto"):
            raise ArithmeticError("Prirejenka ne obstaja")
            
    else:
        prirejenka = []
        b = Matrika(a).KopijaMatrike()

        for i in range (Matrika(a).dim("vrs")):
            vrstica = []
            for j in range (Matrika(a).dim("sto")):
                vrstica.append(b.kofaktor(i, j))
            prirejenka.append(vrstica)
            
        prirejenka = Matrika(prirejenka)
        prirejenka.Transponiranje()
        return prirejenka

def InverzMatrike(a):

    if Matrika(a).dim("vrs") != Matrika(a).dim("sto"):
        raise ArithmeticError("Matrika ni kvadratna zato nima inverza.")

    if Matrika(a).DeterminantaMatrike == 0:
        raise ZeroDivisionError("Determinanta matrike je enaka 0 zato matrika nima inverza")
            
    InverznaMatrika = PrirejenkaMatrike(a) / (DeterminantaMatrike(a))
    InverznaMatrika = Matrika(InverznaMatrika)
    return InverznaMatrika

def EnotskiVektor(a):

    if  Matrika(a).dim("vrs") > 1 and Matrika(a).dim("sto") > 1:
        raise ArithmeticError("Vektor mora biti ali ena vrstica ali en stolpec")
    
    norma = 0
    for i in range(Matrika(a).dim("vrs")):
        for j in range(Matrika(a).dim("sto")):
            norma += Matrika(a).element(i, j) ** 2
    
    norma = norma ** 0.5
    EnotskiVektor = Matrika(a).KopijaMatrike()

    for i in range (Matrika(a).dim("vrs")):
        for j in range (Matrika(a).dim("sto")):
            EnotskiVektor[i][j] = EnotskiVektor[i][j] / norma
        
    return EnotskiVektor

#########################################################################################
#########################################################################################
#########################################################################################

class Operacije():

    def MnozenjeSSkalarjem(self, a, skalar):

        return [[element * skalar for element in vrstica] for vrstica in a]


    def SestevanjeMatrik(self, a, b):
        assert Matrika(a).dim("vrs") == Matrika(b).dim("vrs") and Matrika(a).dim("sto") == Matrika(b).dim("sto")
        sestevek = []
        for vrs_a, vrs_b in zip(a, b):
            sestevek.append([x + y for x, y in zip(vrs_a, vrs_b)])
        return sestevek

    def MnozenjeMatrik(self, a, b):
        zmnozek = []

        if Matrika(a).dim("vrs") == Matrika(b).dim("sto"):
            for i in range (Matrika(a).dim("vrs")):
                vrstica = []
                for j in range (Matrika(b).dim("sto")):
                    x = 0
                    for k in range (Matrika(a).dim("vrs")):
                        x += a[i][k] * b[k][j]
                    vrstica.append(x)
                zmnozek.append(vrstica)
            return zmnozek
        else:
            raise ArithmeticError("Matriki ni mogoce zmnoziti." )
        


    def SkalarniProdukt(self, v1, v2):

        v1 = Matrika(v1)
        v2 = Matrika(v2)

        if (v1.dim("vrs") > 1 and v1.dim("sto") > 1) or (v2.dim("vrs") > 1 and v2.dim("sto") > 1):
            raise ArithmeticError("Vektor mora biti ali ena vrstica ali en stolpec")

        skalarni = 0

        if v1.dim("vrs") == 1 and v2.dim("vrs") == 1 and v1.dim("sto") == v2.dim("sto"):
            for i in range (v1.dim("sto")):
                skalarni += v1[0][i] * v2[0][i]
        
        elif v1.dim("vrs") == 1 and v2.dim("sto") == 1 and v1.dim("sto") == v2.dim("vrs"):
            v2 = v2.Transponiranje()
            for i in range (v1.dim("sto")):
                skalarni += v1[0][i] * v2[i][0]

        elif v1.dim("sto") == 1 and v2.dim("vrs") == 1 and v1.dim("vrs") == v2.dim("sto"):
            v1 = v1.Transponiranje()
            v1 = Matrika(v1)
            for i in range (v1.dim("sto")):
                skalarni += v1[i][0] * v2[0][i] 

        elif v1.dim("sto") == 1 and v2.dim("sto") == 1 and v1.dim("vrs") == v2.dim("vrs"):
            v1 = Matrika(v1.Transponiranje())
            v2 = v2.Transponiranje()
            for i in range (v1.dim("sto")):
                skalarni += v1[i][0] * v2[i][0] 
        return skalarni

    def VektorskiProdukt(self, vektor1, vektor2):

        v1 = Matrika(vektor1).dim("vrs")
        s1 = Matrika(vektor1).dim("sto")
        v2 = Matrika(vektor2).dim("vrs")
        s2 = Matrika(vektor2).dim("sto")
        koeficienti = []
        produkt = [] 
        prvi = 0
        drugi = 0
        tretji = 0

        if ((v1 == 1 and s1 == 3) or (s1 == 1 and v1 == 3)) and ((v2 == 1 and s2 == 3) or (s2 == 1 and v2 == 3)):
            
            if v1 == 1 and v2 == 1:
                pass

            elif v1 == 1 and v2 == 3:
                vektor2 = Matrika(vektor2).Transponiranje()
            
            elif v1 == 3 and v2 == 1:
                vektor1 = Matrika(vektor1).Transponiranje()
            
            elif v1 == 3 and v2 == 3:
                vektor1 = Matrika(vektor1).Transponiranje()
                vektor2 = Matrika(vektor2).Transponiranje()
                
            prvi = vektor1[0][1] * vektor2[0][2] - vektor1[0][2] * vektor2[0][1]
            drugi = vektor1[0][2] * vektor2[0][0] - vektor1[0][0] * vektor2[0][2]
            tretji = vektor1[0][0] * vektor2[0][1] - vektor1[0][1] * vektor2[0][0]
            
            koeficienti.append(prvi)
            koeficienti.append(drugi)
            koeficienti.append(tretji)
            produkt.append(koeficienti)
            return produkt

def print_matrix(a):
    
    vrstice = Matrika(a).dim("vrs")
    for i in range(vrstice):
        print(Matrika(a).vrstica(i+1))