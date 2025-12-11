
"""
# Función sin parametros ni retorno
def saludar():
    print("Holaaaaaa parce... (pana)")

saludar()

def saludo():
    return "Holaaaaaa parce... (pana)"

print(saludo())

# Funciones con parametros
def saludotres(nombre):
    print(f"Como estas {nombre}")

saludotres("Luis Guillermo")
saludotres(3)

def suma(numeroUno: int, numeroDos: int) -> int:
    resultado = numeroUno + numeroDos
    print(f"El resultado de la suma de {numeroUno} + {numeroDos} es: {resultado}")

suma(5, 5)

# funciones con parametros con valores por defecto
def presentar_estudiante(nombre: str, carrera: str ="Ingeniería") -> str:
    print(f"Estudiante: {nombre} | Carrera: {carrera}")

presentar_estudiante("Camilo")
presentar_estudiante("Maryam", "Medicina")

# Funciones con efecto colateral
estudiantes =[]

def agregar_estudiante(nombre: str):
    estudiantes.append(nombre)
    
agregar_estudiante("Gilberto")
agregar_estudiante("Cristhian")
agregar_estudiante("Juan")
agregar_estudiante("Kevin")
agregar_estudiante("Melany")
agregar_estudiante("Oliver")
agregar_estudiante("Rigel")
print(estudiantes)
"""

###  **Ejercicios básicos con funciones `def`**
"""
1. **Suma de dos números**
   Crea una función que reciba dos números y retorne su suma.

#SOLUCION
def suma(numero1: int, numero2: int) -> int:
    resultado = numero1 + numero2
    print(f"LA SUMA DEL NUMERO {numero1} + {numero2} ES: {resultado}")
suma(2,5)
"""  


"""
2. **Número par o impar**
   Escribe una función que reciba un número y diga si es par o impar.

#SOLUCION1

def numeroParOImpar(numero: int) -> int:
        
    if numero % 2 ==0:
        print(f"EL NUMERO: {numero} ES PAR")
        
    else:
        print(f"EL NUMERO: {numero} ES IMPAR")
numeroParOImpar(7)

#SOLUCION2 , AQUI SOLICITO AL USUARIO EL NUMERO.

def numeroParOImpar_con_input():
    numero =int(input("Por favor, ingrese un numero: "))
    
    if numero % 2 ==0:
        print(f"EL NUMERO: {numero} ES PAR")
        
    else:
        print(f"EL NUMERO: {numero} ES IMPAR")
numeroParOImpar_con_input()
"""

   

"""
3. **Área de un triángulo**
   Pide base y altura y devuelve el área del triángulo.
   *(Fórmula: base × altura / 2)*

#SOLUCION 3
def area_triangulo_con_input():
    base = int(input("Por favor, ingrese la base de un triangulo: "))
    altura = int(input("Por favor, ingrese la altura de un triangulo: "))
    resultado = base * altura /2
    print(f"EL AREA DEL TRIANGULO ES: {resultado}")
area_triangulo_con_input()
"""

"""
4. **Saludo personalizado**
   Crea una función que reciba el nombre de una persona y devuelva un saludo como `"Hola, <nombre>!"`.

#SOLUCION 4

def saludo(nombre:str) -> str:
    print(f"Holaa {nombre}")
saludo("Maria")
#SOLUCION PIDIENDO AL USUARIO EL NOMBRE CON (INPUT)
def saludo_con_input():
    nombre = str(input("Por favor, ingrese su nombre: "))
    print(f"Holaa {nombre}")
saludo_con_input()
"""

"""
5. **Máximo de tres números**
   Define una función que reciba tres números y retorne el mayor.
#solucion
def maximo_numero(numero1: int = 0, numero2: int = 12, numero3: int =15):
    if numero1 >= numero2 and numero1 >= numero3:
        print(f"El número mayor es: {numero1}")
    elif numero2 >= numero1 and numero2 >= numero3:
        print(f"El número mayor es: {numero2}")
    else:
        print(f"El número mayor es: {numero3}")
maximo_numero()
"""
   

"""
6. **Contar vocales en una palabra**
   La función debe contar cuántas vocales hay en una cadena dada.

#SOLUCION6
def contar_vocal(palabra: str) -> str:
    vocales = ["a", "e", "i", "o", "u"]
    contador = 0
    encontrada =[]
    for cadena in palabra:
        if cadena in vocales:
            contador += 1
            encontrada.append(cadena)   
    print(f"Cantidad de vocales: {contador}")
    print(f"Vocales encontradas: {encontrada}")
                
contar_vocal("estudiante")
"""
"""
7. **Convertir grados Celsius a Fahrenheit**

#SOLUCION7
def grados_celsius_fahrenheit(celsius: float):
    convertir = celsius *9 /5+32
    print(f"GRADOS CONVERTIDOS: {convertir}")
    
grados_celsius_fahrenheit(30)
"""
"""
8. **Verificar si una palabra es palíndromo**
   Una función que determine si una palabra se lee igual al derecho y al revés.

#SOLUCION 8
def palabra_palindromo(palabra: str) -> str:
    palindromo = palabra[::-1] #aqui se invierte la palabra
    print(f"\nPalabra digitada: {palabra}")
    print(f"Palabra invertida: {palindromo}") #aquí muestra la palabra al revés
    if palabra == palindromo:
        print(f"Es palindromo\n")
    else:
        print(f"No es palindromo")
palabra_palindromo("correa")
palabra_palindromo("ojo")
palabra_palindromo("amor")
palabra_palindromo("ana")
palabra_palindromo("oso")
palabra_palindromo("esqueleto")
"""
"""
9. **Contar elementos pares en una lista**
   La función recibe una lista de números y devuelve cuántos son pares.

 #SOLUCION 9
def elementos_pares(numeros: list):
    lista_numeros=[]
    contador = 0
     
    for n in numeros:
        if n %2==0:
            contador += 1
            lista_numeros.append(n)
            
    print(f"Los numeros pares son: {lista_numeros}")
    print(f"Cantidad de números pares: {contador}")
    
elementos_pares([2,4,6,5,9,8,10,12])
 """
  

"""
10. **Calculadora básica**
    Crea una función que reciba dos números y una operación (`"suma"`, `"resta"`, `"multiplicación"`, `"división"`) y devuelva el resultado correspondiente.

#SOLUCION 10
def calculadora(numero1: float, numero2: float) -> None:

    print("\n\nMENU CALCULADORA")
    print("SUMA(+)\nRESTA(-)\nMULTIPLICACION(*)\nDIVISION (/)\n\n")
    
    operacion = input("Seleccione el signo de la operación: ")

    if operacion == "+":
        print(f"La suma es: {numero1 + numero2}")

    elif operacion == "-":
        print(f"La resta es: {numero1 - numero2}")

    elif operacion == "*":
        print(f"La multiplicación es: {numero1 * numero2}")

    elif operacion == "/":
        print(f"La división es: {numero1 / numero2}")

    else:
        print("Operación no válida")
        
calculadora(20, 15)
"""