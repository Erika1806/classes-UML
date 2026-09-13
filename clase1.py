class Producto:
    def __init__(self, nombre, descripcion, precio, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def imprimir(self):
        print(f"Nombre: {self.nombre}, descripcion: {self.descripcion}, precio: {self.precio}, cantidad: {self.cantidad}")

Producto1 = Producto("COCA COLA", "BEBiDA", "5.000", "10")
Producto2 = Producto("Helado", "comida", "4.500", "4")
print(Producto1.imprimir())
print(Producto2.imprimir())