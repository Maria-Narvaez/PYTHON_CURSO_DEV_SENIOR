"""Escribir un programa que almacene las asignaturas de un curso y en una lista, pregunte al usuario la nota 
que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir"""

def AsignaturasCurso(listaMaterias, notas):
    print("Asignaturas del curso: ")
    print(listaMaterias)
    
    for materia in listaMaterias:
        notaMateria = float(input(f"Por favor Ingrese la nota de la materia {materia}: "))
        notas.append(notaMateria)

#asignaturas aprobadas
def AsignaturasAprobadas(listaMaterias, notas):
    asignaturaAprobada = []
    for i in range(len(notas)):
        if notas[i] >= 3.0:
           asignaturaAprobada.append(listaMaterias[i])
     # eliminar aprobadas de la lista original
    for notaMateria in asignaturaAprobada:
        listaMaterias.remove(notaMateria)
    print("Asignaturas aprobadas eliminadas:", asignaturaAprobada)      
    
def AsignaturasaRepetir(listaMaterias):
    print(f"Estas son las asignaturas que el usuario debe REPETIR: {listaMaterias}")
    
def main():
    listaMaterias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    notas = []
    
    AsignaturasCurso(listaMaterias, notas)
    AsignaturasAprobadas(listaMaterias, notas)
    AsignaturasaRepetir(listaMaterias)

if __name__ == "__main__":
    main()
    
