#print("Hola")
#print("Hola de nuevo")
#print("como estas")
#/////////////////////////////////
#MIERCOLES 22 OCTUBRE 2025

#OPERADORES RELACIONALES
variableX =5
variableY = 10

variableZ , variableW =8, 7

print(f" variableX == variableY: {variableX == variableY} ") #Respuesta logica true o false
print(f" variableZ != variableX: {variableZ != variableX} ")
print(f" variableY > variableW: {variableY > variableW} ")
print(f" variableX < variableW: {variableX < variableW} ")
print(f" variableW >= variableY: {variableW >= variableY} ")
print(f" variableZ <= variableW: {variableZ <= variableW} ")

"""
    OPERADORES LOGICOS

    AND, OR, NOT
    
    and = si tengo el viernes AND si tengo dinero = true
    or= si tengo el viernes OR si tengo dinero = true
    
"""
tiene_dinero = True
esta_libre = False

print(f"AND: {tiene_dinero and esta_libre}")
print(f"OR: {tiene_dinero or esta_libre}")
print(f"NOT: {not esta_libre}")

#1 EJERCICIO EN CLASE IMPRIMIR 3 CONSTANTES

camilo= 10
maria = 20
julia = 40

print(f"camilo tiene: {camilo} años ")
print(f"maria tiene: {maria } años ")
print(f"Julia tiene {julia} años")

#VALIDACION MANUAL

edad = input("ingrese un numero: ")

if edad.isdigit():
    edad=int(edad)
    print(f"La edad es valida: {edad}")
else:
    print("Error, por favor ingrese un numero entero positivo")
    
tiene_dinero = False
if tiene_dinero:
    print("salgamos el viernes")
else:
    print("Te deseo exitos")

#2 EJERCICIO EN CLASE DECLARAR 3 VARIABLES CON TRUE O FALSE 
#uso del condiconal SI  - De lo contrario -> if-else
Es_miercoles = True
Vivo_en_argentina = False
hablo_ingles = False

if Es_miercoles:
    print("Tenemos clase")     
else:
    print("Dia libre")
    
    
if Vivo_en_argentina:
    print("usted es de argentina")    
else:
    print("Error, No es valido")       
    
    
if hablo_ingles:
    print("Felicidades hablas ingles")  
else:
    print("el idioma valido para el ingreso es ingles")   
    
    
#3 EJERCICIO EN CLASE 
""" OPERADORES RELACIONALES

Enunciado:
Crea un programa en Python que solicite al usuario ingresar dos números y muestre en pantalla el 
resultado de las siguientes comparaciones:

Si el primer número es mayor que el segundo.

Si el primer número es menor que el segundo.

Si ambos números son iguales.

""" 
numero_uno = int(input("Ingrese un numero "))
numero_dos = int(input("Ingrese otro numero "))

if numero_uno > numero_dos:
    print(f"{numero_uno} es mayor que {numero_dos}")

if numero_uno < numero_dos:
    print(f"{numero_uno} es menor que {numero_dos}")
    
if numero_uno == numero_dos:
    print(f"{numero_uno} es igual a {numero_dos}")

#4 EJERCICIO EN CLASE     
"""""
EJERCICIOS

Ejercicio 1: Verificar mayoría de edad
1. Enunciado:
Pide la edad de una persona y muestra un mensaje si es mayor de edad (18 años o más).
2. Ejercicio 2: Determinar si un número es positivo
Enunciado:
Pide un número y muestra un mensaje si el número es positivo.

3. Ejercicio 3: Verificar rango de valores
Enunciado:
Pide un número y muestra un mensaje solo si está entre 10 y 50 (inclusive).
"""
#SOLUCION EJERCICIO1
edad = int((input("Digita tu edad: ")))

if edad >=18:
    print(f"Usted tiene {edad} años es mayor de edad")
else:
    print(f"Usted tiene {edad} años es menor de edad")

#SOLUCION EJERCICIO2
numero =int(input("Digite un numero: "))

if numero <0:
    print(f"El numero ingresado es negativo: {numero}")
else:
    print(f"El numero ingresado es positivo: {numero}")

#SOLUCION EJERCICIO3

numero_rango =int(input("Digite un numero: "))

if numero_rango ==10 or numero_rango ==50:
    print(f"El numero esta dentro del rango establecido {numero_rango}" )
else:
    print(f"Eror, el numero no esta dentro del rango establecido {numero_rango}")