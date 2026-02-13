import os
os.system("cls")
alumnos=[]


while True:
    try:
        num=int(input("¿Cuantos alumnos quiere ingresar?"))
        break #si la conversacion es exitosa, salimos del bucle
    except ValueError:
        print("Error : por favor ingrese un numero entero valido.")

for i in range(num):
    nombre=(input("Nombre del alumno: "))
    edad=int(input("Edad del alumno: "))
    materia=(input("Materia del alumno: "))
    calif=float(input("Calificacion de la materia: "))
    
    alumno={
    "nombre": nombre,
    "edad": edad,
    "materia": materia,
    "calificacion": calif
    
} 
alumnos.append(alumno)

#Mostrar la cantidad de alumnos

os.system("cls")
print(f"Se ingresaron {len(alumnos)} alumnos.")

#Calcular el promedio de calificaciones

if alumnos:
    total_calificaciones=sum(alumno["calififcacion"] for alumno in alumnos)
    promedio=total_calificaciones/ len (alumnos)
    print(f"Promedio de calificaciones; {promedio}")
else:
    print("No se ingresaron calificaciones")
    
#Mostrar lista de calificaciones completa
print("Lista completa de alumnos")
for alumno in alumnos:
    print(alumno)