

class persona: 
    
    def inicializar(self,nom):
        self.nombre=nom
    
    
    def imprimir(self):
        print("Nombre",self.nombre)



#Bloque principal

persona1=persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=persona()
persona2.inicializar("Carla")
persona2.imprimir()



