'''
numero=int(input("ingrese un numero: "))

if numero > 0:
    print("numero es positivo", numero)

elif numero < 0:
    print("numero es negativo", numero)
else:
    print("numero es cero", numero)
'''
'''
numero=int(input("ingrese un numero entero positivo: "))
for i in range(1, numero+1):
  print(i)
'''
'''
numero=int(input("ingrese un numero entero positivo: "))
suma = 0 
for i in range (1 , numero +1):
    suma =suma + i 
    print("La suma de los números del 1 al", numero, "es:", suma)
'''
'''
numero = int(input("escribe un numero entero posititvo:"))
factorial = 1
for i in range (1, numero +1):
    factorial = factorial * i
    print("el factorial de los numeros del 1 al", numero, "es:", factorial)
'''
'''
numero = int(input("escribe un numero entero positivo: "))

for i in range(1, numero+1):
     if i % 2 == 0: 
         print(i)
'''
'''
numero = int (input("escriba un numero entero positivo: "))
suma = 0
for i in range (1, numero+1):
    if i % 2 == 0:
        suma = suma + i
print("La suma de los números pares del 1 al", numero ,"es:", suma)
'''
'''
numero = int(input("escriba un numero entero positivo: "))
control = True
for i in range (1, numero+1):
    if i % 1 == 0:
        print(i)
    elif i % i == 0:
        print (i)
    else:
        control = False
print ("los numeros primos entre el 1 al",numero, "son:",i )
'''

'''
numero = int(input("escriba un numero entero positivo: "))
for i in range(1,numero + 1):
    if i % 3 == 0:
        print ("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("frizzbuzz")
    else:
        print(i)
'''
'''
numero = int(input("escriba un numero entero positivo: "))
for i in range(1, numero +1):
    if i % 2 == 0:
        print(i)
'''

'''
nombre = str(input("escriba su nombre: "))
edad = int(input("ingrese su edad: "))

print(f"hola {nombre}, tienes {edad} años" )
'''

'''
suma = 0
for i in range (1, 101):
    suma += i
    print(suma)
'''
'''
numero = int(input("escribe un numero entero positivo: "))
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
'''

'''
numero = int(input("escriba un numero entero positivo: ))
for i in range (1,11):
    print(f"{i} x {numero} = {numero*i}")
'''

'''
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("es mayor de edad")
elif 0 < edad < 18:
    print("es menor de edad")
else:
    print("edad no valida")
'''

'''
numero = int(input("escriba un numero entero positivo: "))
factorial = 1
for i in range(1, numero +1 ):
    factorial = factorial * i
    print(f"el factorial del numero es {factorial}" )
'''

'''
frase = str(input("escriba una frase: "))
print(len(frase))
'''

'''
control = True
numero = int(input("escriba un numero entero positivo: "))
divisor = numero // 2 
cont = 0

while control == True:
    for i in range(2, divisor + 1):
        if numero % i == 0:
            cont+=1
    if cont == 0:
        print(f"{numero} es primo")
    else: 
        control=False
        print(f"{numero} no es primo")
'''

'''
numero = 10 
for i in range(1,11):
    print(i**2)
'''


'''
saldo = 1000
control = True

while control == True:
    print("1. consultar saldo\n2. despositar\n3. retirar\n4. salir")
    opcion = int(input("elija una opcion: "))
    match opcion:
        case 1:
            print(f"su saldo es de: {saldo}")
        case 2:
            deposito = int(input("ingrese el valor a depositar: "))
            saldo = saldo + deposito
        case 3: 
            retiro = int(input("ingrese el valor por retirar: "))
            saldo = saldo - retiro
        case 4: 
            control = False 
        case _:
            print("opcion no valida")
'''

'''
numero = int(input("ingrese un numero entero positivo: "))
suma = 0 
for i in range(1, numero +1): 
    if i % 2 == 0:
        suma = suma + i 
print(f"la suma de los numeros pares del 1 al {numero} es:{suma}")
'''

'''
palabra = str(input("escriba una palabra: "))
def es_palindromo(palabra):
    palabra_limpia = palabra.lower()
    return palabra_limpia == palabra_limpia [::-1]
print(f"{palabra} es un palíndromo: {es_palindromo(palabra)}")
'''

'''
numero = int(input("¿cuantos terminos fibonacci quieres?: "))
a , b = 0 , 1
for i in range(numero):
    print(a, end=" " )
    a , b = b , a + b 
'''
