class vehiculo:
    def __init__(self, tipo, color, marca):
        self.tipo = tipo
        self.color = color
        self.marca = marca
    def encender(self):
        print(f"ENCENDIDO.")
    def pitar(self):
        print(f"El vehiculo esta pitando piiiiiiiiiii")
    def apagar(self):
        print(f"APAGADO.")

MOTO1=vehiculo("moto", "roja", "Kawasaki")
CARRO1=vehiculo("carro", "negro", "Toyota")
BARCO=vehiculo("barco", "blanco", "Bmw")
print (MOTO1.encender())
print (CARRO1.encender())
print (BARCO.encender())
print(MOTO1.pitar())
print(CARRO1.pitar())
print(BARCO.pitar())
print(MOTO1.apagar())
print(CARRO1.apagar())
print(BARCO.apagar())