from tkinter import PhotoImage
import tkinter as tk

from ingresar import*
from general import*

dicc= {}
datosCache = [] 

def impirmirDicc():
    print(datosCache)
    
# diccionario de colores
color = {"fondo":"#F0F0F0", "sidebar":"#052744", "topbar":"#0D5D8C", "caja": "#BFBFBF" ,  "principal": "#043E79", "secundario": "#043E79","tercero":"#0E3D5E"}

#Configuaricón de la ventana
root = tk.Tk()
root.title("Sistema de donaciones")
root.geometry("1300x900+150+50")

#Barra superior
topFrame = tk.Frame(root, bg=color["topbar"])
topFrame.pack(side="top", fill=tk.BOTH)

#Header
titulo = tk.Label(topFrame, text="SISTEMA DE DONACIONES", font="Bahnschrift 15", bg=color["topbar"], fg="white", height=1, padx=20)
titulo.pack()

#Panel de navegación:
navFrame = tk.Frame(root, bg=color["sidebar"], width=300)
navFrame.pack(side="left",fill=tk.BOTH)

#Panel Principal
mainFrame = tk.Frame(root, bg=color["principal"])
mainFrame.pack(fill=tk.BOTH, expand=1)

#Cargar el inicio
corazon_img = PhotoImage(file="D:\TEC\I SEMESTRE\Intro-Taller (Laura)\Taller\Tareas\Tarea Programada 2\Tarea-Programada-2\iconos\cardiogram.png")
corazon_lb = tk.Label(mainFrame, image=corazon_img, bd=0)
corazon_lb.pack(side="top") 

#Botones de navegación:
#Insertar
insertarBtn = tk.Button(navFrame, text="Insertar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:insertarDonadorES(mainFrame, corazon_img, dicc, datosCache))
insertarBtn.place(x=50, y=80, width=200)

#Generar
GenerarBtn = tk.Button(navFrame, text="Generar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5,command=impirmirDicc)
GenerarBtn.place(x=50, y=160, width=200)

#Actualizar
ActualizarBtn = tk.Button(navFrame, text="Actualizar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5)
ActualizarBtn.place(x=50, y=240, width=200)


#Cargar Ventana:
root.mainloop()