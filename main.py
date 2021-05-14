from os import truncate
from tkinter import IntVar, PhotoImage, StringVar
import tkinter as tk
from tkinter import ttk
from tkinter.constants import E, TRUE, W
# diccionario de colores
color = {"fondo":"#F0F0F0", "sidebar":"#052744", "topbar":"#0D5D8C", "caja": "#BFBFBF" ,  "principal": "#043E79", "secundario": "#043E79","tercero":"#0E3D5E"}

# configuaricón de la ventana
root = tk.Tk()
root.title("Sistema de donaciones")
root.geometry("1300x900+150+50")


# loading Navbar icon image:
insertar = PhotoImage(file="D:\TEC\I SEMESTRE\Intro-Taller (Laura)\Taller\Tareas\Tarea Programada 2\Tarea-Programada-2\iconos\m[as.png")
generar = PhotoImage(file="D:\TEC\I SEMESTRE\Intro-Taller (Laura)\Taller\Tareas\Tarea Programada 2\Tarea-Programada-2\iconos\menu.png")


# top Navigation bar:
topFrame = tk.Frame(root, bg=color["topbar"])
topFrame.pack(side="top", fill=tk.BOTH)
# Header label text:
titulo = tk.Label(topFrame, text="SISTEMA DE DONACIONES", font="Bahnschrift 15", bg=color["topbar"], fg="white", height=1, padx=20)
titulo.pack()


# setting Navbar frame:
navFrame = tk.Frame(root, bg=color["sidebar"], width=300)
navFrame.pack(side="left",fill=tk.BOTH)

corazon = PhotoImage(file="D:\TEC\I SEMESTRE\Intro-Taller (Laura)\Taller\Tareas\Tarea Programada 2\Tarea-Programada-2\iconos\cardiogram.png")
mainFrame = tk.Frame(root, bg=color["principal"])
mainFrame.pack(fill=tk.BOTH, expand=1)
navbarBtn = tk.Label(mainFrame, image=corazon, bd=0)
navbarBtn.pack(side="top")

def menu():
    limpiarFrame()
    navbarBtn = tk.Label(mainFrame, image=corazon, bd=0)
    navbarBtn.pack(side="top")

def limpiarFrame():
    for elemento in mainFrame.winfo_children():
        elemento.destroy()


