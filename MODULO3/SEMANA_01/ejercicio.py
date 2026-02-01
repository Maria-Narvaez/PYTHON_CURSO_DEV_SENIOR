"""
SE REALIZA EJERCICIO QUE DEJO EL PROFESOR DE LA TUTORIA NUMERO1
Escribir un programa que almacene en una lista los siguientes precios 50,75,46,26,80,65,8,
y muestre por pantalla el menor y el mayor de los precios 
"""
#mi primera solucion 
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
    main()
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