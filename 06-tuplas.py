

tupla= (1,2,3,4,5,2,3,2)

print(type(tupla))
print(tupla)
print("El elemento de la tupla es: ",tupla[2])

for i in tupla:
    print(i)

print("La cantidad de elemntos en la tupla es: ",len(tupla))
print("La cantida de veces que se repite el numero 2 es: ",tupla.count(2))
print("El indice del numero 3 es: ",tupla.index(3))


#tupla.append(6) #Esto genera un error , ya que las tuplas son inmutables

datos=("Juan,20,True")
#tupla de un solo elemento
una_tupla=(5)
print(datos)
print(una_tupla)
