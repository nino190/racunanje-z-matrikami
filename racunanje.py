class Matrika:

    def KopijaMatrike(self, matrika):
        kopija = []
        for i in range(len(matrika)):
            kopija.append(matrika[i])
        return kopija

    def Identiteta(self, n):
        IdentitetnaMatrika = []
        for i in range (1, n + 1):
            IdentitetnaMatrika.append((i - 1) * [0] + [1] + (n - i) * [0])
        return IdentitetnaMatrika

    def SledMatrike(self, matrika):
        sled = 0
        for i in range(len(matrika)):
            sled += matrika[i][i]
        return sled
    
    def Transponiranje(self, matrika):
        v = len(matrika[0])
        s = len(matrika)
        TransponiranaMatrika = []
        for i in range(v):
            vrstica = []
            for j in range(s):
                vrstica.append(matrika[j][i])
            TransponiranaMatrika.append(vrstica)
        return TransponiranaMatrika

    def MnozenjeZVektorjem(self, matrika, vektor):
        nova = []
        for i in range(0, len(matrika)):
            a = 0
            for j in range (0, len(matrika[0])):
                a += matrika[i][j] * vektor[j]
            nova.append(a)
        return nova

    def SestevanjeMatrik(self, prva, druga):
        sestevek = []
        for i in range(len(prva)):
            vrstica = []
            for j in range(prva[0]):
                vrstica.append(prva[i][j] + druga[i][j])
            sestevek.append(vrstica)
        return sestevek

    def MnozenjeMatrik(self, prva, druga):
        zmnozek = []
        if len(prva) == len(druga[0]):
            for i in range(len(prva)):
                vrstica = []
                for j in range(len(druga[0])):
                    vrstica.append(prva[i][j] * druga[j][i])
                zmnozek.append(vrstica)
            return zmnozek
        else:
            raise ArithmeticError("Matriki ni mogoce zmnoziti." )
    
    def DeterminantaMatrike(self, matrika, determinanta = 0):
        indeksi = list(range(len(matrika)))
        if len(matrika) == len(matrika[0]):
            if len(matrika) == 2:
                mala = matrika[0][0] * matrika[1][1] - matrika[1][0] * matrika[0][1]
                return mala

            for i in indeksi:
                minor = KopijaMatrike(matrika)
                minor = minor[1:]
                SteviloVrstic = len(minor)
 
                for j in range(SteviloVrstic): 
                    minor[j] = minor[j][0:i] + minor[j][i + 1:]
 
                kofaktor = (-1) ** (i % 2) * DeterminantaMatrike(minor)
                determinanta += matrika[0][i] * kofaktor
            return determinanta
        else:
            raise ArithmeticError("Determinanta ne obstaja ker matrika ni kvadratna")
    
    def EnotskiVektor(self, vektor):
        if len(vektor) > 1 or len(vektor[0]) > 1:
            raise ArithmeticError("Vektor mora biti ali ena vrstica ali en stolpec")
        
        norma = 0
        for i in vektor:
            for vrednost in vektor:
                norma += vrednost ** 2
        
        norma = norma ** 0.5

        EnotskiVektor = KopijaMatrike(vektor)

        for i in range(len(vektor)):
            for j in range(len(vektor[0])):
                EnotskiVektor[i][j] = EnotskiVektor[i][j] / norma
        
        return EnotskiVektor
    
    def PrirejenkaMatrike(self, matrika):
        if len(matrika) != len(matrika[0]):
            raise ArithmeticError("Prirejenka ne obstaja")
        
        indeksi = list(range(len(matrika)))
        prirejenka = []
        for a in len(matrika):
            for i in indeksi:
                vrstica = []
                minor = KopijaMatrike(matrika)
                minor = minor[1:]
                SteviloVrstic = len(minor)
                for j in range(SteviloVrstic):
                    minor[j] = minor[j][0:i] + minor[j][i + 1:]
            
                kofaktor = (-1) ** (i % 2) * DeterminantaMatrike(minor) * matrika[a][i]
                vrstica.append(kofaktor)
            prirejenka.append(vrstica)
        prirejenka = Transponiranje(prirejenka)
        return prirejenka

    def InverzMatrike(self, matrika):
        if len(matrika) != len(matrika[0]):
            raise ArithmeticError("Matrika ni kvadratna zato nima inverza.")
        if DeterminantaMatrike(matrika) == 0:
            raise ZeroDivisionError("Determinanta matrike je enaka 0 zato matrika nima inverza")
        
        InverznaMatrika = prirejenka * (DeterminantaMatrike(matrika) ** (-1))
        return InverznaMatrika
    
    def PrehodMedBazami(self, vektor, baza1, baza2):
        prehodna1s = baza1
        prehodna2s = baza2
        prehodna12 = MnozenjeMatrik(InverzMatrike(prehodna1s), prehodna2s)
        VektorVDrugiBazi = MnozenjeZVektorjem(prehodna12, vektor)
        return prehodna12, VektorVDrugiBazi



