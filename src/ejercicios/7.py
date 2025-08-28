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

