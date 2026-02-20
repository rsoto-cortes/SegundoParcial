import os

class operasBas:
    n1=0
    n2=0
    res=0
    def suma(self):
        self.res=self.n1+self.n2
        return self.res
    
    def resta(self):
        self.res=self.n1-self.n2
        return self.res
    
    def mult(self):
        self.res=self.n1*self.n2
        return self.res
    
    def div(self):
        self.res=self.n1/self.n2
        return self.res
    
    
    def pedirNumeros(self):
        self.n1=int(input("n1: "))
        self.n2=int(input("n2: "))
        
    def imprimir(self):
        print("El resultado es: ",self.res)
 
 
def main():
    obj=operasBas()
    op=0
    while op !=5:
        os.system("cls")
        print("1-Suma\n2-Resta\n3-Multiplicacion\n4-Divicion\n5-Salir\n")
        op=int(input("Seleccione una opcion: "))
        if op ==1:
            obj.pedirNumeros()
            obj.suma()
            obj.imprimir()
            input
        if op ==2:
            obj.pedirNumeros()
            obj.resta()
            obj.imprimir()
            input
        if op ==3:
            obj.pedirNumeros()
            obj.mult()
            obj.imprimir()
            input
        if op ==4:
            obj.pedirNumeros()
            obj.div()
            obj.imprimir()
            input
        if op ==5:
            print("Fin del programa...")
            
         
       
 

if __name__=="__main__":
    main()