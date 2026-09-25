class zapatos:
    def __init__(self, estilo, marca, talla, color):
        self.estilo = estilo   
        self.marca = marca
        self.talla = talla
        self.color = color

    def disponibilidad(self,cant):
        print(f"disponibles {cant} zapatos")
    def visualizar (self):
        print(f"Zapatos de la marca {self.marca}, talla {self.talla}, color {self.color}.")
Zapatos1=zapatos("deportivos", "Nike", 34, "blanco")
Zapatos2=zapatos("formales", "Adidas", 38, "negro")
Zapatos1.disponibilidad(50)
Zapatos2.disponibilidad(30)
Zapatos1.visualizar()
Zapatos2.visualizar()
