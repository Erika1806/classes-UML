class estudiante:
    def __init__(self, nombre, documento, carrera, nota):
        self.nombre = nombre
        self.documento = documento
        self.carrera = carrera
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Documento: {self.documento}, Carrera: {self.carrera}, Nota: {self.nota}")

Estudiante1 = estudiante("Juan", "123456789", "Ingeniería", 4.5)
Estudiante2 = estudiante("María", "987654321", "Medicina", 4.8)
print(Estudiante1.imprimir())
print(Estudiante2.imprimir())