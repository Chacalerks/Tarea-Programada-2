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


def reporteProvincia(provincia,matriz):
    fecha = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.now().strftime("%I:%M")
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

def abrirPage(nombreFile):
    webbrowser.open_new_tab(nombreFile)


matriz = []

#lista = ["118460455", "César Jiménez Salazar", "10/06/2003", "O+", "M", "66", "85296827", "ytcesarjs@gmail.com",1,0]
generarDonadores(50,matriz)

#for i in matriz:
#    print(str(i)+"\n")

#crearArchivo('index.html',reporteProvincia("3",matriz))
crearArchivo('rango.html',reporteEdad(18,30,matriz))
abrirPage('rango.html')