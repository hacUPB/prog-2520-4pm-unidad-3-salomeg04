print("ingrese la zona de envio. ")
zona = int(input("1. Norteamerica\n2. Centroamerica\n3. Suramerica\
                 \n4. Europa\n5. Asia\nElija un numero:"))
if zona > 0 and zona < 6:
    peso = int(input("ingrese el peso del paquete en gramo: "))
    if peso < 5000: 
        if zona == 1:
             total = peso * 11
        elif zona == 2:
             total = peso * 10
        elif zona == 3:
             total = peso * 12
        elif zona == 4:
             total = peso * 24
        elif zona == 5:
             total = peso * 27 
        
        print(f"El envio de su paquete cuesta ${total}.") 
    else: 
         print("No se puede envia paquetes de mas de 5kg. ") 
else: 
             print("la zona ingresada no existe. ")



