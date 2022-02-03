def mostrar_menu_principal():
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

    while option >= 1 & option <= 5:
        if option == 1:
            print(1)
            break
        elif option == 2:
            print(2)
            break
        elif option == 3:
            print(3)
            mostrar_menu_consulta()
            break
        elif option == 4:
            print(4)
            break
        elif option == 5:
            print(5)
            break

def mostrar_menu_consulta():
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

    while option >= 1 & option <= 6:
        if option == 1:
            print(1)
            break
        elif option == 2:
            print(2)
            break
        elif option == 3:
            print(3)
            break
        elif option == 4:
            print(4)
            break
        elif option == 5:
            print(5)
            break
        elif option == 6:
            print(6)
            break