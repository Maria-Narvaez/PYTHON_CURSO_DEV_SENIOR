"""TOTORIA4.
PROGRAMA COMPLETO DE CONSULTA DE PRODUCTOS POR NOMBRE O CODIGO, TRAER EL PRECIO Y LAS UNIDADES SI LAS UND SON 0 QUE DIGA NO HAY UNIDADES EN EXISTENCIA.
debe permitir modificar el producto, debe mostrar el precio de cada compra  y mostrar que compro con la suma total, con las unidades que se compraron, trabajando funciones condicionales listas. que la impresión en pantalla de la  factura se vea bonito
"""
"""Mini reto (nivel intermedio)
Crea un programa que:
Pida el nombre de un estudiante
Pida 3 materias y sus notas
Guarde todo en un diccionario
Muestre:
El diccionario completo
El promedio de las notas"""

dic_persona = {}

nombre= str(input("Por favor digite el nombre del estudiante: "))
for i in range(3):
    materia_estudiante= str(input("Digite el nombre de la materia: "))
    nota_estudiante= float(input("Digite la nota: "))
    dic_persona[materia_estudiante] = nota_estudiante
    
print("\nDatos del estudiante")
print("--------------------")
print(f"Nombre del estudiante: {nombre}")
for materia_estudiante, nota_estudiante in dic_persona.items():
    print(f"Materia: {materia_estudiante} - Nota: {nota_estudiante}")
#Calcula el promedio de las notas
suma = sum(dic_persona.values())
promedio = suma / len(dic_persona)
print(f"Promedio total de notas: {promedio}")