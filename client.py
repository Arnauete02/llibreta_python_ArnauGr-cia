import llibreta as ll

class Client:

    #constructor
    def __init__(self, nom, cognom, telefon, correu, adreca, ciutat):  
        self.id = ll.contador
        self.nom = nom
        self.cognom = cognom
        self.telefon = telefon
        self.correu = correu
        self.adreca = adreca
        self.ciutat = ciutat

    #representacio client -> string
    def __str__(self):
        print("Client->[id = "+ self.id +
        ", nom = "+ self.nom +
        ", cognom = "+ self.cognom +
        ", telefon = "+ self.telefon +
        ", correu = "+ self.correu +
        ", adreca = "+ self.adreca +
        ", ciutat = "+ self.ciutat + "]")
