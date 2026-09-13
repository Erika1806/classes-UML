class Libro:
    def __init__(self, titulo, autor, editorial, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.paginas = paginas

    def imprimir(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Editorial: {self.editorial}, Páginas: {self.paginas}")

Libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Editorial Sudamericana", 417)
Libro2 = Libro("1984", "George Orwell", "Editorial Seix Barral", 328)
print(Libro1.imprimir())
print(Libro2.imprimir())