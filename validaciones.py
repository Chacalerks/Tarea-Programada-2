#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:11/05/2021 06:25 p.m.
#Última modificación:11/05/2021 09:10  p.m.
#Versión: 3.9.5

import re

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

def validarFecha(dob):
    """
    funcionamiento: Se encarga de validar que la fecha de nacimiento del donante sea válida
    entradas: dob: la fecha de nacimiento del donante
    salidas: True: si la fecha SÍ es válida 
    False: si la fecha NO es válida
    """
    if re.match("^(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])[-/.](19|20)\\d\\d$", dob):
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
        if int(peso) > 50 and int(peso) < 120:
            return True
        else:
            return False   
    except:
        return False

def 

print(validarPeso("sadas"))