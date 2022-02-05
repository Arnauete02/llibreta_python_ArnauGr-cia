from llibreta import Llibreta

def mostrar_menu_principal():
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
            nom = input("Nom del client: ")
            cognom = input("Cognom: ")
            telefon = int(input("Telefon: "))
            correu = input("Correu electronic: ")
            adreca = input("Adreca: ")
            ciutat = input("Ciutat: ")

            
            Llibreta.afegir_client(nom, cognom, telefon, correu, adreca, ciutat)
        elif option == 2:
            print(2)
        elif option == 3:
            print(3)
            mostrar_menu_consulta()
        elif option == 4:
            print(4)
        elif option == 5:
            print(5)
            break
        else:
            print("Cap número correcte seleccionat.\n")
            mostrar_menu_principal()

def mostrar_menu_consulta():
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
            print(1)
        elif option == 2:
            print(2)
        elif option == 3:
            print(3)
        elif option == 4:
            print(4)
        elif option == 5:
            print(5)
        elif option == 6:
            print(6)
            break
        else:
            print("Cap número correcte seleccionat.")
            mostrar_menu_consulta()