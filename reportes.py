#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:22/05/2021 07:21 p.m.
#Última modificación:24/05/2021 09:10  p.m.
#Versión: 3.9.5
import webbrowser
import dominate
from dominate.tags import *
from archivo import *
from datetime import datetime
from funciones import *

import tkinter as tk
from tkinter import StringVar, ttk, messagebox
from tkinter.constants import E
from typing import Text
from general import *
from validaciones import *
from funciones import *
from archivo import*

def reportesPorProvincia(mainFrame,corazon_img,matriz):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario insertar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)


    #Provincias
    provincia = StringVar()
    provincia.set("San José")
    tk.Label(grupo, text="Provincia: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10, sticky=E)
    provincias_cbo = ttk.Combobox(grupo,textvariable=provincia, width=47, state="readonly")
    provincias_cbo['values']= ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
    provincias_cbo.grid(row=1, column=1, pady=10,padx=10)

     

    buscar_btn = ttk.Button(grupo, text="Crear Reporte",width=40,padding=20, command=lambda:reporteProvinciaES(provincia,matriz))
    buscar_btn.grid(row=9, column=0,padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)

def reporteProvinciaES(provincia,matriz):
    provincia = provincia.get()
    provincia = obtenerIndexLugar(provincia)
    crearArchivo("provincia.html",reporteProvincia(provincia,matriz))
    abrirPage("provincia.html")

def reporteProvincia(provincia,matriz):
    fecha = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.now().strftime("%I:%M %p")
    doc = dominate.document(title='Reporte por provincia')
    donantes = []
    for i in matriz:
        if i[0][0] == provincia:
            donantes.append(i)

    with doc.head:
        link(rel='stylesheet', href='style.css')

    with doc:
        with div(id='header'):
            h1("Donadores por provincia")
            h2('Fecha: '+fecha)
            h2('Hora: '+hora)
            
        with div(cls='body'):
            with table(cls='tabla'):
                with tr(cls="titulos"):
                    th('Cédula')
                    th('Nombre Completo')
                    th('Fecha de Nacimiento')
                    th('Teléfono')
                    th('Correo') 
                for i in donantes:
                    with tr():
                        th(i[0])
                        th(i[1])
                        th(i[2])
                        th(i[6])
                        th(i[7])
    return str(doc)

def reporteEdad(edadIni, edadFin, matriz):
    
    fecha = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.now().strftime("%I:%M")
    doc = dominate.document(title='Reporte por rango de Edad')
    
    donantes = []
    for i in matriz:
        fechaNaci = datetime.strptime(i[2], '%d/%m/%Y')
        annos = datetime.today() - fechaNaci
        annos = annos.days
        annos = annos // 365
        if annos >= edadIni and annos <= edadFin:
            donantes.append(i)
    with doc.head:
        link(rel='stylesheet', href='style.css')

    with doc:
        with div(id='header'):
            h1("Donadores por rango de edad")
            h2('Fecha: '+fecha)
            h2('Hora: '+hora)
            
        with div(cls='body'):
            with table(cls='tabla'):
                with tr(cls="titulos"):
                    th('Cédula')
                    th('Nombre Completo')
                    th('Fecha de Nacimiento')
                    th('Teléfono')
                    th('Correo') 
                for i in donantes:
                    with tr():
                        th(i[0])
                        th(i[1])
                        th(i[2])
                        th(i[6])
                        th(i[7])
    return str(doc)

def reporteTipoSangre(sangre, matriz):
    
    fecha = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.now().strftime("%I:%M")
    doc = dominate.document(title='Reporte por rango de Edad')
    
    donantes = []
    for i in matriz:
        print(i[3])
        if i[3] == sangre:
            donantes.append(i)
    with doc.head:
        link(rel='stylesheet', href='style.css')

    with doc:
        with div(id='header'):
            h1("Donadores por rango de edad")
            h2('Fecha: '+fecha)
            h2('Hora: '+hora)
            
        with div(cls='body'):
            with table(cls='tabla'):
                with tr(cls="titulos"):
                    th('Cédula')
                    th('Nombre Completo')
                    th('Fecha de Nacimiento')
                    th('Teléfono')
                    th('Correo') 
                for i in donantes:
                    with tr():
                        th(i[0])
                        th(i[1])
                        th(i[2])
                        th(i[6])
                        th(i[7])
    return str(doc)

def abrirPage(nombreFile):
    webbrowser.open_new_tab(nombreFile)

