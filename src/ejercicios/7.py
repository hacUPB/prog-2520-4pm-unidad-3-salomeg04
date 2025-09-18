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
'''
import math 
velocidad_ascenso = float(input("Ingrese la velocidad de ascenso de la aeronave: "))
altitud_objetivo = float(input("Ingrese la altitud objetivo: "))
angulo_ataque = float(input("Ingrese el ángulo inicial de ascenso (en grados): "))

altitud_actual = 0
tiempo_transcurrido = 0


while altitud_actual < altitud_objetivo:
    print(f"\nTiempo: {tiempo_transcurrido} segundos")
    print(f"Altitud actual: {altitud_actual:.2f}")

    print("Opciones:\n 1 = Aumentar velocidad \n 2 = Mantener \n 3 = Disminuir")
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
'''
'''
import random

# Variables iniciales
angulo_actual = float(input("Ingrese el ángulo inicial del avión en grados: "))
angulo_limite = 15
tiempo = 0

print("\n--- Simulación de turbulencia ---")

# Simulación
while angulo_actual < angulo_limite:
    tiempo += 1

    # Turbulencia aleatoria entre -3 y 3 grados
    turbulencia = random.randint(-3, 3)

      # Usuario compensa el ángulo 
    compensacion = input("Ingrese compensación (-2, -1, 0, 1, 2): ")
    if compensacion in ["-2", "-1", "0", "1", "2"]:
        compensacion = int(compensacion)
    else:
        compensacion = 0   # si escribe otra cosa, tomamos 0

    # Ecuación del ángulo
    angulo_actual = angulo_actual + turbulencia + compensacion

    # Mostrar estado
    print(f"\nTiempo: {tiempo} s")
    print(f"Turbulencia: {turbulencia}")
    print(f"Compensación: {compensacion}")
    print(f"Ángulo actual: {angulo_actual:.2f}°")

# Fin de simulación
print(" El avión entró en pérdida (ángulo límite superado).")
'''
# Simulación de autonomía con consumo de combustible - Airbus A380

# Constante de consumo (litros por hora)
CONSUMO_A380 = 11400  

# Entradas iniciales
combustible = float(input("Ingrese la cantidad inicial de combustible en litros: "))
velocidad = float(input("Ingrese la velocidad inicial en km/h: "))

tiempo = 0  # en minutos

print("\n--- Simulación de vuelo ---")

# Simulación
while combustible > 0:
    tiempo += 1  # pasa un minuto de vuelo

    print(f"\nMinuto: {tiempo}")
    print(f"Velocidad actual: {velocidad} km/h")
    print(f"Combustible restante: {combustible:.2f} L")

    # Opciones del usuario
    print("Opciones:\n 1 = Aumentar velocidad \n 2 = Mantener \n 3 = Reducir velocidad \n 4 = Aterrizar")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        velocidad += 50
    elif opcion == "3":
        velocidad -= 50
        if velocidad < 100:   # límite mínimo de velocidad
            velocidad = 100
    elif opcion == "4":
        print("\n El avión aterrizó exitosamente.")
        break

    # Cálculo del consumo (convertimos horas a minutos dividiendo entre 60)
    consumo_por_minuto = (velocidad * CONSUMO_A380) / 60
    combustible -= consumo_por_minuto

# Fin de simulación
if combustible <= 0:
    print("\n El combustible se agotó. Vuelo terminado.")

