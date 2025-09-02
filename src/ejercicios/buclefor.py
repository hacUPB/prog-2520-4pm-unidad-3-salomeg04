'''
mensaje = "programacion con python"
numero = int(input("ingrese el numero: "))

for i in range(numero):
    print(f"{i+1}. {mensaje}")
'''
'''
numero = int(input("ingrese el numero entero positivo: "))
acumulador = 0 
for i in range(numero + 1):
    if i % 2 == 0:
        acumulador += i  #tipo de variable acumulador

print(f"la suma de los pares hasta {numero} es {acumulador}")
''' 

numero = int(input("ingrese el numero entero positivo: "))
for i in range (1, numero + 1):
    for j in range(1, i + 1):
      print(j,end=' ')
    print ()