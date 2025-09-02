
# ultimizamos una variable tipo booleana -> una bandera
control = True

while control == True:
    print("1. Entradas\n2. Platos fuertes\n3. Bebidas" \
        "\n4. Postres\n5. salir")
    opcion = int(input("elija una opcion: "))
    match opcion:
        case 1: 
            print("1. patacon con huevo")
            print("2. yuca con chicharron")
            print("3. guineo con suero")
            print()
        case 2: 
            print("1. solomito")
            print("2. hamburguesa")
            print("3. sushi")
            print()
        case 3: 
            print("1. limonada")
            print("2. jugos naturales")
            print("3. cerveza")
            print()
        case 4: 
            print("1. tres leches")
            print("2. tiramisu")
            print("3. rollos de canela")
            print()
        case 5: 
            control = False
        case _:
            print("opcion no valida")   
            print()
        


        



