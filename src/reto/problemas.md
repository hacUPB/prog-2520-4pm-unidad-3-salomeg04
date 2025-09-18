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
inicio
    leer velocidad_ascenso
    leer altitud_objetivo
    leer angulo_ataque

    altitud_actual = 0
    tiempo_transcurrido = 0

    mientras altitud_actual < altitud_objetivo hacer
        mostrar "tiempo:", tiempo_transcurrido, "segundos"
        mostrar "altitud actual:", altitud_actual

        mostrar "opciones:"
        mostrar "1 = aumentar velocidad"
        mostrar "2 = mantener"
        mostrar "3 = disminuir"

        leer opcion

        si opcion = 1 entonces
            velocidad_ascenso = velocidad_ascenso + 10
        sino si opcion = 3 entonces
            velocidad_ascenso = velocidad_ascenso - 10
            si velocidad_ascenso < 0 entonces
                velocidad_ascenso = 0
            fin si
        fin si

        si tiempo_transcurrido % 300 = 0 y tiempo_transcurrido ≠ 0 entonces
            leer angulo_ataque
        fin si

        altitud_actual = velocidad_ascenso * sen(angulo_ataque en radianes) * tiempo_transcurrido

        tiempo_transcurrido = tiempo_transcurrido + 1
    fin mientras

    mostrar "¡el avión alcanzó la altitud objetivo!"
    mostrar "altitud final:", altitud_actual
fin


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
inicio
    leer angulo_actual
    angulo_limite = 15
    tiempo = 0

    mostrar "simulación de turbulencia"

    mientras angulo_actual < angulo_limite hacer
        tiempo = tiempo + 1

        turbulencia = valor_aleatorio_entre(-3, 3)

        mostrar "ingrese compensación (-2, -1, 0, 1, 2): "
        leer compensacion

        si compensacion está en [-2, -1, 0, 1, 2] entonces
            compensacion = entero(compensacion)
        sino
            compensacion = 0
        fin si

        angulo_actual = angulo_actual + turbulencia + compensacion

        mostrar "tiempo:", tiempo, "s"
        mostrar "turbulencia:", turbulencia
        mostrar "compensación:", compensacion
        mostrar "ángulo actual:", angulo_actual
    fin mientras

    mostrar "el avión entró en pérdida (ángulo límite superado)."
fin

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
inicio
    consumo_a380 = 11400

    combustible = 11400
    leer velocidad

    tiempo = 0

    mostrar "simulación de vuelo"

    mientras combustible > 0 hacer
        tiempo = tiempo + 1

        mostrar "minuto:", tiempo
        mostrar "velocidad actual:", velocidad, "km/h"
        mostrar "combustible restante:", combustible, "l"

        mostrar "opciones:"
        mostrar "1 = aumentar velocidad"
        mostrar "2 = mantener"
        mostrar "3 = reducir velocidad"
        mostrar "4 = aterrizar"

        leer opcion

        si opcion = 1 entonces
            velocidad = velocidad + 50
        sino si opcion = 3 entonces
            velocidad = velocidad - 50
            si velocidad < 100 entonces
                velocidad = 100
            fin si
        sino si opcion = 4 entonces
            mostrar "el avión aterrizó exitosamente."
            break
        fin si

        consumo_por_minuto = consumo_a380 / 60
        combustible = combustible - consumo_por_minuto
    fin mientras

    si combustible <= 0 entonces
        mostrar "el combustible se agotó. vuelo terminado."
    fin si
fin

```
