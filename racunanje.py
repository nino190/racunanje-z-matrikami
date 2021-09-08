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

        if type(self.matrika) == Matrika:
            kopija = []
            for i in range(self.matrika.dim("vrs")):
                kopija.append(self.matrika.vrstica(i))
            return kopija
        
        else:
            kopija = []
            for i in range(Matrika(self.matrika).dim("vrs")):
                kopija.append(self.matrika[i])
            return kopija
        
    def Transponiranje(self):
        transponirana = []
        for i in range(1, Matrika(self.matrika).dim("sto") + 1):
            transponirana.append(Matrika(self.matrika).stolpec(i))
        return transponirana

def matrika(*argumenti):
    
    mat = []
    for arg in argumenti:
        mat.append(arg)
    return mat

def vrs(*argumenti):

    r = []
    for arg in argumenti:
        r.append(arg)
    return r

def DeterminantaMatrike(a):

    if type(a) == Matrika:
     
        if a.dim("vrs") == 2 and a.dim("sto") == 2:
            return a.element(1, 1) * a.element(2, 2) - a.element(1, 2) * a.element(2, 1)

        determinanta = 0
        for i in range(a.dim("sto")):
            determinanta += a.element(1, i + 1) * kofaktor(a, 1, i + 1)

        return determinanta
    
    else:
        a = Matrika(a)
        if a.dim("vrs") == 2 and a.dim("sto") == 2:
            return a.element(1, 1) * a.element(2, 2) - a.element(1, 2) * a.element(2, 1)

        determinanta = 0
        for i in range(Matrika(a).dim("sto")):
            determinanta += a.element(1, i + 1) * kofaktor(a, 1, i + 1)

        return determinanta


def kofaktor(a, vrs, sto):

    kofaktor = 0
    a = Matrika(a).KopijaMatrike()
    a = Matrika(a)
    a.zbrisi_vrstico(vrs)
    a.zbrisi_stolpec(sto)
    kofaktor = DeterminantaMatrike(a)
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
                vrstica.append(kofaktor(b, i, j))
            prirejenka.append(vrstica)
            
        prirejenka = Matrika(prirejenka)
        prirejenka.Transponiranje()
        return prirejenka

def InverzMatrike(a):

    koordinata = Matrika(a).element

    def adj():
        adj_matrika = matrika()

        for x in range(1, Matrika(a).dim("vrs") + 1):
            vrs = []
            for y in range(1, Matrika(a).dim("sto") + 1):
                vrs.append(kofaktor(a, x, y))
            Matrika(adj_matrika).dodaj_vrstico(vrs)
        
        return Matrika(adj_matrika).Transponiranje()
            
    if Matrika(a).dim("vrs") == 2 and Matrika(a).dim("sto") == 2:
        div = 1 / DeterminantaMatrike(a)
        pred_inverzom = matrika(
            vrs(koordinata(2, 2), -1 * koordinata(1, 2)),
            vrs(-1 * koordinata(2, 1), -1 * koordinata(1, 1))
            )
        return Operacije().MnozenjeSSkalarjem(pred_inverzom, div)

    adj_matrika = adj()
    div = 1 / DeterminantaMatrike(a)

    return Operacije().MnozenjeSSkalarjem(adj_matrika, div) 

def EnotskiVektor(a):

    if  len(a) > 1:
        if type(a[0]) == int:
            pass
        elif len(a[0]) > 1:
            raise ArithmeticError("Vektor mora biti ali ena vrstica ali en stolpec")

    
    if len(a) > 1:
        norma = 0
        for i in range(len(a)):
            norma += a[i] ** 2
    
        norma = norma ** 0.5
        EnotskiVektor = a

        for i in range(len(a)):
            EnotskiVektor[i] = EnotskiVektor[i] / norma
            
        return EnotskiVektor
    else:
        norma = 0
        for i in range(len(a[0])):
            norma += a[0][i] ** 2
    
        norma = norma ** 0.5
        EnotskiVektor = a

        for i in range(len(a[0])):
            EnotskiVektor[0][i] = EnotskiVektor[0][i] / norma
            
        return EnotskiVektor

#########################################################################################
#########################################################################################
#########################################################################################

class Operacije():

    def MnozenjeSSkalarjem(self, a, skalar):
        if type(a) == Matrika:
            b = []
            for i in range(a.dim("vrs")):
                vrstica = []
                for j in range(a.dim("sto")):
                    vrstica.append(a.element(i + 1, j + 1) * skalar)
                b.append(vrstica)
            return b
        else:
            b = []
            for i in range(Matrika(a).dim("vrs")):
                vrstica = []
                for j in range(Matrika(a).dim("sto")):
                    vrstica.append(Matrika(a).element(i + 1, j + 1) * skalar)
                b.append(vrstica)
            return b


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

        if type(v1[0]) == int and type(v2[0]) == int:
            skalarni = 0
            if len(v1) == len(v2):
                for i in range(len(v1)):
                    skalarni += v1[i] * v2[i]
            return skalarni
        else:

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

        produkt = []
        prvi = 0
        drugi = 0
        tretji = 0

        if type(vektor1[0]) == int and type(vektor2[0]) == int:
            if len(vektor1) == 3 and len(vektor2) == 3:
                prvi = vektor1[1] * vektor2[2] - vektor1[2] * vektor2[1]
                drugi = vektor1[2] * vektor2[0] - vektor1[0] * vektor2[2]
                tretji = vektor1[0] * vektor2[1] - vektor1[1] * vektor2[0]

                produkt.append(prvi)
                produkt.append(drugi)
                produkt.append(tretji)
                return produkt

            else:
                raise ArithmeticError("Vektorji niso tridimenzionalni.")              

        else:

            v1 = Matrika(vektor1).dim("vrs")
            s1 = Matrika(vektor1).dim("sto")
            v2 = Matrika(vektor2).dim("vrs")
            s2 = Matrika(vektor2).dim("sto")
            

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
            
                produkt.append(prvi)
                produkt.append(drugi)
                produkt.append(tretji)
                return produkt

def print_matrix(a):
    
    vrstice = Matrika(a).dim("vrs")
    for i in range(vrstice):
        print(Matrika(a).vrstica(i+1))