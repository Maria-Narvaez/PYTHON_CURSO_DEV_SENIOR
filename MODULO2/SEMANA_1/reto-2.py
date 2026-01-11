from abc import ABC, abstractmethod

#Interfaz Movible
class Movible:
    def mover(self):
        pass
#Composición
class Motor:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def __str__(self):
        return f"Motor tipo {self.tipo}"


# clase abstracta
class Vehiculo(ABC, Movible):
    def __init__(self, placa: str, motor: Motor):
        self.placa = placa
        self.motor = motor
        self.conductor = None  #Agregación , no es obligatorio asignarlo

    def asignar_conductor(self, conductor):
        self.conductor = conductor

    @abstractmethod
    def iniciar_jornada(self):
        pass


# sub clases
class Moto(Vehiculo):
    def __init__(self, placa: str, motor: Motor, casco: bool):
        super().__init__(placa, motor)
        self.casco = casco

    def iniciar_jornada(self):
        if self.casco:
            print("La moto inicia jornada con casco obligatorio. ")
            print(f"Conductor:{self.conductor.nombre}, Documento:{self.conductor.documento}, Licencia:{self.conductor.licencia}")      
        else:
            print("No puede iniciar: casco obligatorio.")

    def mover(self):
        print("La moto está en movimiento.\n")


class Carro(Vehiculo):
    def __init__(self, placa: str, motor: Motor, revision_vigente: bool):
        super().__init__(placa, motor)
        self.revision_vigente = revision_vigente

    def iniciar_jornada(self):
        if self.revision_vigente:
            print("El carro inicia jornada con revisión vigente.")
            print(f"Conductor:{self.conductor.nombre}, Documento:{self.conductor.documento}, Licencia:{self.conductor.licencia}")
        else:
            print("No puede iniciar: revisión vencida.")

    def mover(self):
        print("El carro está en movimiento.\n")


class Camion(Vehiculo):
    def __init__(self, placa: str, motor: Motor, peso_carga: float):
        super().__init__(placa, motor)
        self.peso_carga = peso_carga
        self.peso_maximo = 20000

    def iniciar_jornada(self):
        if self.peso_carga <= self.peso_maximo:
            print("El camión inicia jornada con carga permitida.")
            print(f"Conductor:{self.conductor.nombre}, Documento:{self.conductor.documento}, Licencia:{self.conductor.licencia}")
        else:
            print("No puede iniciar: exceso de carga.")

    def mover(self):
        print("El camión está en movimiento.\n")


# conductor
class Conductor:
    def __init__(self, nombre: str, documento: str, licencia: str):
        self.nombre = nombre
        self.documento = documento
        self.licencia = licencia

    def __str__(self):
        return f"Conductor: {self.nombre}"
        

# programa principal
def main():
    conductor1 = Conductor("Carlos medina", "135754", "A2")
    conductor2 = Conductor("Marcos Tovar", "235788", "B2")
    conductor3 = Conductor("Jose Mendoza", "654321", "C3")

    motor_moto = Motor("Gasolina")
    motor_carro = Motor("Diesel")
    motor_camion = Motor("Diesel")

    moto = Moto("ABC123", motor_moto, casco=True)
    carro = Carro("DEF456", motor_carro, revision_vigente=True)
    camion = Camion("GHI789", motor_camion, peso_carga=9000)

    moto.asignar_conductor(conductor1)
    moto.iniciar_jornada()
    moto.mover()
    

    carro.asignar_conductor(conductor2)
    carro.iniciar_jornada()
    carro.mover()

    camion.asignar_conductor(conductor3)
    camion.iniciar_jornada()
    camion.mover()


main()