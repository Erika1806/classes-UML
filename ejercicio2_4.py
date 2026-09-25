numero = int(input("Ingrese un número entero positivo: "))
primo = True
if numero <= 1:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
if primo:
    print("El número es primo.")
else:
    print("El número no es primo.")