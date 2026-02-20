import os,math

class areas:
    a=0
    b=0
    c=0
    res=0
    def cuadrado(self):
        self.res=(self.a)**2
        return self.res
    
    def rectangulo(self):
        self.res=self.a*self.b
        return self.res
    
    def triangulo(self):
        self.res=(self.a*self.b)/2
        return self.res
    
    def circulo(self):
        self.res=(math.pi)*(self.a**2)
        return self.res
    
    def trapecio(self):
        self.res=((self.a+self.b)*self.c)/2
        return self.res
    
    def pedirNumeros(self,op):
        if op==1 or op==4:
            self.a=int(input("Ingrese lado/radio: "))
        elif op==2 or op==3:
            self.a=int(input("Ingrese base: "))
            self.b=int(input("Ingrese altura: "))
        elif op==5:
            self.a=int(input("Ingrese base mayor: "))
            self.b=int(input("Ingrese base menor: "))
            self.c=int(input("ingrese altura: "))
        
    def imprimir(self):
        print("El resultado es: ",self.res)
        
        
def main():
    obj=areas()
    op=0
    while op !=6:
        os.system("cls")
        print("1-Cuadrado\n2-Rectangulo\n3-Triangulo\n4-Circulo\n5-Trapecio\n6-Salir\n")
        op=int(input("Seleccione una opcion: "))
        if op ==1:
            os.system("cls")
            obj.pedirNumeros(op)
            obj.cuadrado()
            obj.imprimir()
            input()
        elif op ==2:
            os.system("cls")
            obj.pedirNumeros(op)
            obj.rectangulo()
            obj.imprimir()
            input()
        elif op ==3:
            os.system("cls")
            obj.pedirNumeros(op)
            obj.triangulo()
            obj.imprimir()
            input()
        elif op ==4:
            os.system("cls")
            obj.pedirNumeros(op)
            obj.circulo()
            obj.imprimir()
            input()
        elif op ==5:
            os.system("cls")
            obj.pedirNumeros(op)
            obj.trapecio()
            obj.imprimir()
            input()
        elif op ==6:
            os.system("cls")
            print("Fin del programa...")
              
if __name__=="__main__":
    main()         
