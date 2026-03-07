import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk


cine=tk.Tk()
cine.title("Cinepolis")
cine.geometry("1024x559")

def cerrar():
    respuesta=messagebox.askyesno("Salir","¿Desea cerrar la aplicacion?")
    if respuesta:
        cine.destroy()
        
        
def entradas():
    try:
        ing_nombre=nombre.get()
        num1=int(compradores.get())
        num2=tarjeta.get()
        num3=int(boletos.get())
        limite=num1*7
        precio=num3*12
        if not ing_nombre:
            messagebox.showerror("Error","Ingrese su nombre")
            return
        if num3>limite:
            messagebox.showerror("Error","No puede comprar mas de 7 boletos por persona")
            return
        elif num3>5:
            descuento=precio*0.15
            precio=precio-descuento
        elif num3==5 or num3>2:
            descuento=precio*0.10
            precio=precio-descuento
            
        if num2==1:
           descuento=precio*0.10
           precio=precio-descuento
        label_resultado.config(text=f"Valor a Pagar: {precio}")
    except ValueError:
        messagebox.showerror("Error","Porfavor ingrese numeros validos")
        return
           

       
imagen=Image.open("cinepolis.jpg")
fondo=ImageTk.PhotoImage(imagen)
label_fondo=tk.Label(cine,image=fondo)
label_fondo.place(x=0,y=0,relwidth=1,relheight=1)
  
frame_entradas=tk.LabelFrame(cine,text="Entrada",bg= "#0A1F59",fg="#FFFFFF",padx=10,pady=10) 
frame_entradas.place(x=60,y=300,width=350,height=150)

label_nombre=tk.Label(frame_entradas,text="Nombre:",bg="#0A1F59",fg="#FFFFFF")
label_nombre.grid(row=0,column=0)
nombre=tk.Entry(frame_entradas)
nombre.grid(row=0,column=2)

label_compradores=tk.Label(frame_entradas,text="Cantidad de  Compradores:",bg="#0A1F59",fg="#FFFFFF")
label_compradores.grid(row=1,column=0)
compradores=tk.Entry(frame_entradas)
compradores.grid(row=1,column=2)
 
tarjeta=tk.IntVar()
label_tarjeta=tk.Label(frame_entradas,text="Tarjeta Cineco:",bg="#0A1F59",fg="#FFFFFF")
label_tarjeta.grid(row=2,column=0)
tk.Radiobutton(frame_entradas,text="Si",variable=tarjeta,value=1,bg="#196380",fg="#000000").grid(row=2,column=2,sticky="W")
tk.Radiobutton(frame_entradas,text="No",variable=tarjeta,value=2,bg="#196380",fg="#000000").grid(row=2,column=2,sticky="E")

label_boletos=tk.Label(frame_entradas,text="Cantidad de Boletos:",bg="#0A1F59",fg="#FFFFFF")   
label_boletos.grid(row=3,column=0)
boletos=tk.Entry(frame_entradas)
boletos.grid(row=3,column=2)
                               
frame_salidas=tk.LabelFrame(cine,text="Salidas",bg= "#0A1F59",fg="#FFFFFF",padx=10,pady=10)
frame_salidas.place(x=700,y=300,width=250,height=100)

label_resultado=tk.Label(frame_salidas,text="Valor a Pagar:",bg="#0A1F59",fg="#FFFFFF",font=("Arial",12))  
label_resultado.grid(row=0,column=2,padx=45,pady=15)  
                              
  
frame_acciones=tk.LabelFrame(cine,text="Acciones",bg= "#0A1F59",fg="#FFFFFF",padx=10,pady=10)
frame_acciones.place(x=425,y=400,width=250,height=100)

boton_salir=tk.Button(frame_acciones,text="Salir",command=cerrar)
boton_salir.grid(row=0,column=4,padx=5,pady=15)

boton_proceso=tk.Button(frame_acciones,text="Procesar",command=entradas)
boton_proceso.grid(row=0,column=2,padx=50,pady=15)
   
   
cine.mainloop()  