#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:11/05/2021 06:25 p.m.
#Última modificación:11/05/2021 09:10  p.m.
#Versión: 3.9.5

import re
from datetime import datetime

def validarEntero(num):
    """
    Funcionamiento: Determina si el número es connveritble a  un entero
    Entradas:
    -num(string): Una cadena de texto con la posibilidad de ser entero
    Salidas: 
    -True si el número sí es entero
    -'a' si el número no fuese entero. 
    """
    try:
        num = int(num)
        if num > 0:
            return True
    except ValueError:
        return False

def validarCedula(id):
    """
    funcionamiento: Se encarga de validar que el numero de cedula ingresado por el usuario sea válido
    entradas: id: la cedula del donador a validar
    salidas: True: si la cédula SÍ es válida 
    False: si la cédula NO es válida
    """
    if re.match("^\d\-\d{4}\-\d{4}$",id):
        return True
    else:
        return False

def validarFormatoFecha(dob):
    """
    funcionamiento: Se encarga de validar que la fecha de nacimiento del donante sea válida
    entradas: dob: la fecha de nacimiento del donante
    salidas: True: si la fecha SÍ es válida 
    False: si la fecha NO es válida
    """
    if re.match("^(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/](19[0-9][0-9]|20[0-9][0-9])$", dob):
        return True
    else:
        return False

def validarEdad(dob):
    """
    funcionamiento: se encarga de validar que el donante sea mayor a 18 años
    entradas: la fecha del donante
    salidas: true: si el donante es mayor de edad
    False: si el donante NO es mayor de edad
    """
    fecha = datetime.strptime(dob, '%d/%m/%Y')
    resta = datetime.now() - fecha
    resta = resta.days
    if resta >= 6575 and resta <= 21900:
        return True
    else:
        return False

def validarCorreo(correo):
    """
    funcionamiento: Se encarga de validar que la el correo electronico del donador sea valido
    entradas: correo: el correo electronico del donador
    salidas: True: si el correo SÍ es válida 
    False: si el correo NO es válida
    """
    if re.match("^[a-z0-9]+[\.'\-a-z0-9_]*[a-z0-9]+@(gmail.com|costarricense.cr|racsa.go.cr|ccss.sa.cr)$",correo.lower()):
        return True
    else:
        return False

def validarTelefono(telefono):
    """
    funcionamiento: Se encarga de validar que el numero de telefono del donador sea valido
    entradas: correo: el numero de telefono del donador
    salidas: True: si el numero de telefono SÍ es válida 
    False: si el numero de telefono NO es válida
    """
    if re.match("^\d{4}\-\d{4}$",telefono):
        return True
    else:
        return False
        
def validarPeso(peso):
    """
    funcionamiento: Se encarga de validar que el peso del donador sea valido
    entradas: correo: el peso del donador
    salidas: True: si el peso SÍ es válida 
    False: si el peso NO es válida
    """
    try:
        if peso > 50 and peso < 120:
            return True
        else:
            return False   
    except:
        return False

def validarExistente(id, matriz):
    """
    funcionamiento: Se encarga de validar que el donador no haya sido ingresado ya
    entradas: id: numero de cedula del donador
    salidas: True: si el donador SI se encuentra ya en la base de datos
    False: si el donador NO se encuentra en la base de datos
    """
    for i in matriz:
        if id == i[0]:
            return True
    return False

def validarRangoEdad(edad):
    """
    funcionamiento: Se encarga de validar la edad que el usuario ingrese de un donante en los reportes
    entradas: edad: la edad que haya ingresado
    salidas: True: si la edad SI es igual o mayor a 18 y menor o igual a 60
    False: si la edad NO es mayor a 18 o si la edad es mayor a 60
    """
    try:
        if int(edad) >= 18 and int(edad) < 60:
            return True
        else:
            return False
    except:
        return False
