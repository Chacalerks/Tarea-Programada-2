#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:11/05/2021 06:25 p.m.
#Última modificación:11/05/2021 09:10  p.m.
#Versión: 3.9.5

import pickle
def leerDatos(nomArchLeer):
    dicc={}
    try:
        f=open(nomArchLeer,"rb")
        dicc = pickle.load(f)
        f.close()
    except:
        print("No se ha encontrado datos registrados en: ", nomArchLeer)
    return dicc

def guardarDatos(nomArchGrabar,dicc):
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(dicc,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
    return