# Determinar si un numero es par o impar
#leer numero 
numero = int(input("ingresa un numero entero: "))
residuo = numero % 2
#si residuo es cero es par 
if residuo == 0:
    print(numero, " es par")
else:
    print(numero, " es impar")
    