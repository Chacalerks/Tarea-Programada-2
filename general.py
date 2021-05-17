from tkinter import BooleanVar, StringVar
import tkinter as tk

color = {"fondo":"#F0F0F0", "sidebar":"#052744", "topbar":"#0D5D8C", "caja": "#BFBFBF" ,  "principal": "#043E79", "secundario": "#043E79","tercero":"#0E3D5E"}
tittle = "Sistema de donación"
#----------------------------------------------------------------------------
#                           Navegación
#----------------------------------------------------------------------------
def cargarInicio(mainFrame, corazon_img):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario insertar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    corazon_lb = tk.Label(mainFrame, image=corazon_img, bd=0)
    corazon_lb.pack(side="top")


def limpiarFrame(mainFrame):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario insertar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    for elemento in mainFrame.winfo_children():
        elemento.destroy()

def limpiarCampos(datos):
    """
    Funcionamiento: Limpia los campos del formulario.
    Entradas: Las variables que esta enlazadas alformulario
    Salidas: NA
    """
    i = 0
    while i<len(datos):
        datos[i].set("")
        i+=1
#----------------------------------------------------------------------------
#                           Entrada y Salida
#----------------------------------------------------------------------------
def establecerDatos(datosString):
    """
    Funcionamiento: Se encarga de estableces los datos de los campos.
    Entradas: -datosString: el array con las variables.
    Salidas: -Datos: Lista con los datos en string
    """
    datos = []
    i=0
    if len(datosString)==0:# Cuando no hay datos que leer []
        while True:
            if i == 4 :
                datos.append(BooleanVar())
                datos[i].set(True)
            else:
                datos.append(StringVar())
                datos[i].set("")            
                if i==7:
                    break
            i+=1
    else: # cuando se van a cargar datos en el formularios
        while True:
            if i == 4 :
                datos.append(BooleanVar())
                datos[i].set(datosString[i])
            else:
                datos.append(StringVar())
                datos[i].set(datosString[i])            
                if i==7:
                    break
            i+=1
    return datos
def obtenerDatos(datos):
    """
    Funcionamiento: Se encarga de obtener los datos de los campos.
    Entradas: -Datos: el array con las variables.
    Salidas: -DatosString: Lista con los datos en string
    """
    datosString = []
    i = 0
    while i<len(datos):
        datosString.append(datos[i].get())
        i+=1
    if datosString[5].isdigit():
        datosString[5]=int(datosString[5])
    return datosString
#----------------------------------------------------------------------------
#                           Procesar
#----------------------------------------------------------------------------
def insertarDonador(datos, matriz):
    """
    funcionamiento: Se encarga insertar el donador en la base de datos con la información correspondiente
    entradas: id: cédula de la persona, nombre: nombre completo de la persona, dob: la fecha de nacimiento
    de la persona, tipoSangre: el tipo de sangre de la persona, sexo: el sexo biológico de la persona, 
    peso: cuanto pesa la persona, telefono: el numero de contacto de la persona, correo: el correo electrónico
    de la persona, dicc: la base de datos.
    salidas: el diccionario con el nuevo donador
    """
    id = datos[0]
    fila= []
    i =1
    while i<len(datos):
        fila.append(datos[i])
        i+=1
    matriz[id] = fila
    return matriz

