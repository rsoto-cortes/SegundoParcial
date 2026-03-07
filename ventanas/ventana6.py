import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1= float(entrada1.get())
        num2=float(entrada2.get())
        operacion=opcion.get()
        
        if operacion==1:
            resultado=num1 + num2
        elif operacion==2:
            resultado=num1-num2
        elif operacion==3:
            resultado=num1*num2
        elif operacion==4:
            if num2==0:
                messagebox.showerror("error","No se puede dividir entre cero")
                return
            resultado=num1/num2
        else:
            messagebox.showwarning("Advertencia","Selecciona una operacion")
            return
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error","Por favor ingrese numeros validos")
        
        
ventana=tk.Tk()
ventana.title("Calculadora con radiobotones")
ventana.geometry("350x300")

#Entradas
tk.Label(ventana,text="Primer numero:").pack(pady=5)
entrada1=tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana,text="Segundo numero:").pack(pady=5)
entrada2=tk.Entry(ventana)
entrada2.pack()

#Variable para los radio botones
opcion=tk.IntVar()

tk.Label(ventana,text="Seleccione la operacion:").pack(pady=10)

tk.Radiobutton(ventana,text="Suma",variable=opcion,value=1).pack()
tk.Radiobutton(ventana,text="Resta",variable=opcion,value=2).pack()
tk.Radiobutton(ventana,text="Multiplicacion",variable=opcion,value=3).pack()
tk.Radiobutton(ventana,text="Divicion",variable=opcion,value=4).pack()

tk.Button(ventana,text="Calcular",command=calcular).pack(pady=10)

#Resultado
etiqueta_resultado=tk.Label(ventana,text="Resultado: ")
etiqueta_resultado.pack()


ventana.mainloop()



            