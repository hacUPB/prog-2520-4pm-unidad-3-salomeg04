

nombre = input ("Por favor ingrese su nombre:")
print (" Bienvenido ", nombre)

# calcular el indice de masa corporal:
# imc = peso / estatura**2

#leer estatura
estatura = input ("ingrese su estatura en metros:" )
estatura = float(estatura)
#leer peso
peso = input ("ingrese su peso en kilogramos:" )
peso = float(peso)
#calcular imc
imc = peso / estatura ** 2
#mostrar imc
print ("su imc - ", imc)

if imc < 18.5:
    mensaje= "bajo peso"
elif imc < 25:
    mensaje= "peso normal"
elif imc < 30:
    mensaje= "sobrepeso"
elif imc < 35:
    mensaje= "obesidad tipo 1"
elif imc < 40:
    mensaje= "obesidad tipo 2"
else:
    mensaje= "obesidad extrema"

print(f"{nombre}, su IMC es {imc:0.2f} y su condicion es {mensaje}")  



        

