#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:11/05/2021 06:25 p.m.
#Última modificación:11/05/2021 09:10  p.m.
#Versión: 3.9.5
from validaciones import validarCedula, validarExistente
import names
import random
import time
import string

def randomEmail(y):
       email = ''.join(random.choice(string.ascii_lowercase) for x in range(y))
       return email + random.choice(["@gmail.com","@costarricense.cr","@racsa.go.cr","@ccss.sa.cr"])

def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)
    

def insertarDonador(datos, matriz):
    """
    funcionamiento: Se encarga insertar el donador en la base de datos con la información correspondiente
    entradas: id: cédula de la persona, nombre: nombre completo de la persona, dob: la fecha de nacimiento
    de la persona, tipoSangre: el tipo de sangre de la persona, sexo: el sexo biológico de la persona, 
    peso: cuanto pesa la persona, telefono: el numero de contacto de la persona, correo: el correo electrónico
    de la persona, matriz: la base de datos.
    salidas: la matriz con el nuevo donador
    """
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
    donador.append(winner)
    donador.append(random_date("1/1/1970 1:30 PM", "1/1/2003 4:50 AM", random.random())[0:10])
    donador.append(random.choice(["O", "A", "B", "AB"])+random.choice("-+"))
    if winner == m:
        donador.append(True)
    else:
        donador.append(False)
    donador.append(random.randint(51,120))
    donador.append(str(random.randint(2000,9999))+"-"+str(random.randint(2000,9999)))
    donador.append(randomEmail(7))
    donador.append(1)
    return donador
    

    
matriz = []
#lista = ["118460455", "César Jiménez Salazar", "10/06/2002", "O+", "M", "66", "85296827", "ytcesarjs@gmail.com"]
#print(insertarDonador(lista, dicc))
generarDonadores(100,matriz)

for i in matriz:
    print(str(i)+"\n")

var = input("Aqui: ")

print(validarExistente(var, matriz))