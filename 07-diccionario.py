"""¿Que es un diccionario?
un diccionario es una estructura de datos que almacena informacion pares clave-valor

no se accede por posicion, si no por clave 

Ejemplo:
alumno={
    "nombre": "Ana",
    "edad": 21,
    "carrera": "Ingieneria"
    
    }
"""
alumno={
    "nombre": "Ana",
    "edad": 21,
    "carrera": "Ingieneria"
    
}
print(type(alumno))
print(alumno)

print("print(alumno[´nombre´]) = " ,alumno["nombre"])
print("print(alumno.get(´edad´)) = ",alumno.get("edad"))

#Agregar o modificar valores
alumno["promedio"] =9.2
print(alumno)
alumno["edad"]=22
print(alumno)

#Eliminar un par clave-valor
del alumno["carrera"]
print(alumno)

#Recorrer un diccionario
for clave in alumno:
    print(clave)
    print(clave, ":" , alumno[clave])   



#funciones clave para un dicionario
print("Cantidad de pares clave-valor: ",len(alumno))
print("Claves del diccionario: ",alumno.keys())
print("Valores del diccionario: ",alumno.values())
print("Pares clave-valor: ",alumno.items())

###### Practica #######


alumno1={
    "nombre": "",
    "edad": 0,
    "carrera": ""
    
} 
ico201=[]

num=int(input("¿Cuantos alumnos quiere ingresar?"))

for i in range(1,num):
    nombre=(input("Nombre del alumno: "))
    edad=int(input("Edad del alumno: "))
    carrera=(input("Carrera del alumno: "))
    
    alumno1["nombre"]=nombre
    alumno1["edad"]=edad
    alumno1["carrera"]=carrera
    
    ico201.append(alumno1.copy())
    
print("Lista de alumnos ingresados")

for alumno1 in ico201:
    print (alumno1)