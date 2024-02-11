#calculadora para saber la masa corporal (IMS)

#Herrramienta que permite calcular tu masa corporal es por ello que te pido que ingreses correctamente para que puedas avanzar

#preguntaremo su nombre 
nombre=input('Ingrese tu nombre ') 
while not nombre.isalpha(): #aqui es donde declaramos mientras no se detecte texto str no avanzara es decir si en la variable nombre solo lleva str avansa mientras no 
    print(' ERROR, el valor ingresado es incorrecto debe de ser tu nombre no se puede dejar el campo vasio ')
    nombre =input('Ingrese tu nombre correctamente ')
nombre =str(nombre)

priapellido=input('Ingrese tu primer apellido ') #pedimos el apellido al usuario
while not priapellido.isalpha():   # .isalpha se utiliza para string 
    print(' ERROR, el valor ingresado debe de ser tu primer apellido ')
    priapellido =input('Ingrese tu primer apellido  correctamente ')
priapellido =str(priapellido)

seapellido=input('Ingrese tu segundo apellido ') #pedimos el apellido al usuario
while not seapellido.isalpha():   # .isalpha se utiliza para string 
    print(' ERROR, el valor ingresado debe de ser tu segundo apellido ')
    seapellido =input('Ingrese tu segundo apellido  correctamente ')
seapellido =str(seapellido)

while True:
    try:
        edad = int(input("Escribe tu edad: "))
    except ValueError:
        print("Debes escribir en número.")
        continue

    if edad < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

while True:
    try:
        peso = float(input("ingresa tu peso en kiloramo: "))
    except ValueError:
        print("Debes escribir un número en kilogramos. ")
        continue

    if peso < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

while True:
    try:
        altura = float(input("ingresa tu altura en metros: "))
    except ValueError:
        print("Debes escribir un número en metros. ")
        continue

    if altura < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break
#esta es la formula par calcular la IMS 
ims=peso/altura**2

#ahora vamos a realizar distintas variaciones para hacre el calculo correspondiente 
print(f'Hola {nombre} {priapellido} {seapellido} tus resultados son los siguientes IMC :{ims}')


    #Hacemos las distintas validaciones
if ims >= 0 and ims <= 15.99 :
        print ("Delgadez severa")
elif ims >= 16.00 and ims <= 16.99 :
        print ("Delgadez moderada")
elif ims >= 17.00 and ims <= 18.49:
        print ("Delgadez leve")
elif ims >= 18.50 and ims <= 24.99 :
        print ("Normal")
elif ims >= 25.00 and ims <= 29.99:
        print ("Sobrepeso")
elif ims >= 30.00 and ims <= 34.99:
        print ("obesidad leve")
elif ims >= 35.00 and ims <= 39.00:
        print ("obesidad media")
elif ims >= 40.00:
        print ("obesidad morbida")