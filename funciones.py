from tkinter import PhotoImage, StringVar
import tkinter as tk

# diccionario de colores
color = {"fondo":"#F0F0F0", "sidebar":"#052744", "topbar":"#0D5D8C", "caja": "#BFBFBF" ,  "principal": "#043E79", "secundario": "#043E79","tercero":"#0E3D5E"}

# configuaricón de la ventana
root = tk.Tk()
root.title("Sistema de donaciones")
root.geometry("1800x900+50+50")


# loading Navbar icon image:
insertar = PhotoImage(file="D:\TEC\I SEMESTRE\Intro-Taller (Laura)\Taller\Tareas\Tarea Programada 2\Tarea-Programada-2\iconos\m[as.png")
generar = PhotoImage(file="D:\TEC\I SEMESTRE\Intro-Taller (Laura)\Taller\Tareas\Tarea Programada 2\Tarea-Programada-2\iconos\menu.png")


# top Navigation bar:
topFrame = tk.Frame(root, bg=color["topbar"])
topFrame.pack()
# Header label text:
titulo = tk.Label(topFrame, text="SISTEMA DE DONACIONES", font="Bahnschrift 15", fg="black", height=1, padx=20)
titulo.pack()


# setting Navbar frame:
navFrame = tk.Frame(root, bg=color["sidebar"], width=300)
navFrame.pack(side="left")

corazon = PhotoImage(file="D:\TEC\I SEMESTRE\Intro-Taller (Laura)\Taller\Tareas\Tarea Programada 2\Tarea-Programada-2\iconos\cardiogram.png")
mainFrame = tk.Frame(root, bg=color["principal"])
mainFrame.pack()


def menu():
    limpiarFrame()
    navbarBtn = tk.Label(mainFrame, image=corazon, bd=0)
    navbarBtn.pack(side="top")
def limpiarFrame():
    for elemento in mainFrame.winfo_children():
        elemento.destroy()


def insertarDonadorES():

    limpiarFrame()

    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=10)

    grupo.pack(side="left", fill=tk.BOTH)

    cedula = StringVar()
    tk.Label(grupo, text="Cédula",font="BahnschriftLight 12", bg=color["fondo"],width=10, fg="black").pack()
    cedula_txt = tk.Entry(grupo,textvariable=cedula, bg=color["caja"],bd=0, width=50)
    cedula_txt.pack()

    nombreCompleto = StringVar()


    regresar = tk.Button(mainFrame, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,height=2, padx=20, command=menu)
    regresar.pack(side="right")

    picha = cedula_txt.get()
    print(picha,nombreCompleto)

def poner(cedula,nombre):
  cedula.set("")
  nombre.set("")

def actualizarDonadorES():
    actualizarFrame = tk.Frame(root, bg=color["principal"],height= 1800,width=1500,padx= 30, pady=30)
    actualizarFrame.place(x=300, y=30)
    tk.Label(actualizarFrame, text="Cédula ionseral;ksdj",font="BahnschriftLight 12", bg=color["fondo"],width=10, fg="black").place(x=50,y=50)
    regresar = tk.Label(actualizarFrame, text="PasdfE", font="Bahnschrift 15", fg="gray17", height=2, padx=20)
    regresar.pack(side="right")


# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
opciones = ["Insertar", "Generar", "Actualizar datos", "Eliminar", "Insertar lugar","Reportes", "Salir"]
iconos = [insertar,generar ]
# Navbar Option Buttons:


insertarBtn = tk.Button(navFrame, text="Insertar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=insertarDonadorES)
insertarBtn.place(x=50, y=80, width=200)

GenerarBtn = tk.Button(navFrame, text="Generar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5)
GenerarBtn.place(x=50, y=160, width=200)

ActualizarBtn = tk.Button(navFrame, text="Actualizar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5, command=actualizarDonadorES)
ActualizarBtn.place(x=50, y=240, width=200)
"""
EliminarBtn = tk.Button(navRoot, text="Eliminar",font="BahnschriftLight 12", bg=color["principal"],fg="white", activebackground="white",\
activeforeground="black", bd=0, padx=60, pady=5)
EliminarBtn.place(x=55, y=360)


opcion = tk.IntVar()
opcion.get()
tk.Label(navFrame, text="Menú",font="BahnschriftLight 12", bg=color["sidebar"],width=27, fg="white",pady=15).pack(side="top")
for i in range(7):
    #tk.Button(navRoot,  image=iconos[0],bg=color["sidebar"], bd=0 ).place(x=25, y=y)
    tk.Button(navFrame,text=opciones[i],cursor="dot", font="BahnschriftLight 12", bg=color["principal"],width=20, fg="white", activebackground="white",activeforeground="black", bd=0, pady=5).place(x=25, y=y)
    y += 80
"""


# contenedor principal 




# window in mainloop:
root.mainloop()

"""
from tkinter import *



ventanaMain = Tk()
ventanaMain.geometry("650x550")
ventanaMain.title("Registration Form - Python + Tkinter")



barraMenu = Menu(ventanaMain)
barraMenu.add_command(label="Insertar Donador")
barraMenu.add_command(label="Generar  Donadores")
barraMenu.add_command(label="Actualizar datos del donador")
barraMenu.add_command(label="Eliminar donador")
barraMenu.add_command(label="Insertar lugar de donación según provincia")
barraMenu.add_command(label="Reportes")
barraMenu.add_command(label="Sa;or")


ventanaMain.config(menu=barraMenu)
ventanaMain.mainloop()


root = Tk()

e = Entry(root,width=50)
e.pack()
def picha(titulo): 
    
    my= Label(root, text=titulo +e.get())
    my.pack()

myLabel1 = Label(root, text="este es el seunndo label")
button = Button(root, text="Picha", command=picha)
"""