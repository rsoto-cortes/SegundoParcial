import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

calculadora=tk.Tk()
calculadora.title("Calculadora de Resistencias Electricas")
calculadora.geometry("300x650")

def calcular():
    def_color={"Negro":"#000000","Cafe":"#643303","Rojo":"#A80A0A","Naranja":"#EF5B00","Amarillo":"#FFB700","Verde":"#3DBD0E","Azul":"#0037FF","Morado":"#8C00FF","Gris":"#7C7777","Blanco":"#FFFFFF"}
    valor_colores={"Negro":0,"Cafe":1,"Rojo":2,"Naranja":3,"Amarillo":4,"Verde":5,"Azul":6,"Morado":7,"Gris":8,"Blanco":9}
    multiplicadores={"Negro":1,"Cafe":10,"Rojo":100,"Naranja":1000,"Amarillo":10000,"Verde":100000,"Azul":1000000,"Morado":10000000,"Gris":100000000,"Blanco":1000000000}
    try:
        num1=valor_colores[combo1.get()]
        num2=valor_colores[combo2.get()]
        mult=multiplicadores[combo3.get()]
        col1=def_color[combo1.get()]
        col2=def_color[combo2.get()]
        col3=def_color[combo3.get()]
        res=resis.get()
        numero_ohm=(num1*10+num2)
        valor_ohm=numero_ohm*mult

        y=0
        if y==0:
            label_coles1.config(text=f"{num1}",bg=f"{col1}",fg="#FFFFFF")
            label_coles2.config(text=f"{num2}",bg=f"{col2}",fg="#FFFFFF")
            label_coles3.config(text=f"{mult}",bg=f"{col3}",fg="#FFFFFF")
            y=+1
        
        if col1=="#FFFFFF":
            label_coles1.config(fg="#000000")
        if col2=="#FFFFFF":
            label_coles2.config(fg="#000000")
        if col3=="#FFFFFF":
            label_coles3.config(fg="#000000")
            
        if res==1:
            resistencia=valor_ohm*0.05
            valor_max=valor_ohm+resistencia
            valor_min=valor_ohm-resistencia
            label_minimo.config(text=f"Valor Minimo: {valor_min}")
            label_maximo.config(text=f"Valor Maximo: {valor_max}")
            label_ohm.config(text=f"Valor de Ohm: {valor_ohm}")
            label_tolesc.config(text="5%",bg="#A07838",fg="#FFFFFF")
        elif res==2:
            resistencia=valor_ohm*0.10
            valor_max=valor_ohm+resistencia
            valor_min=valor_ohm-resistencia
            label_minimo.config(text=f"Valor Minimo: {valor_min}")
            label_maximo.config(text=f"Valor Maximo: {valor_max}")
            label_ohm.config(text=f"Valor de Ohm: {valor_ohm}")
            label_tolesc.config(text="10%",bg="#938F8F" ,fg="#FFFFFF")
        
        if res==0:
            messagebox.showerror("Error","Seleccione una tolerancia")
            
    except KeyError:
        messagebox.showerror("Error","Seleccione los colores") 
        return  

fondo=tk.Label(calculadora,text="",bg="#0C47A6")
fondo.place(x=0,y=0,height=650,width=300)

imagen=Image.open("Resistencias.jpg")
imag=ImageTk.PhotoImage(imagen)
label_imagen=tk.Label(calculadora,image=imag)
label_imagen.place(x=25,y=60)

titulo=tk.Label(calculadora,text="Calcular Valor de Resistencia",bg="#0F9A62",font=("Arial",14),fg="#FFFFFF")
titulo.place(x=25,y=25)

colores=("Negro","Cafe","Rojo","Naranja","Amarillo","Verde","Azul","Morado","Gris","Blanco")
    
combo1=ttk.Combobox(calculadora,values=colores)
combo1.place(x=25,y=330)
label_coles1=tk.Label(calculadora,text="",bg="#0C47A6")
label_coles1.place(x=215,y=330,height=23,width=75)

combo2=ttk.Combobox(calculadora,values=colores)
combo2.place(x=25,y=370)
label_coles2=tk.Label(calculadora,text="",bg="#0C47A6")
label_coles2.place(x=215,y=370,height=23,width=75)

combo3=ttk.Combobox(calculadora,values=colores)
combo3.place(x=25,y=410)
label_coles3=tk.Label(calculadora,text="",bg="#0C47A6")
label_coles3.place(x=215,y=410,height=23,width=75)

label_tolerancia=tk.Label(calculadora,text="Tolerancia",bg="#0C47A6",fg="#FFFFFF")
label_tolerancia.place(x=25,y=440)

resis=tk.IntVar()
tk.Radiobutton(calculadora,text="Dorado",variable=resis,value=1,bg="#0C47A6",).place(x=25,y=470)     
tk.Radiobutton(calculadora,text="Plateado",variable=resis,value=2,bg="#0C47A6",).place(x=25,y=500)

label_tolesc=tk.Label(calculadora,text="",bg="#0C47A6")
label_tolesc.place(x=215,y=475,height=23,width=75)

boton_calcular=tk.Button(calculadora,text="Calcular",command=calcular)
boton_calcular.place(x=120,y=530)

label_ohm=tk.Label(calculadora,text="Valor de Ohm:",bg="#0C47A6")
label_ohm.place(x=100,y=560)

label_maximo=tk.Label(calculadora,text="Valor Maximo:",bg="#0C47A6")
label_maximo.place(x=100,y=590)

label_minimo=tk.Label(calculadora,text="Valor Minimo:",bg="#0C47A6")
label_minimo.place(x=100,y=620)

calculadora.mainloop()
