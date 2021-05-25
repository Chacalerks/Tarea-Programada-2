#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

"""
Documentación IMPORTANTE:
+La interfaz del main no se cuentra una función y es por custiones de eficiencia y menos exigencia al procesador, ya que los frames no cambian solo el main 
    el top bar y el nav bar no cambia y volver a ejecutarlo en una función recursuva hace que se destruya y se vuelva a crear haciendo que el procesador 
    ejecute instrucciones inecesarias.
"""

from tkinter import PhotoImage
import tkinter as tk

from ingresar import*
from generar import*
from eliminar import*
from provincias import *
from about import *

from general import*
from funciones import *
from archivo import *
from validaciones import *
from reportes import *
matriz= []
matriz = leerDatos('datos')
dicc = leerDatos('provincias')

print(matriz)
print("\n\n")
print(dicc)

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
corazon_img = PhotoImage(file=".\iconos\cardiogram.png")
tk.Label(mainFrame, bg=color["principal"], text="",pady=25).pack(side="top")
corazon_lb = tk.Label(mainFrame, image=corazon_img, bd=0,bg=color["principal"])
corazon_lb.pack(side="top") 
tk.Label(mainFrame, text="Donar sangre, es donar vida", font="Bahnschrift 16", bg=color["principal"], fg="white", height=1, padx=20,pady=25).pack(side="top")


#Botones de navegación:
#Insertar
insertar_btn = tk.Button(navFrame, text="Insertar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:insertarDonadorES(mainFrame, corazon_img, matriz,[],"I",dicc))
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
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:insertarLugarES(mainFrame,corazon_img,dicc))
provincia_btn.place(x=50, y=400, width=200)

#Reportes
reportes_btn = tk.Button(navFrame, text="Reportes",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:menuReportes(mainFrame, corazon_img, matriz))
reportes_btn.place(x=50, y=480,width=200)

#Salir
salir_btn = tk.Button(navFrame, text="Salir",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=salir)
salir_btn.place(x=50, y=560,width=200)

#Acerca de 
acerca_btn = tk.Button(navFrame, text="Acerca de",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:about(mainFrame, corazon_img, matriz))
acerca_btn.place(x=50, y=800,width=200)

#Cargar Ventana:
root.mainloop()