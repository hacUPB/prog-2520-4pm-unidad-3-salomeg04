# imprimir los numeros pares entre el 20 y el 80
'''
numero=20
while numero <= 80:
    print(numero)
    numero += 2 
''' 

# imprimir los numeros impares entre el 99 y el 61 en orden descendente 

'''
numero=99
while numero >=61:
    print(numero)
    numero -= 2
'''

# solicitar dos numeros al usuario e imprimir los numeros impares entre ellos

'''
numero1 = int(input("ingrese numero a:"))
numero2 =int(input("ingrese numero b:"))

if numero1 > numero2:
    mayor = numero1
    menor = numero2
else: 
    mayor = numero2
    menor = numero1 

while menor<= mayor: 
    if menor % 2 == 1: 
        print(menor)
    menor += 1
'''

# imprimir los multiplos de 7 entre 0 y 100 

'''

numero = 0 
while numero<=100:
    if  numero % 7 == 0:
         print(numero)
    numero +=1
''' 

# solicitar un numero al usuario e imprimir su tabla de multiplicar hasta 15

'''
numero= int(input("ingrese un numero entero: "))
i=1 
while i <= 15:
     resultado = i * numero 
     print(f"{numero} x {i} = {resultado}")
     i += 1
''' 

import math

velocidad_ascenso = float(input("Ingrese la velocidad de ascenso de la aeronave: "))
altitud_objetivo = float(input("Ingrese la altitud objetivo: "))

altitud_actual = 0
tiempo_transcurrido = 0
angulo_ataque = float(input("Ingrese el ángulo inicial de ascenso (en grados): "))

while altitud_actual < altitud_objetivo:
    print(f"\nTiempo: {tiempo_transcurrido} segundos")
    print(f"Altitud actual: {altitud_actual:.2f}")
    print("Opciones: 1 = Aumentar velocidad \n 2 = Mantener \n 3 = Disminuir")
    opcion = input("Seleccione opción: ")

    if opcion == "1":
        velocidad_ascenso += 10
    elif opcion == "3":
        velocidad_ascenso -= 10
        if velocidad_ascenso < 0:  
            velocidad_ascenso = 0
            if tiempo_transcurrido % 300 == 0 and tiempo_transcurrido != 0:
                angulo_ataque = float(input("Ingrese nuevo ángulo de ascenso (en grados): "))
                altitud_actual = velocidad_ascenso * math.sin(angulo_ataque) * tiempo_transcurrido
                tiempo_transcurrido += 1

print("\n¡El avión alcanzó la altitud objetivo!")
print(f"Altitud final: {altitud_actual:.2f}")