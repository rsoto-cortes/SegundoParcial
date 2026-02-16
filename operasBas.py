import os
os.system("cls")


def suma():
    os.system("cls")
    print("Suma")
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: "))
    c=a+b
    print ("La suma es: ",c)
    input()

def resta():
    os.system("cls")
    print("Resta")
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: "))
    c=a-b
    print ("La resta es: ",c)
    input()

def mult():
    os.system("cls")
    print("Multiplicacion")
    x=int(input("Ingrese el primer valor: "))
    y=int(input("Ingrese el segundo valor: "))
    mul=x*y
    print ("la multiplicacion es: ",mul)
    input()

def div():
      os.system("cls")
      print("Divicion")
      x=int(input("Ingrese el primer valor: "))
      y=int(input("Ingrese el segundo valor: "))
      mul=x/y
      print ("La divicion es: ",mul)
      input()
      
opcion=0

while opcion !=5:
    os.system("cls")
    print("1-Suma\n2-Resta\n3-Multiplicacion\n4-Divicion\n5-Salir\n")
    opcion=int(input("Seleccione una opcion: "))
    if opcion==5:
        print("Fin del programa")
        break
    if opcion==1:
        suma()
    if opcion ==2:
        resta()
    if opcion ==3:
        mult()
    if opcion ==4:
        div()
                
                
                    