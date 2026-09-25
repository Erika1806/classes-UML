class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def calcular_promedio(self):
        suma = sum(self.notas)
        promedio = suma / len(self.notas)
        return promedio
    def verificar_si_aprobado(self):
            promedio = self.calcular_promedio()
            if promedio >= 3.0:
                return True, "aprobado"
            else:
                return False, "reprobado"
lista_Estudiantes = []
E1 = Estudiante("Juan", [5, 3, 2])
E2 = Estudiante("Maria", [4, 4, 4])
lista_Estudiantes.append(E1)
lista_Estudiantes.append(E2)
for estudiante in lista_Estudiantes:
    print(f"El estudiante {estudiante.nombre} tiene un promedio de {estudiante.calcular_promedio():.2f} y está {estudiante.verificar_si_aprobado()[1]}.")