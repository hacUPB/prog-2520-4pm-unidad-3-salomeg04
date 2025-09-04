'''
# import random 
from random import randint

#num_aleatorio = random.randint (0,50)
num_aleatorio = randint(1,100)
print(num_aleatorio)
'''
'''
from random import randint
#num_aleatorio = random.randint (0,100)
num_aleatorio = randint(1,100)
intentos = 0 
numero = -1            #obliga a entrar al while en la primera vez 

while numero != num_aleatorio:
    numero = int(input("adivina el numero oculto entre 1 y 100:"))
    intentos +=1
    if numero > num_aleatorio:
        print("el numero oculto es menor")
    elif numero < num_aleatorio:
        print("el numero oculto es mayor")
    else: 
        print("felicidades, lo adivinaste...")
'''


from random import randint
#num_aleatorio = random.randint (0,100)
num_aleatorio = randint(1,100)
intentos = 0 
#numero = -1            #obliga a entrar al while en la primera vez 
flag = True

while True: 
            numero = int(input("adivina el numero oculto entre 1 y 100:"))
            intentos +=1
            if numero > num_aleatorio:
                print("el numero oculto es menor")
            elif numero < num_aleatorio:
                print("el numero oculto es mayor")
            else: 
                print("felicidades, lo adivinaste...")
                break 