class Farmaceutico:
    def __init__(self, dni: str, nombre: str) -> None:
        self.dni = dni
        self.nombre = nombre
        if len(dni) != 8:
            raise ValueError("El dni es incorrecto")
        

    def mostrar_informacion(self) -> None:
        print("DNI: " + self.dni, end=', ')
        print("Nombre: " + self.nombre)

    def __repr__(self) -> str:
        return "dni: {}, nombre: {}".format(self.dni, self.nombre)