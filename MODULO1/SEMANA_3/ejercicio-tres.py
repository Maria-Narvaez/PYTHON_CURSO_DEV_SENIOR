"""
contador = 1

while contador <= 5:
    print("contandor", contador)
    contador +=1 #INCREMENTANDO LA VARIABLE EN LA UNIDAD
    
    print("Fin del ciclo")
   
   
#APLICACION QUE PERMITA SOLICITAR UNA PALABRA POR TECLADO Y ESCRIBIR "SALIR " PARA SALIR DE LA APP

palabra =""

while palabra != "salir":
    palabra = input("Por favor, ingrese una palabra (Salir... para finalizar)")
    print(f"Escribiste la palabra => {palabra}")
    
print("Programa finalizado...")

#MENU POR CONSOLA

opcion =""

print("************MENU POR CONSOLA*************")
print("Opcion 1: Saludar")
print("Opcion 2: Mensaje")
print("Opcion 3: Salir")

while True:
    opcion = input("Ingrese una opcion (1-3): ")
    if opcion == "1":
        print("Hola, como estas? ")
    elif opcion == "2":
        print("Que tengas feliz dia")
    elif opcion == "3":
        print("Saliendo de la aplicación")
        break

#SUMA ACUMULADA DE NUMEROS: SE SOLICITAN NUMERO AL USUARIO Y ACUMULA SU SUMA HASTA QUE ESCRIBA 0 LO SACA DEL CICLO.

suma = 0
numero = int(input("Ingrese un numero (0 para salir) "))

#el signo != , significa diferente a

while numero !=0:
    suma+= numero
    numero = int(input("Ingrese otro numero (0 para salir ) "))

print(f"La suma total es => {suma}")

#VALIDAR ENTRADA POSITIVA: Solicita un numero positivo, si el usuario ingresa un numero negativo, repite la solicitud

numero = int(input("Ingrese un numero positivo: "))

while numero < 0:
    print("EROR, Debes ingresar un numero positivo ")
    numero = int(input("Por favor , te solicito amablemente ingresar un numero positivo: ")) 
    
print(f"El numero ingresado es:  {numero}")
"""  


""" 
######################################################################################################
# For => Se utiliza para recorrer una secuencia como: lista, rangos de números o cadenas de caracteres

# Quiero hacer un ciclo For para que me imprima los números del 1 al 6

for numero in range (1, 7): # Se imprimiran los números de 1 al 6
    print(f"El número a imprimir es  {numero}")

# Ahora, quiero imprimir una lista (estructura de datos) de elementos

productos = ["Pan", "Huevo", "Harina", "Leche", "Queso"]

for producto in productos:
    print(f"El producto es => {producto}")

# El uso del "break" y el "continue" dentro del ciclo "For"
# break

for numero in range (1, 7): # Se imprime hasta el número 3 por el uso del BREAK
    if numero == 4:
        print("Se interrumpio el ciclo For para excluir numeros a partir del 4")
        break
    print(f"El número a imprimir es  {numero}")
    

for numero in range (1, 7): # Se salta la impresión del número 4 por el uso del CONTINUE
    if numero == 4:
        print("\n\n Por el uso de la PALABRA RESERVADA CONTINUE se salta la impresión del número 4\n\n")
        continue
    print(f"El número a imprimir es  {numero}")


for numero in range (1, 7, 2): # Se imprime los números desde el 1, con incremento de 2 hasta el 6
    print(f"El número a imprimir es  {numero}")


# Imprimir una cadena de caracteres (string => str) uno por uno. Ejemplo de caracteres: ú, R, s, !, "5", &...

cadena = input("Por favor, ingrese una cadena de caracteres: ")

for caracter in cadena:
    print(caracter)
"""  
#EJERCICIOS EN CLASE     
"""  
 
#1 Desarrolle una app en python que permita sumar los números de 1 al 100
for numero in range (1, 101):
    print(f"NUMERO:: {numero}")
print("\n\nFIN DEL PROGRAMA\n\n")
 """  
"""  
#2 Desarrolle una app en python que permita calcular el cuadrado de los números de 1 al 5

for numero in range (1, 6):
    
    while True:
        numero =int(input("Digite un número del 1 al 5 para calcular su cuadrado: "))
        
        if numero >=1 and numero <=5:
            print(f"EL CUADRADO DEL NUMERO: {numero} es: {numero*numero}")
            break
        else:
            print("ERROR, DIGITE UN NUMERO DEL 1 AL 5")
"""
"""
#3 Desarrolle una app en python que permita mostrar solo las vocales de una palabra

palabra = input("POR FAVOR INGRESE UNA PALABRA: ")
vocales = ["a", "e", "i", "o", "u"]
for caracter in palabra:
    if caracter in vocales:
        print(f"LAS VOCALES QUE INGRESO EN LA PALABRA SON => {caracter}") 
        
"""      
"""
#4 Desarrolle una app en python que permita imprimir la tabla de multiplicar de un número ingresado por teclado

numero = int(input("Digite un número para imprimir la tabla de multicar: "))
print(f"TABLA DE MULTIPLICAR DEL {numero} ")
for caracter in range (1,11):    
    tabla = numero* caracter
    print(f" {numero} * {caracter} = {tabla}")
    
"""
