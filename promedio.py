import os
os.system("cls")

prom=0
alumno1={
    "nombre": "",
    "edad": 0,
    "materia": "",
    "calificacion": 0
    
} 
ico201=[]

num=int(input("¿Cuantos alumnos quiere ingresar?"))

for i in range(num):
    nombre=(input("Nombre del alumno: "))
    edad=int(input("Edad del alumno: "))
    materia=(input("Materia del alumno: "))
    calif=float(input("Calificacion de la materia: "))
    
    prom=prom+calif
    
    alumno1["nombre"]=nombre
    alumno1["edad"]=edad
    alumno1["materia"]=materia
    alumno1["calificacion"]=calif
    
    ico201.append(alumno1.copy()) 
    
  
    
    
    
print("Lista de alumnos ingresados")

for alumno1 in ico201:
    print (alumno1)
    
print("Cantidad de alumnos ingresados: ",num)
print("El promedio de las calificaciones es: ",(prom/num))






