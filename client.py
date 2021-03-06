class Client:
    id = ""
    nom = ""
    cognom = ""
    telefon = ""
    correu = ""
    adreca = ""
    ciutat = ""

    #constructor
    def __init__(self, id, nom, cognom, telefon, correu, adreca, ciutat):  
        self.id = id
        self.nom = nom
        self.cognom = cognom
        self.telefon = telefon
        self.correu = correu
        self.adreca = adreca
        self.ciutat = ciutat

    #representacio client -> string
    def __str__(self):
        s = ("Client->[id = "+ str(self.id) +
        ", nom = "+ self.nom +
        ", cognom = "+ self.cognom +
        ", telefon = "+ str(self.telefon) +
        ", correu = "+ self.correu +
        ", adreca = "+ self.adreca +
        ", ciutat = "+ self.ciutat + "]")
        return s
