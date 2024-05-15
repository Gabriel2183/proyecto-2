import random
simulación = "n"
pagoporunidaddedolorin = 5
codigoid = []
estación = []
nombre = []
apellido = []
fechadenacimiento = []
contraseña = []
numeros_aleatoriosest1 = []
numeros_aleatoriosest2 = []
numeros_aleatorioest3 = []


def ingresar_operarios ():
    print ("Ingresar operarios")
    print ("Ingrese el codigo de identificación")
    codigoid.append (input())
    print ("Ingrese la estación de trabajo")
    estación.append (input())
    print ("Ingrese el nombre del operario")
    nombre.append (input())
    print ("Ingrese el apellido del operario")
    apellido.append (input())
    print ("Ingrese la fecha de nacimiento")
    fechadenacimiento.append (input())
    print ("Ingrese la contraseña")
    contraseña.append (input())
    print ("Operario registrado con éxito")

def mostrar_equipo_de_trabajo ():
    print ("Equipo de trabajo")
    for i in range (len (codigoid)):
        print ("Codigo de identificación: ", codigoid[i])
        print ("Estación de trabajo: ", estación[i])
        print ("Nombre: ", nombre[i])
        print ("Apellido: ", apellido[i])
        print ("Fecha de nacimiento: ", fechadenacimiento[i])
        print ("Contraseña: ", contraseña[i])
        print ("---------------------------")


def simular_paso_del_tiempo():
    print("Simular paso del tiempo")
    for i in range(5):
        numeroest1 = random.randint(75, 120)
        numeros_aleatoriosest1.append(numeroest1)
    for i in range(5):
        numeroest2 = random.randint(75, 120)
        numeros_aleatoriosest2.append(numeroest2)
    for i in range(5):
        numeroest3 = random.randint(75, 120)
        numeros_aleatorioest3.append(numeroest3)

def historial_de_producción ():
    i = 1
    print ("Historial de producción")
    print ("Estación 1")
    print ("Producto ", numeros_aleatoriosest1[i], numeros_aleatoriosest1[i+1], numeros_aleatoriosest1[i+2], numeros_aleatoriosest1[i+3], numeros_aleatoriosest1[i+4])
    print ("Estación 2")
    print ("Producto ", numeros_aleatoriosest2[i], numeros_aleatoriosest2[i+1], numeros_aleatoriosest2[i+2], numeros_aleatoriosest2[i+3], numeros_aleatoriosest2[i+4])
    print ("Estación 3")
    print ("Producto ", numeros_aleatorioest3[i], numeros_aleatorioest3[i+1], numeros_aleatorioest3[i+2], numeros_aleatorioest3[i+3], numeros_aleatorioest3[i+4])

def control_de_calidad ():
   continuar = "s"
   while continuar == "s":
    print ("control de calidad")
    print ("Ingrese la cantidad de producto defecturoso")
    input ()
    print ("ingrese el dia que se encontró el producto defectuoso")
    input ()
    print ("ingrese la estación en la que se encontró el producto defectuoso")
    input ()
    print ("¿Desea continuar con el control de calidad? s/n")
    continuar = input ()

def pago_a_operarios ():
    print ("Pago a operarios")
    pagototalest1 = 0
    cantidadproducidaest1 = 0
    print ("Estación 1")
    for i in range (5):
     if numeros_aleatoriosest1[i] > 100:
        pagototalest1 += 15.00
     cantidadproducidaest1 += numeros_aleatoriosest1[i]  
    pagototalest1 += cantidadproducidaest1 * pagoporunidaddedolorin 
    print ("El pago total de la estación 1 es de: ", pagototalest1)
    pagototalest2 = 0
    cantidadproducidaest2 = 0
    print ("Estación 2")
    for i in range (5):
     if numeros_aleatoriosest2[i] > 100:
        pagototalest2 += 15.00
     cantidadproducidaest2 += numeros_aleatoriosest2[i]
    pagototalest2 += cantidadproducidaest2 * pagoporunidaddedolorin
    print ("El pago total de la estación 2 es de: ", pagototalest2)
    pagototalest3 = 0
    cantidadproducidaest3 = 0
    print ("Estación 3")
    for i in range (5):
        if numeros_aleatorioest3[i] > 100:
            pagototalest3 += 15.00
        cantidadproducidaest3 += numeros_aleatorioest3[i]
    pagototalest3 += cantidadproducidaest3 * pagoporunidaddedolorin
    print ("El pago total de la estación 3 es de: ", pagototalest3)





while True:
    print ("Bienvenido al sistema de registro de usuarios")
    print ("Seleccione una opción")
    print ("1. Ingresar operarios")
    print ("2. Mostrar equipo de trabajo")
    print ("3. Simular paso del tiempo")
    print ("4. Historial de reproduccion")
    print ("5. Control de calidad")
    print ("6. Pago a operarios")
    print ("7. Reestablecer contraseña")
    print ("8. Cambiar contraseña")
    print ("9. Salir")