"""
    
Clasificador de temperatura:
Necesitamos desarrollar un programa que solicite al usuario una temperatura (en grados Celsius) y mostrar un mensaje dependiendo del rango:

* Menor a 0 → "Hace mucho frío"
* Entre 0 y 20 → "Clima templadito"
* Entre 21 y 30 → "Clima agradable"
* Mayor a 30 → "Terrible"

"""
temperatura =int(input("Por favor, ingrese la temperatura: "))

if temperatura <0:
    print("Hace mucho frio")
elif temperatura <=20:
    print("Clima templadito")
elif temperatura <=30:
    print("Clima agradable")
else:
    print("Clima terrible...")
    
#Programa que permite validar si una persona es mayor de edad o no

edad =int(input("Por favor ingrese su edad: "))

if edad <18:
    print("Sumerce es menor de edad")
else:
    print("Sumerce es mayor de edad")
    
    
"""
Ejercicios:

1. Número positivo, negativo o cero

Descripción: Solicitar un número e indicar si es positivo, negativo o cero.

2. Clasificador de notas

Descripción: El usuario ingresa una nota de 0 a 100. Mostrar el nivel académico según el puntaje.

| Rango  | Mensaje   |
| ------ | ----------|
| 90–100 | Excelente |
| 70–89  | Aprobado  |
| 0–69   | Reprobado |


3. Clasificador de edad

Descripción: Pedir la edad del usuario y clasificarla en rangos.

| Rango | Mensaje      |
| ----- | ------------ |
| 0–12  | Niño         |
| 13–17 | Adolescente  |
| 18–59 | Adulto       |
| 60+   | Adulto mayor |


5. Verificar hora del día

Descripción: Pedir la hora (0 a 23) e indicar si es mañana, tarde o noche.
"""
#SOLUCION EJERCICIOS
#SOLUCION EJERCICIO 1
numero= int(input("Por favor, Digite un numero"))

if numero >0:
    print("El numero digitado es positivo")
elif numero <0:
    print("El numero digitado es negativo")
elif numero ==0:
    print(f"El numero digitado es {numero}")

#SOLUCION EJERCICIO 2
nota =int(input("Por favor, digite su nota: "))

if nota  >=90 or nota ==100:
    print("Excelente")
elif nota >=70 or nota == 89:
    print("Aprobado")
elif nota >=0 or nota ==69:
    print("Reprobado")    
    
#SOLUCION EJERCICO 3
rango=int(input("por favor, ingrese su edad: "))

if rango >=0 and rango <=12:
    print("Es un niño")
elif rango >=13 and rango<=17:
    print("Es un adolescente")
elif rango>=18 and rango <=59:
    print("Es un adulto")
elif rango >=60:
    print("Es un adulto mayor")
    
#SOLUCION EJERCICIO 4
"""
5. Verificar hora del día

Descripción: Pedir la hora (0 a 23) e indicar si es mañana, tarde o noche.

"""
hora =int(input("Por favor, digite la hora del dia: "))

if hora >=0 and hora <=12:
    print("Es de mañana")
elif hora >=13 and hora <=16:
    print("Es de tarde ")
elif hora >=17 and hora <=23:
    print("Es de noche ")
elif hora  >=24:
    print("no es valido el formato de hora")