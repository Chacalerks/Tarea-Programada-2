#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización: 06/05/2021 09:48 p.m.
#Última modificación: 13/05/2021 1:00  p.m.
#Versión: 3.9.5

import tkinter as tk
from tkinter import ttk
from tkinter.constants import E
from general import *
from validaciones import *

def insertarDonadorES(mainFrame,corazon_img,dicc,datosCache):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario insertar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)
    datos = establecerDatos(datosCache)
    #Cédula
    tk.Label(grupo, text="Cédula: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=0, column=0, pady=10,padx=10,sticky=E)
    cedula_txt = ttk.Entry(grupo,textvariable=datos[0], width=50)
    cedula_txt.grid(row=0, column=1, pady=10,padx=10)

    #Nombre completo
    tk.Label(grupo, text="Nombre completo: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10, sticky=E)
    nombreCompleto_txt = ttk.Entry(grupo,textvariable=datos[1],width=50)
    nombreCompleto_txt.grid(row=1, column=1, pady=10,padx=10)

    #Fecha de Nacimiento
    tk.Label(grupo, text="Fecha de Nacimiento: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=2, column=0, pady=10,padx=10, sticky=E)
    fechaNacimiento_txt = ttk.Entry(grupo,textvariable=datos[2],width=50)
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

    Ingresar_btn = ttk.Button(grupo, text="Registrar",width=70, padding=20, command=lambda:ingresarValidaciones(datos,dicc))
    Ingresar_btn.grid(row=9, column=0, columnspan=2)

    limpiar_btn = ttk.Button(grupo, text="Limpiar",width=70, padding=20, command=lambda:limpiarCampos(datosCache,datos))
    limpiar_btn.grid(row=10, column=0, columnspan=2)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0, width=50, padx=20,command=lambda:cargarInicio(mainFrame,corazon_img,datosCache,datos))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10, padx=10, sticky=E)

def ingresarValidaciones(datos,dicc):
    datosString=obtenerDatos(datos)
    if validarCedula(datosString[0]):
        if validarFecha(datosString[2]):
            insertarDonador(datosString, dicc)
        else:
            print("no joda fecha invalida")

