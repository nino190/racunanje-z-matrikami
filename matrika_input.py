from racunanje import Matrika

class VhodnaMatrika():
    
    def __init__(self, vrstice, stolpci):

        self.vrs = int(vrstice)
        self.sto = int(stolpci)
        self.vhodna = []

        for i in range (1, self.vrs + 1):
            vrstica = []
            for j in range (1, self.sto + 1):

                print ('Vnesi (' + str(i) + ', ' + str(j) + ') - ti element matrike: ')
                x = input ('> ')
                vrstica.append(x)

            self.vhodna.append(vrstica)
