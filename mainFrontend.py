from tkinter import PhotoImage
import tkinter as tk

from ingresar import*
from generar import*
from eliminar import*

from general import*

from funciones import *
from archivo import *
from validaciones import *
matriz= []
matriz = leerDatos('datos')
dicc = leerDatos('provincias')
print(matriz)
    
# diccionario de colores
color = {"fondo":"#F0F0F0", "sidebar":"#052744", "topbar":"#0D5D8C", "caja": "#BFBFBF" ,  "principal": "#043E79", "secundario": "#043E79","tercero":"#0E3D5E"}

#Configuaricón de la ventana
root = tk.Tk()
root.title("Sistema de donaciones")
root.geometry("1400x900+150+50")

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
insertar_btn = tk.Button(navFrame, text="Insertar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:insertarDonadorES(mainFrame, corazon_img, matriz))
insertar_btn.place(x=50, y=80, width=200)

#Generar
generar_btn = tk.Button(navFrame, text="Generar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5,command=lambda:generarDonadorES(mainFrame, corazon_img, matriz))
generar_btn.place(x=50, y=160, width=200)

#Actualizar
actualizar_btn = tk.Button(navFrame, text="Actualizar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:actulizarDonadorES(mainFrame, corazon_img, matriz))
actualizar_btn.place(x=50, y=240, width=200)

#Eliminar
eliminar_btn = tk.Button(navFrame, text="Eliminar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:eliminarES(mainFrame, corazon_img, matriz))
eliminar_btn.place(x=50, y=320, width=200)

#Provincia
provincia_btn = tk.Button(navFrame, text="Según Provincia",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:actulizarDonadorES(mainFrame, corazon_img, matriz))
provincia_btn.place(x=50, y=400, width=200)

#Reportes
reportes_btn = tk.Button(navFrame, text="Reportes",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:actulizarDonadorES(mainFrame, corazon_img, matriz))
reportes_btn.place(x=50, y=480, width=200)

#Cargar Ventana:
root.mainloop()