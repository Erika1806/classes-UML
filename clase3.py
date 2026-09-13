class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}")

Persona1 = Persona("Juan", 25, "Calle 123, Bogota")
Persona2 = Persona("María", 30, "Avenida 456")
print(Persona1.imprimir())
print(Persona2.imprimir())
