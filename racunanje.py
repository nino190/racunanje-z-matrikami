class Matrika:

    def __init__(self, matrika):
        self.matrika = matrika
    
    def dimenzija(self, dim):
        if dim == "vrstice":
            return len(self.matrika)
        elif dim == "stolpci":
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

    def element_matrike(self, vrs, sto):
        return Matrika(self.matrika).vrstica(vrs)[sto-1]

    def KopijaMatrike(self, matrika):
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
        for i in range(1, Matrika(self.matrika).dimenzija("stolpci") + 1):
            transponirana.append(Matrika(self.matrika).stolpec(i))
        return transponirana

#########################################################################################
#########################################################################################
#########################################################################################

    def MnozenjeZVektorjem(matrika, vektor):
        nova = []
        for i in range(0, len(matrika)):
            a = 0
            for j in range (0, len(matrika[0])):
                a += matrika[i][j] * vektor[j]
            nova.append(a)
        return nova

    def SestevanjeMatrik(prva, druga):
        sestevek = []
        for i in range(len(prva)):
            vrstica = []
            for j in range(prva[0]):
                vrstica.append(prva[i][j] + druga[i][j])
            sestevek.append(vrstica)
        return sestevek

    def MnozenjeMatrik(prva, druga):
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
        
    def DeterminantaMatrike(matrika, determinanta = 0):
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
        
    def EnotskiVektor(vektor):
        if len(vektor) > 1 and len(vektor[0]) > 1:
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
        
    def PrirejenkaMatrike(matrika):
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

    def InverzMatrike(matrika):
        if len(matrika) != len(matrika[0]):
            raise ArithmeticError("Matrika ni kvadratna zato nima inverza.")
        if DeterminantaMatrike(matrika) == 0:
            raise ZeroDivisionError("Determinanta matrike je enaka 0 zato matrika nima inverza")
            
        InverznaMatrika = PrirejenkaMatrike(matrika) * (DeterminantaMatrike(matrika) ** (-1))
        return InverznaMatrika
        
    def PrehodMedBazami(vektor, baza1, baza2): 
        prehodna1s = baza1
        prehodna2s = baza2
        prehodna12 = MnozenjeMatrik(InverzMatrike(prehodna1s), prehodna2s)
        VektorVDrugiBazi = MnozenjeZVektorjem(prehodna12, vektor)
        return prehodna12, VektorVDrugiBazi

    def SkalaraniProdukt(vektor1, vektor2):
        if (len(vektor1) > 1 and len(vektor1[0]) > 1) or (len(vektor2) > 1 and len(vektor2[0]) > 1):
            raise ArithmeticError("Vektor mora biti ali ena vrstica ali en stolpec")

        skalarni = 0

        if len(vektor1) == 1 and len(vektor2) == 1 and len(vektor1[0]) == len(vektor2[0]):
            for i in range(len(vektor1[0])):
                skalarni += vektor1[0][i] * vektor2[0][i]
        
        elif len(vektor1) == 1 and len(vektor2[0]) == 1 and len(vektor1[0]) == len(vektor2):
            vektor2 = Transponiranje(vektor2)
            for i in range(len(vektor1[0])):
                skalarni += vektor1[0][i] * vektor2[0][i]

        elif len(vektor1[0]) == 1 and len(vektor2) == 1 and len(vektor1) == len(vektor2[0]):
            vektor1 = Transponiranje(vektor1)
            for i in range(len(vektor1[0])):
                skalarni += vektor1[0][i] * vektor2[0][i] 

        elif len(vektor1[0]) == 1 and len(vektor2[0]) == 1 and len(vektor1) == len(vektor2):
            vektor1 = Transponiranje(vektor1)
            vektor2 = Transponiranje(vektor2)
            skalarni += vektor1[0][i] * vektor2[0][i] 

        return skalarni

    def VektorskiProdukt(vektor1, vektor2):
        v1 = len(vektor1)
        s1 = len(vektor1[0])
        v2 = len(vektor2)
        s2 = len(vektor2[0])
        koeficienti = []
        produkt = [] 
        prvi = 0
        drugi = 0
        tretji = 0

        if ((v1 == 1 and s1 == 3) or (s1 == 1 and v1 == 3)) and ((v2 == 1 and s2 == 3) or (s2 == 1 and v2 == 3)):
            
            if v1 == 1 and v2 == 1:
                pass

            elif v1 == 1 and v2 == 3:
                vektor2 = Transponiranje(vektor2)
            
            elif v1 == 3 and v2 == 1:
                vektor1 = Transponiranje(vektor1)
            
            elif v1 == 3 and v2 == 3:
                vektor1 = Transponiranje(vektor1)
                vektor2 = Transponiranje(vektor2)
                
            prvi = vektor1[0][1] * vektor2[0][2] - vektor1[0][2] * vektor2[0][1]
            drugi = vektor1[0][2] * vektor2[0][0] - vektor1[0][0] * vektor2[0][2]
            tretji = vektor1[0][0] * vektor2[0][1] - vektor1[0][1] * vektor2[0][0]
            
            koeficienti.append(prvi)
            koeficienti.append(drugi)
            koeficienti.append(tretji)
            produkt.append(koeficienti)
            return produkt