import uuid
import client

class Llibreta:
    llistaClients = []
    idClient = 0

    def __init__(self):
        self.llistaClients = []
        self.idClient = ""
        
    
    def get_llista_clients(self):
        for client in self.llistaClients:
            print(client.__str__)

    def afegir_client(self, nom, cognom, telefon, correu, adreca, ciutat):
        id = uuid.uuid4()
        newClient = client.Client(id, nom, cognom, telefon, correu, adreca, ciutat)
        self.llistaClients.append(newClient)

    def eliminar_client(self, idClient):
        for clientTmp in self.llistaClients:
            if str(client.id) == idClient:
                self.llistaClients.remove(clientTmp)

    def cercar_per_id(self, idClient):
        x = []
        for clientTmp in self.llistaClients:
            if str(clientTmp.id) == idClient:
                x.append(clientTmp)
        return x

    def cercar_per_nom(self, nom):
        x = []
        for clientTmp in self.llistaClients:
            if clientTmp.nom == nom:
                x.append(clientTmp)
        return x

    def cercar_per_cognom(self, cognom):
        x = []
        for clientTmp in self.llistaClients:
            if clientTmp.cognom == cognom:
                x.append(clientTmp)
        return x