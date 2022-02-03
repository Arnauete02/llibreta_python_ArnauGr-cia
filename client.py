from typing_extensions import Self


import uuid

class Client:

    #constructor
    def __init__(self, nom, cognom, telefon, correu, adreca, ciutat):  
        #self.id = uuid.uuid1()
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
