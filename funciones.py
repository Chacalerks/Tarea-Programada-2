#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:11/05/2021 06:25 p.m.
#Última modificación:11/05/2021 09:10  p.m.
#Versión: 3.9.5
from validaciones import *
import names
import random
from datetime import datetime
import string
from dateutil.relativedelta import relativedelta
import time

def str_time_prop(start, end, time_format, prop):
    """
    funcionamiento: genera una fecha aleatoria entre dos fechas dadas
    entradas: start: la fecha inicial
    end: la fecha futura
    time_format: el formato de la fecha
    prop: numero aleatorio para sacar la fecha
    salidas: la fecha aleatoria
    """
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)

def generarRangoFecha():
    fechaMin = (datetime.today() + relativedelta(years=-18)).strftime('%d/%m/%Y')
    fechaMax = (datetime.today() + relativedelta(years=-50)).strftime('%d/%m/%Y')
    return [fechaMax,fechaMin]

def randomEmail(y):
       email = ''.join(random.choice(string.ascii_lowercase) for x in range(y))
       return email + random.choice(["@gmail.com","@costarricense.cr","@racsa.go.cr","@ccss.sa.cr"])
    

def insertarDonador(datos, matriz):
    """
    funcionamiento: Se encarga insertar el donador en la base de datos con la información correspondiente
    entradas: id: cédula de la persona, nombre: nombre completo de la persona, dob: la fecha de nacimiento
    de la persona, tipoSangre: el tipo de sangre de la persona, sexo: el sexo biológico de la persona, 
    peso: cuanto pesa la persona, telefono: el numero de contacto de la persona, correo: el correo electrónico
    de la persona, matriz: la base de datos.
    salidas: la matriz con el nuevo donador
    """
    datos.append(1)
    datos.append(0)
    matriz.append(datos)
    return matriz

def generarDonadores(cant, matriz):
    cant = int(cant)
    while cant != 0:
        insertarDonador(randomDonador(),matriz)
        cant-=1    
    
def randomDonador():
    donador = []
    donador.append(str(random.randint(1,9))+"-"+str(random.randint(1000,9999))+"-"+str(random.randint(1000,9999)))
    m = names.get_full_name(gender='male')
    f = names.get_full_name(gender='female')
    winner = random.choice([m, f])
    donador.append(winner+" "+names.get_last_name())
    donador.append(random_date(generarRangoFecha()[0], generarRangoFecha()[1], random.random()))
    donador.append(random.choice(["O", "A", "B", "AB"])+random.choice("-+"))
    if winner == m:
        donador.append(True)
    else:
        donador.append(False)
    donador.append(random.randint(51,120))
    donador.append(str(random.randint(2000,9999))+"-"+str(random.randint(2000,9999)))
    donador.append(randomEmail(7))
    return donador

def crearFecha(edad):
    fecha = (datetime.today() + relativedelta(years=-edad)).strftime('%d/%m/%Y')
    fecha = datetime.strptime(fecha, '%d/%m/%Y')
    return fecha

#matriz = []
#lista = ["118460455", "César Jiménez Salazar", "10/06/2002", "O+", "M", "66", "85296827", "ytcesarjs@gmail.com"]
#print(insertarDonador(lista, dicc))
#generarDonadores(100,matriz)

#for i in matriz:
#    print(str(i)+"\n")

#var = input("Aqui: ")

#print(validarExistente(var, matriz))

# Arreglar la validacion de la fecha de nacimiento y los mayores a 18 años por meses
# Generar donantes respecto a una resta de años, no sólo entre dos fechas, para que así sea flexible con el paso del tiempo
# Hacer Actualizar donador
# Eliminar donador
# Insertar lugar de donación según provincia en un archivo diferente al de los donadores