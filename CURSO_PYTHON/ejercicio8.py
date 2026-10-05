# Reto para estudiantes

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
calificacion1 = float(input("Ingresa tu primera calificación: "))
calificacion2 = float(input("Ingresa tu segunda calificación: "))
calificacion3 = float(input("Ingresa tu tercera calificacion: "))
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

print("Hola", nombre)
print("Tienes", edad, "años")
if promedio >= 71:
    print("Aprobado")
else:
    print("Reprobado")