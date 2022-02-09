from xmlrpc import client
import llibreta

class Menu:
    llibretaClients = llibreta.Llibreta()

    def mostrar_menu_principal(self):
        option = 0

        while option >= 1 & option <= 5:
            option = int(input("MENU PRINCIPAL\n" +
                "=========================\n" +
                "Seleccioni una opció i premi Intro\n" +
                "=========================\n" +
                "\t1. Afegir client\n" +
                "\t2. Eliminar client\n" +
                "\t3. Consultar client\n" +
                "\t4. Modificar un camp d'un client (*)\n" +
                "\t5. Sortir\n\n" +
                "Enter an option: "))
            if option == 1:
                print("\n1. Afegir client\n")
                nom = input("Nom del client: ")
                cognom = input("Cognom: ")
                telefon = int(input("Telefon: "))
                correu = input("Correu electronic: ")
                adreca = input("Adreca: ")
                ciutat = input("Ciutat: ")

                self.llibretaClients.afegir_client(nom, cognom, telefon, correu, adreca, ciutat)
            elif option == 2:
                print("\n2. Eliminar client\n")
                idClient = input("Introdueix l'identificador del client que vols eliminar: ")
                if (self.llibretaClients.eliminar_client(self.llibretaClients, idClient)):
                    print("Client eliminat satifactoriament!")    
            elif option == 3:
                print("\n3. Consultar client\n")
                self.mostrar_menu_consulta(self.mostrar_menu_consulta)
            elif option == 4:
                print("\n4. Modificar un camp d'un client (*)\n")
                idClient = input("Introdueix l'identificador del client que vols eliminar: ")
                if client in self.llibretaClients.cercar_per_id(self.llibretaClients, idClient):
                    x = False
                    while not x:
                        print("\nQuin paràmetre vols modificar del client", client.identificador)
                        option = int(input("""
                            1. Nom:
                            2. Cognom
                            3. Telefon
                            4. Correu
                            5. Adreça
                            6. Ciutat
                            7. Sortir
    
                            Enter an option:"""))
                        if option == 1:
                            nom = input("Introdueix un nou nom: ")
                            client.nom = nom
                        elif option == 2:
                            cognom = input("Introdueix un nou cognom: ")
                            client.cognom = cognom
                        elif option == 3:
                            telefon = input("Introdueix un nou telefon: ")
                            client.telefon = telefon
                        elif option == 4:
                            correu = input("Introdueix un nou correu: ")
                            client.correu = correu
                        elif option == 5:
                            adreça = input("Introdueix un nou adreça: ")
                            client.adreça = adreça
                        elif option == 6:
                            ciutat = input("Introdueix un nou ciutat: ")
                            client.ciutat = ciutat
                        elif option == 7:
                            surtBucle = True
            elif option == 5:
                print("\nGood Bye!\n")
                break
            else:
                print("Cap número correcte seleccionat.\n")
                self.mostrar_menu_principal()

    def mostrar_menu_consulta(self):
        option = 0

        while option >= 1 & option <= 6:
            option = int(input("MENU CONSULTA\n" +
                "=========================\n" +
                "Seleccioni una opció i premi Intro\n" +
                "=========================\n" +
                "\t1. Cercar client per Identificador\n" +
                "\t2. Cercar client per Nom\n" +
                "\t3. Cercar client per Cognom\n" +
                "\t4. Llistar tots els clients\n" +
                "\t5. Llistar tots els clients per Nom\n\n" +
                "\t6. Enrere\n\n" +
                "Enter an option: "))
            if option == 1:
                print("\n1. Cercar client per Identificador\n")
                idClient = input("Introdueix l'identificador del client que vols eliminar: ")
                for clientTmp in self.llibretaClients.cercar_per_id(self.llibretaClients, idClient):
                    print(clientTmp, "\n")
            elif option == 2:
                print("\n2. Cercar client per Nom\n")
                nom = input("Introdueix el nom del client que vols eliminar: ")
                for clientTmp in self.llibretaClients.cercar_per_nom(self.llibretaClients, nom):
                    print(clientTmp, "\n")
            elif option == 3:
                print("\n3. Cercar client per Cognom\n")
                cognom = input("Introdueix el cognom del client que vols eliminar: ")
                for clientTmp in self.llibretaClients.cercar_per_cognom(self.llibretaClients, cognom):
                    print(clientTmp, "\n")
            elif option == 4:
                print("\n4. Llistar tots els clients\n")
                for clientTmp in self.llibretaClients:
                    print(clientTmp, "\n")
            elif option == 5:
                print("\n5. Llistar tots els clients per Nom\n")
                for clientTmp in sorted(self.llibretaClients, key=lambda x: x.nom):
                    print(clientTmp, "\n")
            elif option == 6:
                print("\n6. Enrere\n")
                self.mostrar_menu_principal()
            else:
                print("Cap número correcte seleccionat.")
                self.mostrar_menu_consulta()