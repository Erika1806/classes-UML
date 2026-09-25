notas=[4,3,4]  
notas.pop(-1)
notas.append(4)
estudiantes=["carlos","lucia","juan","marcos"]
estudiantes.remove("lucia")
suma=0
for nota in notas:
    suma=suma+nota 
    print (nota)
for estudiante in estudiantes:
    print(estudiante)
promedio=suma/(len (notas))
print(suma)
print(promedio)