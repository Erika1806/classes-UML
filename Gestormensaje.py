class mensaje:
    def __init__(self, remitente, destinatario, contenido):
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido
    def mostrar_mensaje(self):
        print(f"De:{self.remitente}")
        print(f"Para:{self.destinatario}")
        print(f"mensaje:{self.contenido}")
lista_mensajes=[]
opcion=""
while opcion != "3":
    print("==Menu==")
    print("1. Desea enviar un mensaje")
    print("2. Buscar mensajes")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print ("==Enviar mensaje==")
        remitente = input("Ingrese el remitente: ")
        destinatario = input("Ingrese el destinatario: ")
        contenido = input("Ingrese el contenido del mensaje: ")
        nuevo_mensaje = mensaje(remitente, destinatario, contenido)
        lista_mensajes.append(nuevo_mensaje)
        print("Mensaje creado con exito.")
    elif opcion == "2":
        print ("[Buscar mensaje por remitente]")
        busqueda = input("escriba el nombre del remitente a buscar: ")
        print(f"resultados para la busqueda de {busqueda}:")
        encontrados =False
        for msg in lista_mensajes:
            if msg.remitente.lower() == busqueda.lower():
                msg.mostrar_mensaje()
                encontrados = True

        if not encontrados:
            print(f"No se encontraron mensajes para mostrar la busqueda por  {busqueda}.")
    elif opcion == "3":
        print("Saliendo del sistema de gestión de mensajes.")
    else:
        print("Opción no válida. Por favor, intente nuevamente.") 
        print("--------------------")