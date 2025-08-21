

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

#si imc < 18.48 condicion de peso bajo 
if imc < 18.49:
    mensaje = "condicion: peso bajo"
else: 
    if 18.5 < imc < 24.99:
        mensaje = "condicion peso normal"

#si imc es > 25 condicion sobrepeso
if 25 < imc < 29.9:
    mensaje = "condicion: sobrepeso"
else: 
   if 30 < imc < 39.9:
    mensaje = "condicion: obesidad"

#si imc es > 40 condicion obesidad extrema
if imc > 40:
    mensaje = "condicion: obesidad extrema"

print (mensaje)


        

