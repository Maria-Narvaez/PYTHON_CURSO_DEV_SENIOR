"""
SE REALIZA EJERCICIO QUE DEJO EL PROFESOR DE LA TUTORIA NUMERO1
Escribir un programa que almacene en una lista los siguientes precios 50,75,46,26,80,65,8,
y muestre por pantalla el menor y el mayor de los precios 
"""
"""#mi primera solucion 
def mostrar_lista(lista):
    print("Lista de precios de menor a mayor:")
    print(lista)

def ordenar_lista(lista):
    lista.sort()

def main():
    precios = [50, 75, 46, 26, 80, 65, 8]

    ordenar_lista(precios)
    mostrar_lista(precios)

if __name__ == "__main__":
    main()"""
"""
#Segunda solucion mas sencilla
print("LISTA DE PRECIOS DE MENOR A MAYOR")
def main():
    
    mostrarLista =[50,75,46,26,80,65,8]
    mostrarLista.sort()
    print(mostrarLista)
    
if __name__=="__main__":
    main()
"""




#EJERCICIOS PROPIOS PARA HACER EN CASA REPASAR

"""#dia1 ejercicio propio, crear 3 varibales y imprimirlas en una sola linea
nombre = "Maria"
edad = 22
ciudad ="Villavicencio"

print(nombre, edad, ciudad)

#dia2 ejercicio propio, crear una varibale de cada tipo y imprimir el valor y su tipo
edad = 22
pi = 3.131415
nombre = "MARIA C"
femenino = True

print(edad,type(edad))
print(pi, type(pi))
print(nombre, type(nombre))
print(femenino, type(femenino))

#dia3 ejercicio propio, crear una lista con 5 cosas que me gusten , imprimir la primera y la ultima

cosasQueMeGustan =["Manzana", "Conejos", "Arroz con pollo", "Jugar futbol", "Hacer peinados"]
print(f"COSA N1 QUE ME GUSTA: {cosasQueMeGustan [0]}, COSA N2 QUE ME GUSTA {cosasQueMeGustan [4]}")

#dia4 ejercicio, agregar 3 elementos eliminar 1 y imprimir la lista final

frutas=[]
#se agregan las frutas a la lista que se inica vacia
frutas.append("Manzana")
frutas.append("Uva")
frutas.append("cereza")
#se elimina la fruta de la lista
frutas.remove("Uva")
#se aplica el contador de las frutad disponibles
cantidad= len(frutas)
print(f"Se imprime la lista final: {frutas}, Cantidad de frutas: {cantidad}")

#Dia 5 ejercicio, imprime cada elemento de una lista usando for

lista=["Lapiz", "Borrador", "Crayon", "Lapicero", "Saca puntas"]
for mostarElemento in lista:
    print(mostarElemento)

#Dia 6 ejercicio, verifica si un elemento existe en la lista, este ejercicio va con el ejercicio 5

print(f"LISTA DE ELEMENTOS: {lista}")
encontrado= str(input("Digite el elemento que desea encontrar: ").strip().lower())
for mostrarElemento in lista:
    if mostrarElemento.lower() == encontrado:
        print(f"El elemento encontrado en la lista es: {mostrarElemento}")
        break
else:
    print("Elemento digitado NO ENCONTRADO")
 
#Dia 7 ejercicio, crea una lista de materia reprobadas usando append y remove

listaReprobadas = ["Ingles", "Español", "Contabilidad"]
aprobadas = []
while True:
    materia = str(input("Digite otra materia: "))
    if materia in listaReprobadas:
        print(f"La materia {materia} esta reprobada , sera eliminada\n")
        listaReprobadas.remove(materia)
        print(f"LISTA DE MATERIAS REPROBADAS: {listaReprobadas}")
        break
        
    else:
        aprobadas.append(materia)
        print(f"La materia {materia} fue aprobada\n")
        print(f"LISTA DE MATERIAS APROBADAS: {aprobadas}")
""" 

