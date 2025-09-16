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


   


