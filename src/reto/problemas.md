 seccion 1.1 
 # Ascenso hasta altitud objetivo

simula como un avion asciende hacia una altitud establecida
- el usuario decide si aumenta, mantiene o disminuye la velocidad de ascenso cada segundo.
- el usuario cada 5 minutos ingresa el angulo de ascenso.
- ecuacion: altitud = velocidad_ascenso . seno(angulo_ataque) . tiempo_transcurrido
## Tabla de datos:

| Variables de entrada | variables de salida | variable de control | Constante |
|----------------------|---------------------|---------------------|-----------|
| velocidad_ascenso | altitud_actual | angulo_ataque | tiempo_transcurrido |

## Pseudocodigo:

``` 
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

    altitud_actual = velocidad_ascenso * math.sin(math.radians(angulo_ataque)) * tiempo_transcurrido
    tiempo_transcurrido += 1

print("\n¡El avión alcanzó la altitud objetivo!")
print(f"Altitud final: {altitud_actual:.2f}")

```   


seccion 1.2
#  Turbulencia y estabilidad del avión

simula el efecto de la turbulencia sobre el ángulo de ataque.
- cada segundo hay una variación aleatoria en el ángulo.
- el usuario puede compensar el ángulo con sus decisiones.
- si el ángulo de ataque llega a 15° o más, el avión entra en pérdida y la simulación termina.
ecuacion = angulo_actual​= angulo_anterior​+turbulencia+compensacion
si el angulo actual supera el angulo limte, la aeronave entra en perdida.
## Tabla de datos:

| Variables de entrada | variables de salida | variable de control |constante|
|----------------------|---------------------|---------------------|---------|
|Turbulencia  | Angulo actual | compensacion | Angulo limite |

## Pseudocodigo:

```  
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

```  
seccion 1.3
# Autonomía con consumo de combustible

simula el consumo de combustible durante un vuelo.
- el usuario inicia con cierta cantidad de combustible y una velocidad.
- en cada minuto puede decidir aumentar, mantener o reducir la velocidad, lo que cambia el consumo.
- el vuelo continúa hasta que se acaba el combustible o el usuario decide aterrizar.
ecuacion = combustible restante = combustible inicial(velocidad . constante de consumo . tiempo de vuelo )
la constante de ecuacion va a aplicar para un A380, seria constante, Consumo A380: 11.400 Litros por hora.
## Tabla de datos:

| Variables de entrada | variables de salida | variable de control | constante |
|----------------------|---------------------|---------------------|-----------|
| velocidad | combustible restante | decision de usuario(aumentar, mantener o reducir la velocidad)   , aterrizar o seguir en vuelo | consumo A380 |

## Pseudocodigo:

```
# Simulación de autonomía con consumo de combustible - Airbus A380

# Constante de consumo (litros por hora)
CONSUMO_A380 = 11400  

# Entradas iniciales
combustible = 11400
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
    print("Opciones:\n. 1 = Aumentar velocidad\n.  2 = Mantener\n. 3 = Reducir velocidad\n. 4 = Aterrizar")
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
    consumo_por_minuto = (CONSUMO_A380) / 60
    combustible -= consumo_por_minuto

# Fin de simulación
if combustible <= 0:
    print("\n El combustible se agotó. Vuelo terminado.")
```
