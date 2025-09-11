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
math import

velocidad_ascenso = float(input("Ingrese la velocidad de ascenso de la aeronave: "))
altitud_objetivo = float(input("Ingrese la altitud objetivo: "))

altitud_actual = 0
tiempo_transcurrido = 0
angulo_ataque = float(input("Ingrese el ángulo inicial de ascenso (en grados): "))

while altitud_actual < altitud_objetivo:
    print(f"\nTiempo: {tiempo_transcurrido} segundos")
    print(f"Altitud actual: {altitud_actual:.2f}")

     print("Opciones: 1 = Aumentar velocidad | 2 = Mantener | 3 = Disminuir")
    opcion = input("Seleccione opción: ")

    if opcion == "1":
        velocidad_ascenso += 10
    elif opcion == "3":
        velocidad_ascenso -= 10
        if velocidad_ascenso < 0:  
            velocidad_ascenso = 0

 if tiempo_transcurrido % 300 == 0 and tiempo_transcurrido != 0:
    angulo_ataque = float(input("Ingrese nuevo ángulo de ascenso (en grados): "))

 altitud_actual = velocidad_ascenso * seno(angulo_ataque) * tiempo_transcurrido

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