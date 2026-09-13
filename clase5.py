class Tienda:
    def __init__(self, nombre, ubicacion,propietario):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.propietario = propietario

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Ubicación: {self.ubicacion}, Propietario: {self.propietario}")

Tienda1 = Tienda("Tienda Las Palomas", "Barrio Porvenir", "Juan Pérez")
Tienda2 = Tienda("Tienda La esperanza", "Avenida Ecuador", "María García")
print(Tienda1.imprimir())
print(Tienda2.imprimir())
