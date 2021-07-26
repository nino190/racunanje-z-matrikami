from racunanje import Matrika

def vnesi(i, j):
    print ('Vnesi (' + str(i) + ', ' + str(j) + ') - ti element matrike: ')
    x = input ('> ')
    return x

class VhodnaMatrika():
    
    def __init__(self, vrstice, stolpci):

        self.vrs = int(vrstice)
        self.sto = int(stolpci)
        self.vhodna = []

        for i in range (1, self.vrs + 1):
            vrstica = []
            for j in range (1, self.sto + 1):

                x = vnesi(i, j)
                while x is not float:
                    print('To ni število. Prosim vnesi število.')
                    x = vnesi(i, j)
                
                vrstica.append(x)

            self.vhodna.append(vrstica)