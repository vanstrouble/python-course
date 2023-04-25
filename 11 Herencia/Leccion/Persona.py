class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f'Persona: {self.nombre}, {self.edad} años'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self) -> str:
        return f'{super().__str__()}, {self.sueldo} MXN'
