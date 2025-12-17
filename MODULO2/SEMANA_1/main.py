"""
from dataclasses import dataclass

@dataclass
class Libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._titulo = valor
        else:
            raise ValueError("El título debe ser un texto válido")
    
    @property
    def autor(self) -> str:
        return self._autor
    
    @autor.setter
    def autor(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._autor = valor
        else:
            raise ValueError("El autor debe ser un texto válido")
    
    @property
    def isbn(self) -> str: # 9785.123.457-1
        return self._isbn
    
    @isbn.setter
    def isbn(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._isbn = valor
        else:
            raise ValueError("El ISBN debe ser un texto válido")
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, valor: float) -> None:
        if isinstance(valor, float) and valor > 0:
            self._precio = valor
        else:
            raise ValueError("El Precio debe ser un número entero o c/decimales")
    
    def __repr__(self) -> str:
        return(
            f"Libro(titulo='{self._titulo}', autor='{self._autor}', "
            f"ISBN='{self._isbn}', precio='{self._precio}')"
        )
    
def main() -> None:
    libro = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "321-456-987-1", 100000.00)
    
    print("\n*** Información del Libro ***\n")
    
    print(libro)
    libro.precio = 185500.00
    libro.titulo = "100 años de soledad"
    
    print("\n*** Datos de Libro actualizados ***\n")
    print(libro)
    
    print("\n<< Programa finalizado >>>\n")
    
if __name__ == "__main__":
    main()
    
    """
#EJERCICIO EN CLASE

from dataclasses import dataclass

@dataclass
class ProductoIndustrial:
    _nombre: str
    _categoria: str
    _codigoInterno: int
    _precioUnitario: float
    _cantidadInventario: float
    
    #aquí aplicamos encapsulamiento a cada atributo que protegemos usando @property y @setter.
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, nuevoNombre: str) -> None:
        if isinstance(nuevoNombre, str) and nuevoNombre.strip():
            self._nombre = nuevoNombre
        else:
            raise ValueError("El nombre digitado debe ser un texto válido")
        
    @property
    def categoria(self) -> str:
        return self._categoria
    @categoria.setter
    def categoria(self, nuevaCategoria: str)-> None:
        if isinstance(nuevaCategoria, str) and nuevaCategoria.strip():
            self._categoria = nuevaCategoria
        else:
            raise ValueError("La categoria digitada debe ser un texto valido")
    
    @property
    def codigoInterno(self) -> int:
        return self._codigoInterno
    
    @codigoInterno.setter
    def codigoInterno(self, codigoInternoNuevo: int) -> None:
        if isinstance(codigoInternoNuevo, int) and codigoInternoNuevo > 0:
            self._codigoInterno = codigoInternoNuevo
        else:
            raise ValueError("El codigo interno debe ser un número entero")
    
    @property
    def precioUnitario(self) -> float:
        return self._precioUnitario
    
    @precioUnitario.setter
    def precioUnitario(self, precioUnitarioNuevo: float) -> None:
        if isinstance(precioUnitarioNuevo, float) and precioUnitarioNuevo > 0:
            self._precioUnitario = precioUnitarioNuevo
        else:
            raise ValueError("El precio Unitario debe ser un numero entero o decimal")
        
    @property
    def cantidadInventario(self) -> float:
        return self._cantidadInventario
    
    @cantidadInventario.setter
    def cantidadInventario(self, cantidadInventarioNuevo: float) -> None:
        if isinstance (cantidadInventarioNuevo, float) and cantidadInventarioNuevo > 0:
            self._cantidadInventario = cantidadInventarioNuevo
        else:
            raise ValueError("La cantidad de inventario debe ser un numero entero o decimal")
        
    #aqui aplicamos el método de representación del objeto   
    def __str__(self) -> str:
        return (
        "Producto Industrial\n"
        f"Nombre: {self._nombre}\n"
        f"Categoría: {self._categoria}\n"
        f"Código Interno: {self._codigoInterno}\n"
        f"Precio Unitario: ${self._precioUnitario}\n"
        f"Cantidad en Inventario: {self._cantidadInventario}"
    ) 
    """
    #aqui mostramos el objeto de una manera tecnica
    def __repr__(self) -> str:
        return(
            f"ProductoIndustrial(nombre = '{self._nombre}', categoria='{self._categoria}', "
            f"codigoInterno='{self._codigoInterno}', precioUnitario='{self._precioUnitario}', cantidadInventario='{self._cantidadInventario}' )"
        )
    """
def main() -> None:
    productoIndustrial1 = ProductoIndustrial("Maquinaria pesada", "Movimiento de tierras", 10, 500.899, 20)
    
    print("\n*** Información del Producto Industrial ***\n")
    
    print(productoIndustrial1)
    productoIndustrial1.nombre = "Cemento"
    productoIndustrial1.categoria = "Ferreteria"
    productoIndustrial1.codigoInterno = 20
    productoIndustrial1.precioUnitario = 45.509
    productoIndustrial1.cantidadInventario = 20.999
    
    print("\n*** Datos del Producto Industrial actualizados ***\n")
    print(productoIndustrial1)
    
    print("\n<< Programa finalizado >>>\n")
    
if __name__ == "__main__":
    main()
        
        