import os,math
os.system("cls")


def cuadrado():
    os.system("cls")
    print("Area del Cuadrado")
    a=int(input("Ingrese el valor de un lado: "))
    c=a*a
    print ("El resultado es: ",c)
    input()

def rectangulo():
    os.system("cls")
    print("Area del Rectangulo")
    a=int(input("Ingrese el valor de la altura: "))
    b=int(input("Ingrese el valor de la base: "))
    c=a*b
    print ("El resultado es: ",c)
    input()

def triangulo():
    os.system("cls")
    print("Area del Triangulo")
    x=int(input("Ingrese el valor de la altura: "))
    y=int(input("Ingrese el valor de la base: "))
    mul=(x*y)/2
    print ("El resultado es: ",mul)
    input()

def circulo():
      os.system("cls")
      print("Area del Ciculo")
      x=float(input("Ingrese el valor del radio: "))
      mul=(math.pi)*(x**2)
      print ("El resultado es: ",mul)
      input()
      
def trapecio():
    os.system("cls")
    print("Area de Trapecio")
    x=int(input("Ingrese el valor de la base mayor: "))
    y=int(input("Ingrese el valor de la base menor: "))
    z=int(input("Ingrese el valor de la altura: "))
    area=((x+y)*z)/2
    print("El resultado es: ",area)
    input()
    
def menu():
    opcion=0
    while opcion !=6:
        os.system("cls")
        print("1-Cuadrado\n2-Rectangulo\n3-Triangulo\n4-Circulo\n5-Trapecio\n6-Salida\n")
        opcion=int(input("Seleccione una opcion: "))
        if opcion==6:
            print("Fin del programa")
            break
        if opcion==1:
            cuadrado()
        if opcion ==2:
            rectangulo()
        if opcion ==3:
            triangulo()
        if opcion ==4:
            circulo()
        if opcion==5:
            trapecio()

        
if __name__==("__main__"):
    menu()
    