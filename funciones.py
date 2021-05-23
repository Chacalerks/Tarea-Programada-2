from validaciones import validarCedula, validarExistente
import names
import random
import time
import string
def determinarPar(num):
    """
    Funcionamiento: Determina si el número es par
    Entradas:
    -num(int): número a válidar
    Salidas: 
    -True: si es par
    -False: si no es par
    """
    if num % 2 ==0:
        return True
    else:
        return False

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
    return donador

def traducirLugar(lugar):
    """
    funcionamiento: Traduce el lugar según corresponsa con tilde  no 
    entradas: lugar: lugar a traducir
    salidas: Traduccion
    """
    traduccion = ["San José","San Jose","Limón","Limon"]
    if lugar in traduccion:
        if determinarPar(traduccion.index(lugar)):
            return traduccion[traduccion.index(lugar)+1]
        else:
            return traduccion[traduccion.index(lugar)-1]
    else:
        return lugar
def datosSangre(sangre):
    datos = ["se  les  recomienda donar  glóbulos  rojos  dobles  y  sangre entera.",
    "se   recomienda   donar   glóbulos   rojos dobles y sangre entera.",
    "se  les recomienda  que  donen  sangre  entera  y plaquetas.",
    "se   les recomienda  que  donen  sangre  entera  y glóbulos rojos dobles.",
    "sangre  entera  y  de  glóbulos  rojos dobles.",
    "se  les  recomienda  que  donen  sangre entera o plaquetas.",
    "se  les recomienda     hacer     donaciones     de plaquetas y de plasma.",
    "se  lesrecomienda donar plaquetas y plasma."]
    tipo =["O+","O-","A+","A-","B+","B-","AB+","AB-"]
    return datos[tipo.index(sangre)]

def datosLugares(cedula,dicc):
    provincias = ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón","San José","San José"]
    return "Dado que usted nació en la provincia de " +provincias[int(cedula[0])-1]+" usted podría donar en: \n"+obtenerLugares(traducirLugar(provincias[int(cedula[0])-1]),dicc)

def obtenerLugares(lugar,dicc):
    lugares = ""
    for i in dicc[lugar]:
        lugares+="\t-"+i+"\n"
    return lugares
#----------------------------------------------------------------------------#
#                           Base de datos                                    #
#----------------------------------------------------------------------------#
def insertarDonador(datos, matriz):
    """
    funcionamiento: Se encarga insertar el donador en la base de datos con la información correspondiente
    entradas: Datos: los datos ha registrar del donador matriz: variable a guardar
    salidas: la matriz con el nuevo donador
    """
    datos.append(1)
    datos.append(0)
    matriz.append(datos)
    return matriz

def obtenerDatosDonador(cedula, matriz):
    """
    Funcionamiento: Se encarga buscar a un donador.
    Entradas: -cedula: cedula del donador matriz: matriz en el que se va a buscar
    Salidas: Los datos del donardor encontrados
    """
    for i in matriz:
        if i[0] == cedula:
            return matriz[matriz.index(i)]

def actulizarDonador(datos, matriz):
    """
    Funcionamiento: Se encarga actuallizar a un donador.
    Entradas: -datos: datos del donador matriz: matriz en el que se va a guardar
    Salidas: NA
    """
    matriz[matriz.index(datos)] = datos


#----------------------------------------------------------------------------#
#                           Provincias                                       #
#----------------------------------------------------------------------------#
def guardarLugar(datos,dicc):
    """
    Funcionamiento: Se encarga guardar los nuevos lugares.
    Entradas: -datos: datos del lugar dicc: diccionario en el que se va a guardar
    Salidas: NA
    """
    lugares = []
    lugares = dicc[datos[0]]
    lugares.append(datos[1])
    dicc[datos[0]] = lugares




