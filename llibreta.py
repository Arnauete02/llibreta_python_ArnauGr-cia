import client as c

class Llibreta:
    contador = 0

    def __init__(self):
        self.llistaClients = []
        self.idClient = self.contador
        
        self.contador += 1
    
    def get_llista_clients(self):
        for client in self.llistaClients:
            print(client)

    def afegir_client(self, client):
        if type(client) == type(c):
            self.llistaClients.append(client)

    def eliminar_client(self, client):
        self.llistaClients.remove(client)

    def cercar_per_id():
        x = 0

    def cercar_per_nom():
        x = 0

    def cercar_per_cognom():
        x = 0