def insertarDonadorES():
  limpiarFrame()
  grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
  grupo.pack(fill=tk.BOTH,expand=1)
  datos = []
  i=0
  while True:
    datos.append(StringVar())
    datos[i].set("")
    i+=1
    if i==8:
      break
  #Cédula
  tk.Label(grupo, text="Cédula: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=0, column=0, pady=10,padx=10,sticky=E)
  cedula_txt = tk.Entry(grupo,textvariable=datos[0], width=50)
  cedula_txt.grid(row=0, column=1, pady=10,padx=10)

  #Nombre completo
  tk.Label(grupo, text="Nombre completo: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10, sticky=E)
  nombreCompleto_txt = tk.Entry(grupo,textvariable=datos[1],width=50)
  nombreCompleto_txt.grid(row=1, column=1, pady=10,padx=10)

  #Fecha de Nacimiento
  tk.Label(grupo, text="Fecha de Nacimiento: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=2, column=0, pady=10,padx=10, sticky=E)
  fechaNacimiento_txt = tk.Entry(grupo,textvariable=datos[2],width=50)
  fechaNacimiento_txt.grid(row=2, column=1, pady=10,padx=10)

  #Tipo de Sangre
  tk.Label(grupo, text="Tipo de Sangre: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=3, column=0, pady=10,padx=10, sticky=E)
  tipoSangre_cbo = ttk.Combobox(grupo,textvariable=datos[3], width=47, state="readonly")
  tipoSangre_cbo['values']= ["O+","O-","A+","A-","B+","B-","AB+","AB-"]
  tipoSangre_cbo.grid(row=3, column=1, pady=10,padx=10)

  #Sexo
  datos[4].set("M")
  tk.Label(grupo, text="Sexo: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=4,rowspan=2,column=0, pady=10,padx=10, sticky=E)
  sexo_rb1 = ttk.Radiobutton(grupo,variable=datos[4], text="Masculino",value="M", width=45)
  sexo_rb2 = ttk.Radiobutton(grupo,variable=datos[4], text="Femenino",value="F", width=45)
  sexo_rb1.grid(row=4, column=1, pady=10,padx=10)
  sexo_rb2.grid(row=5, column=1, pady=10,padx=10)

  #Peso
  tk.Label(grupo, text="Peso: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=6, column=0, pady=10,padx=10, sticky=E)
  peso_txt = ttk.Entry(grupo,textvariable=datos[5], width=50)
  peso_txt.grid(row=6, column=1, pady=10,padx=10)

  #Teléfono
  tk.Label(grupo, text="Teléfono: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=7, column=0, pady=10,padx=10, sticky=E)
  telefono_txt = ttk.Entry(grupo,textvariable=datos[6], width=50)
  telefono_txt.grid(row=7, column=1, pady=10,padx=10)

  #Correo
  tk.Label(grupo, text="Correo: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=8, column=0, pady=10,padx=10, sticky=E)
  email_txt = ttk.Entry(grupo,textvariable=datos[7], width=50)
  email_txt.grid(row=8, column=1, pady=10,padx=10)

  Ingresar_btn = ttk.Button(grupo, text="Ingresar",width=70, padding=20, command=lambda:picha(datos))
  Ingresar_btn.grid(row=9, column=0, columnspan=2)

  regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0, width=50, padx=20, command=menu)
  regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=10,sticky=E)

def poner(cedula,nombre,fechaNacimiento,tipoSangre,sexo,peso,telefono,correo):
  """
  Funcionamiento: Limpia los campos del formulario.
  Entradas: Las variables que esta enlazadas alformulario
  Salidas: NA
  """
  cedula.set("")
  nombre.set("")
  fechaNacimiento.set("")
  tipoSangre.set("")
  sexo.set("")
  peso.set("")
  telefono.set("")
  correo.set("")
def picha(datos):
  print(datos)
  datosString = []
  i = 0
  while i<len(datos):
    datosString.append(datos[i].get())
    i+=1
  print(datosString)


def actualizarDonadorES():
    limpiarFrame()
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


button.pack()

root.mainloop()

# Truzz Blogg | Python + Tkinter | How to create a GUI
# How to create a registration form using Python + Tkinter

# Let's import tkinter 

#import tkinter as tk
 
# Manipulate data from registration fields 
def send_data():
  username_info = username.get()
  password_info = password.get()
  fullname_info = fullname.get()
  age_info = str(age.get())
  print(username_info,"\t", password_info,"\t", fullname_info,"\t", age_info)
 
#  Open and write data to a file
  file = open("user.txt", "a")
  file.write(username_info)
  file.write("\t")
  file.write(password_info)
  file.write("\t")
  file.write(fullname_info)
  file.write("\t")
  file.write(age_info)
  file.write("\t\n")
  file.close()
  print(" New user registered. Username: {} | FullName: {}   ".format(username_info, fullname_info))
 
#  Delete data from previous event
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  fullname_entry.delete(0, END)
  age_entry.delete(0, END)

# Create new instance - Class Tk()  
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Registration Form - Python + Tkinter")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Python Form | TRUZZ BLOGG", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
username_label = Label(text = "Username", bg = "#FFEEDD")
username_label.place(x = 22, y = 70)
password_label = Label(text = "Password", bg = "#FFEEDD")
password_label.place(x = 22, y = 130)
fullname_label = Label(text = "Fullname", bg = "#FFEEDD")
fullname_label.place(x = 22, y = 190)
age_label = Label(text = "Age", bg = "#FFEEDD")
age_label.place(x = 22, y = 250)
 
# Get and store data from users 
username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()
 
username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*")
fullname_entry = Entry(textvariable = fullname, width = "40")
age_entry = Entry(textvariable = age, width = "40")
 
username_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)
fullname_entry.place(x = 22, y = 220)
age_entry.place(x = 22, y = 280)
 
# Submit Button
submit_btn = Button(mywindow,text = "Submit Info", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 320)

mywindow.mainloop()"""