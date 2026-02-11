"""
carros = []
carros.append("ford")

print(carros)
carros.append("chevrolet")
print("carros")
carros.insert(0,"honda")
print(carros)
#insertar en posicion espesifica
carros.insert(2,"nissan")
print(carros)
print(len(carros))
carros.sort()
print(carros)
#ordenar de menor a mayor
carros.sort(reverse=True)
print(carros)

carros.reverse()
print(carros)


#Programa de promedio de notas con listas 
asignaturas = []
datos = []

asignaturas.append("matematicas")
print(asignaturas)
asignaturas.append("fisica")
print(asignaturas)
asignaturas.append("quimica")
print(asignaturas)
#entrada de datos 
for asig in asignaturas:
    notas = []
    print(f"ingrse 3 notas pa para la asignatura de {asig}")
    for i in range(3):
        nota=float(input(f"nota{i+1}: "))
        notas.append(nota)
    
    datos.append([asig,notas])

#calculo

finalistas = []

for item in datos:
    promedio = sum(item[1])/len(item[1])
    print(f"Promedio en {item[0]}: {promedio:.2f}")
    
    if promedio>7:
        finalistas.append([item[0], promedio])
        
def segundo_elemento(x):
    return x[1]

finalistas.sort(key=segundo_elemento,reverse=True)

#con lamda
#finalistas.sort(key=segundo_elemento,reverse=True)

print("\n == Asignatura destacada (promedio > 7) ordenadas:===")

for nombre,promedio in finalistas:
    print(f"{nombre:<12} -> {promedio:.2f}")

# for f in finalistas:
#     print(f"{f[0]}: {promedio:.2f}")


#SE ANIDAN 3 LISTAS EN UNA SOLA LISTA, utilizando el for each

"""
"""#EJERCICIOS DE PRACTICA
principal = [
    ["Maria","Kevin", "Marilet", "Dainer"],
    [22, 26, 46, 50],
    [2003, 1999, 1960,1975]
    ]
    
titulos=["NOMBRES: ", "EDADES: ", "AÑOS: " ]

#for para datos
for i in range(len(principal)):
    print(titulos[i], principal[i])
    
#ejercicio2
categorias = ["FRUTAS:", "PRECIOS:", "CANTIDADES:"]

datos = [
    ["Manzana", "Banano", "Fresa"],
    [2500, 1800, 3200],
    [5, 8, 3]
]
    
for i in range(len(categorias)):
    print(categorias[i], datos[i])
    
#ejercicio3

#listaFrutas[]
frutas=[]
precio=[]
cantidad=[]
lista=["Fruta N1: ", "Fruta N2: ", "Fruta N3: "]

for i in range(3):

    fruta = str(input(f"Ingrese el nombre de la {lista[i]} "))
    precios = float(input(f"Ingrese el precio de {lista[i]} "))
    cantidades = float(input(f"Ingrese la cantidad de {lista[i]} "))
    
    frutas.append(fruta)
    precio.append(precios)
    cantidad.append(cantidades)
for i in range (len(frutas)):
    print(f"{lista [i]} {frutas[i]}, Precio: {precio[i]}, cantidad: {cantidad[i]}")
   
    
#EJERCICIO: REGISTRO DE ESTUDIANTES
nombre =[]
nota =[]
edad=[]
lista = ["Estudiante N1: " , "Estudiante N2: " ,"Estudiante N3: "]

for i in range(3):
    
    nombres= str(input(f"Ingrese el nombre del {lista[i]}"))
    notas=float(input(f"Ingrese la nota del {lista[i]}"))
    edades=float(input(f"Ingrese la edad del {lista[i]}"))
    
    nombre.append(nombres)
    nota.append(notas)
    edad.append(edades)
    
for i in range(len(nombre)):
    print(f"{lista[i]} {nombre[i]}, Nota: {nota[i]}, Edad: {edad[i]}")
#calcular el promedio de las notas
suma_notas = 0

for n in nota:
    suma_notas += n

promedio = suma_notas / len(nota)
print(f"El promedio de las notas es: {promedio}")
 
#EJERCICIO CORTO: PROMEDIO DE 3 NÚMEROS
numeros =[]

for i in range(3):
    numero =int(input("Ingrese un numero: "))
    numeros.append(numero)
    resultado= sum(numeros)
promedio = resultado/ len(numeros)
print(f"El promedio de los 3 numeros es: {promedio}")
"""  
#EJERCICIO: PROMEDIO DE N NÚMEROS

numeros_ingresados=[]
numeros = int(input("Por favor digite cuantos numeros desea ingresar: "))
if numeros >0:
    print(" debe Digitar un numero positivo mayor a cer0")
else:
    for i in range(numeros):
        cantidad =int(input(f"Por favor digite el numero {i}: "))
        numeros_ingresados.append(cantidad)
    resultado = sum(numeros_ingresados)
    promedio = resultado/len(numeros_ingresados) 
    print(f"El promedio de los numeros {numeros_ingresados}, es: {promedio}")