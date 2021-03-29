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
        return Matrika(self.matrika).vrstica(vrs)[sto-1]

    def KopijaMatrike(self):
        kopija = []
        for i in range(len(self.matrika)):
            kopija.append(self.matrika[i])
        return kopija

    def SledMatrike(self):
        sled = 0
        for i in range(len(self.matrika)):
            sled += self.matrika[i][i]
        return sled
        
    def Transponiranje(self):
        transponirana = []
        for i in range(1, Matrika(self.matrika).dim("sto") + 1):
            transponirana.append(Matrika(self.matrika).stolpec(i))
        return transponirana

    def DeterminantaMatrike(self, determinanta = 0):

        indeksi = list(range(self.matrika.dim("vrs")))

        if self.matrika.dim("vrs") == self.matrika.dim("sto"):
            if self.matrika.dim("vrs") == 2:
                mala = self.matrika.element(1, 1) * self.matrika.element(2, 2) - self.matrika.element(2, 1) * self.matrika.element(1, 2)
                return mala

            for i in indeksi:
                minor = self.matrika.KopijaMatrike()
                minor.zbrisi_vrstico(1)
                SteviloVrstic = len(minor)
        
                for j in range(SteviloVrstic): 
                    minor[j] = minor[j][0:i] + minor[j][i + 1:]
        
                kofaktor = (-1) ** (i % 2) * minor.DeterminantaMatrike()
                determinanta += self.matrika[0][i] * kofaktor
            return determinanta
        else:
            raise ArithmeticError("Determinanta ne obstaja ker matrika ni kvadratna")

    def kofaktor(self, vrs, sto):

        kofaktor = 0
        a = self.matrika.KopijaMatrike()
        a.zbrisi_vrstico(vrs)
        a.zbrisi_stolpec(sto)
        kofaktor = a.DeterminantaMatrike
        return kofaktor

    def PrirejenkaMatrike(self):

        if self.matrika.dim("vrs") != self.matrika.dim("sto"):
                raise ArithmeticError("Prirejenka ne obstaja")
                
        else:
            prirejenka = []
            a = self.matrika.KopijaMatrike()

            for i in range (self.matrika.dim("vrs")):
                vrstica = []
                for j in range (self.matrika.dim("sto")):
                    vrstica.append(a.kofaktor(i, j))
                prirejenka.append(vrstica)
                
            prirejenka = Matrika(prirejenka)
            prirejenka.Transponiranje()
            return prirejenka

    def InverzMatrike(self, a):

        a = Matrika(a)

        if a.dim("vrs") != a.dim("sto"):
            raise ArithmeticError("Matrika ni kvadratna zato nima inverza.")

        if a.DeterminantaMatrike == 0:
            raise ZeroDivisionError("Determinanta matrike je enaka 0 zato matrika nima inverza")
                
        InverznaMatrika = a.PrirejenkaMatrike() / (a.DeterminantaMatrike())
        InverznaMatrika = Matrika(InverznaMatrika)
        return InverznaMatrika
    
#########################################################################################
#########################################################################################
#########################################################################################

class Operacije:

    def MnozenjeSSkalarjem(self, a, skalar):

        nova = []
        y = Matrika(a)

        for i in range (y.dim("vrs")):
            z = 0
            for j in range (y.dim("sto")):
                z += a[i][j] * skalar
            nova.append(z)
        return nova

    def SestevanjeMatrik(self, a, b):
        sestevek = []
        x = Matrika(a)
        for i in range (x.dim("vrs")):
            vrstica = []
            for j in range (x.dim("sto")):
                vrstica.append(a[i][j] + b[i][j])
            sestevek.append(vrstica)
        return sestevek

    def MnozenjeMatrik(self, a, b):
        zmnozek = []
        x = Matrika(a)

        if x.dim("vrs") == x.dim("sto"):
            for i in range (x.dim("vrs")):
                vrstica = []
                for j in range (x.dim("sto")):
                    vrstica.append(a[i][j] * b[j][i])
                zmnozek.append(vrstica)
            return zmnozek
        else:
            raise ArithmeticError("Matriki ni mogoce zmnoziti." )
        
    def EnotskiVektor(self, v):

        x = Matrika(v)

        if  x.dim("vrs") > 1 and x.dim("sto") > 1:
            raise ArithmeticError("Vektor mora biti ali ena vrstica ali en stolpec")
        
        norma = 0
        for i in range(x.dim("vrs")):
            for j in range(x.dim("sto")):
                norma += x.element(i, j) ** 2
        
        norma = norma ** 0.5
        EnotskiVektor = x.KopijaMatrike()

        for i in range (x.dim("vrs")):
            for j in range (x.dim("sto")):
                EnotskiVektor[i][j] = EnotskiVektor[i][j] / norma
            
        return EnotskiVektor
        
    

    def SkalaraniProdukt(self, a, b):

        v1 = Matrika(a)
        v2 = Matrika(b)

        if (v1.dim("vrs") > 1 and v1.dim("sto") > 1) or (v2.dim("vrs") > 1 and v2.dim("sto") > 1):
            raise ArithmeticError("Vektor mora biti ali ena vrstica ali en stolpec")

        skalarni = 0

        if v1.dim("vrs") == 1 and v2.dim("vrs") == 1 and v1.dim("sto") == v2.dim("sto"):
            for i in range (v1.dim("sto")):
                skalarni += a[0][i] * b[0][i]
        
        elif v1.dim("vrs") == 1 and v2.dim("sto") == 1 and v1.dim("sto") == v2.dim("vrs"):
            v2 = v2.Transponiranje()
            for i in range (v1.dim("sto")):
                skalarni += a[0][i] * b[i][0]

        elif v1.dim("sto") == 1 and v2.dim("vrs") == 1 and v1.dim("vrs") == v2.dim("sto"):
            v1 = v1.Transponiranje()
            v1 = Matrika(v1)
            for i in range (v1.dim("sto")):
                skalarni += a[i][0] * b[0][i] 

        elif v1.dim("sto") == 1 and v2.dim("sto") == 1 and v1.dim("vrs") == v2.dim("vrs"):
            v1 = v1.Transponiranje()
            v2 = v2.Transponiranje()
            skalarni += a[i][0] * b[i][0] 
        return skalarni

    def VektorskiProdukt(self, a, b):

        vektor1 = Matrika(a)
        vektor2 = Matrika(b)

        v1 = vektor1.dim("vrs")
        s1 = vektor1.dim("sto")
        v2 = vektor2.dim("vrs")
        s2 = vektor2.dim("sto")
        koeficienti = []
        produkt = [] 
        prvi = 0
        drugi = 0
        tretji = 0

        if ((v1 == 1 and s1 == 3) or (s1 == 1 and v1 == 3)) and ((v2 == 1 and s2 == 3) or (s2 == 1 and v2 == 3)):
            
            if v1 == 1 and v2 == 1:
                pass

            elif v1 == 1 and v2 == 3:
                vektor2 = vektor2.Transponiranje()
            
            elif v1 == 3 and v2 == 1:
                vektor1 = vektor1.Transponiranje()
            
            elif v1 == 3 and v2 == 3:
                vektor1 = vektor1.Transponiranje()
                vektor2 = vektor2.Transponiranje()
                
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