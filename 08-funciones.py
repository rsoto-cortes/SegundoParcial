"""
Las funciones en Python son bloques de codigo reutilizables que realizan una tarea especifica.
Sirven para organizar,reutilizar y hacer mas claro el codigo.

¿Para que sirven?

*Evitar repetir codigo.
*Permiten dividir un problema grande en partes pequeñas.
*Hacen el programa mas facil de mantener. 
*Mejoran la legibilidad

#En Python se define con la palabra clave def:
def nombre_funcion(parametros): 
    #bloque de codigo
    return valor
    
"""

def nombre():#Funcion que no resive nada ni regresa nada
    print("Hola Mundo!!")
    
nombre()

def suma():
    a=6
    print("Dentro de la funcion",a)
    b=7
    c=a+b
    
    return c


print("La suma es: ",suma())

a=3
print("Fuera de la funcion",a)
b=7
c=a+b


def multipilca(x,y):#Funcion que recibe parametros y da parametros
    
    return x*y

print ("La multiplicacion es: ",multipilca(a,b))

