import math
import random


# 1.1 : Ascenso

def simulacion1():
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

        altitud_actual = velocidad_ascenso * math.sin(math.radians(angulo_ataque)) * tiempo_transcurrido
        tiempo_transcurrido += 1

    print("\n¡El avión alcanzó la altitud objetivo!")
    print(f"Altitud final: {altitud_actual:.2f}")



# 1.2: Turbulencia

def simulacion2():
    angulo_actual = float(input("Ingrese el ángulo inicial del avión en grados: "))
    angulo_limite = 15
    tiempo = 0
    print("\nSimulación de turbulencia ")

    while angulo_actual < angulo_limite:
        tiempo += 1
        turbulencia = random.randint(-3, 3)

        compensacion = input("Ingrese compensación (-2, -1, 0, 1, 2): ")
        if compensacion in ["-2", "-1", "0", "1", "2"]:
            compensacion = int(compensacion)
        else:
            compensacion = 0  

        angulo_actual = angulo_actual + turbulencia + compensacion

        print(f"\nTiempo: {tiempo} s")
        print(f"Turbulencia: {turbulencia}")
        print(f"Compensación: {compensacion}")
        print(f"Ángulo actual: {angulo_actual:.2f}°")

    print("El avión entró en pérdida (ángulo límite superado).")



# 1.3: Combustible

def simulacion3():
    CONSUMO_A380 = 11400  
    combustible = 11400
    velocidad = float(input("Ingrese la velocidad inicial en km/h: "))
    tiempo = 0  

    print("\n--- Simulación de vuelo ---")

    while combustible > 0:
        tiempo += 1  

        print(f"\nMinuto: {tiempo}")
        print(f"Velocidad actual: {velocidad} km/h")
        print(f"Combustible restante: {combustible:.2f} L")

        print("Opciones:\n 1 = Aumentar velocidad\n 2 = Mantener\n 3 = Reducir velocidad\n 4 = Aterrizar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            velocidad += 50
        elif opcion == "3":
            velocidad -= 50
            if velocidad < 100:
                velocidad = 100
        elif opcion == "4":
            print("\nEl avión aterrizó exitosamente.")
            break

        consumo_por_minuto = (CONSUMO_A380) / 60
        combustible -= consumo_por_minuto

    if combustible <= 0:
        print("\nEl combustible se agotó. Vuelo terminado.")



# Menu interactivo

control = True

while control == True:
    print("\n========= MENÚ =========")
    print("1. Simulación 1 (Ascenso)")
    print("2. Simulación 2 (Turbulencia)")
    print("3. Simulación 3 (Combustible)")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            simulacion1()
        case 2:
            simulacion2()
        case 3:
            simulacion3()
        case 4:
            print("Saliendo del programa...")
            control = False
        case _:
            print("Opción no válida\n")
