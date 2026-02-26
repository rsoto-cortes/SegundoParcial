import tkinter as tk

#creamos la ventana principal
ventana=tk.Tk()

#le damos titulo a la ventana
ventana.title("Mi primera aplicacion")

#le damos un tamaño a la ventana
ventana.geometry("400x300")

#creamos una etiqueta
etiqueta=tk.Label(ventana, text="Hola Mundo",font=("Arial",16,"bold"))
etiqueta.pack(pady=20)

#mostramos la etiqueta en la ventana
ventana.mainloop()