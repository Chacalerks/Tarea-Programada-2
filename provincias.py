#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización: 06/05/2021 09:48 p.m.
#Última modificación: 13/05/2021 1:00  p.m.
#Versión: 3.9.5

import tkinter as tk
from tkinter import StringVar, ttk, messagebox
from tkinter.constants import E
from typing import Text
from general import *
from validaciones import *
from funciones import *
from archivo import*

def insertarLugarES(mainFrame,corazon_img,dicc):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario insertar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)
    datos = []
    datos = establecerDatos(datos)
    tk.Label(grupo, text="Ingresar Lugar de Donación",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2,padx=10,sticky=E)
    #Cédula

    
    #Provincias
    provincia = StringVar()
    datos[0].set("San José")
    tk.Label(grupo, text="Provincia: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10, sticky=E)
    provincias_cbo = ttk.Combobox(grupo,textvariable=datos[0], width=47, state="readonly")
    provincias_cbo['values']= ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
    provincias_cbo.grid(row=1, column=1, pady=10,padx=10)

    #lugar
    
    tk.Label(grupo, text="Lugar: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=2, column=0, pady=10,padx=10,sticky=E)
    lugar_txt = ttk.Entry(grupo,textvariable=datos[1], width=50)
    lugar_txt.grid(row=2, column=1, pady=10,padx=10)

    ingresar_btn = ttk.Button(grupo, text="Registrar",padding=15,width=50, command=lambda:ingresarLugarES(datos,dicc))
    ingresar_btn.grid(row=3, column=0, columnspan=2, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)


def ingresarLugarES(datos,dicc):
    """
    Funcionamiento: Se encarga validar los datos del lugar.
    Entradas: -datos: datos del lugar dicc: diccionario en el que se va a guardar
    Salidas: Mensajes de ardevertencias o confirmación
    """
    datosString = obtenerDatos(datos)
    print(datosString)
    datosString[0]= traducirLugar(datosString[0])
    if not validarVacio(datosString[1]):
        messagebox.showwarning(title=tittle, message="Debe de ingresar el nombre de un lugar")
    if datosString[1] in dicc[datosString[0]]:
        messagebox.showwarning(title=tittle, message="Este lugar ya se encuentra registrado")
    else:
        guardarLugar(datosString,dicc)
        guardarDatos('provincias',dicc)
        
        print(dicc)
        messagebox.showinfo(title=tittle, message="Se ha registrado un nuevo lugar")



