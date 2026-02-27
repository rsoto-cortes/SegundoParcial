import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def suma():
    try:
        num1=float(entrada1.get())
        num2=float(entrada2.get())
        resultado=num1+num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error","Porfavor ingrese un numero valido")

ventana=tk.Tk()
ventana.title("Operaciones")
ventana.geometry("400x300")

tk.Label(ventana,text="num1: ",font=("Arial",16)).grid(row=0,column=0)
entrada1=tk.Entry(ventana)
entrada1.grid(row=0,column=1)

tk.Label(ventana,text="num2: ",font=("Arial",16)).grid(row=1,column=0)
entrada2=tk.Entry(ventana)
entrada2.grid(row=1,column=1)

boton=ttk.Button(ventana,text="Calcular",command=suma).grid(row=2,column=0)

etiqueta_resultado=tk.Label(ventana,text="Resultado: ")
etiqueta_resultado.grid(row=3,column=2)

ventana.mainloop()