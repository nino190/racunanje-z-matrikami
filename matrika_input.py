from racunanje import Matrika

class VhodnaMatrika():
    
    def __init__(self, vrstice, stolpci):

        self.vrs = vrstice
        self.sto = stolpci
        self.vhodna = []

        for i in range (self.vrs):
            vrstica = []
            for j in range (self.sto):

                print ('Vnesi (' + str(i) + ', ' + str(j) + ') - ti element matrike: ')
                x = input ('> ')
                vrstica.append(x)

            self.vhodna.append(vrstica)