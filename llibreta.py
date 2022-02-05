import client as cl

class Llibreta:
    contador = 0

    def __init__(self):
        self.llistaClients = []
        self.idClient = self.contador
        
        self.contador += 1
    
    def get_llista_clients(self):
        for client in self.llistaClients:
            print(client)

    def afegir_client(self, nom, cognom, telefon, correu, adreca, ciutat):
        self.llistaClients.append(cl(nom, cognom, telefon, correu, adreca))

    def eliminar_client(self, idClient):
        for client in self.llistaClients:
            if idClient == client.id:
                self.llistaClients.remove(client)

#    def cercar_per_id(self, idClient):
#        x = 0

#    def cercar_per_nom():
#        x = 0

#    def cercar_per_cognom():
#        x = 0