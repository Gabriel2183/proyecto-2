from random import *
import os
simulación = "n"
pagoporunidaddedolorin = 5
codigoid = []
estación = []
nombre = []
apellido = []
diadenacimiento = []
mesdenacimiento = []
añodenacimiento = []
contraseña = []
numeros_aleatoriosest1 = []
numeros_aleatoriosest2 = []
numeros_aleatorioest3 = []
    
def ingresar_supervisor ():
    print ("Ingresar supervisor")
    print ("Ingrese el código de identificación")
    codigoid.append (input())
    os.system('cls' if os.name == 'nt' else 'clear')
    estación.append ("Supervisor")
    print ("Ingrese el nombre del supervisor")
    nombre.append (input())
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Ingrese el apellido del supervisor")
    apellido.append (input())
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print ("Ingrese el día de nacimiento")
        dianaci = int(input())      
        if dianaci > 0 and dianaci < 32:
            print ("ingrese un dia de nacimiento valido")
        else:
            diadenacimiento.append (dianaci)
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        print ("Presione enter para continuar")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print ("Ingrese el mes de nacimiento")
        mesnaci = int(input())
        if mesnaci > 0 and mesnaci < 13:
            print ("ingrese un mes de nacimiento valido")
        else:
            mesdenacimiento.append (mesnaci)
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        print ("Presione enter para continuar")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            print ("Ingrese el año de nacimiento")
            añonaci = int(input())
            if añonaci > 0 and añonaci < 2024:
                print ("ingrese un año de nacimiento valido")
            elif añonaci > 2005 :
                print ("El supervisor debe ser mayor de edad")
            else:
                añodenacimiento.append (añonaci)
                print ("Presione enter para continuar")
                input()
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            
    print ("Ingrese la contraseña")
    contraseña.append (input())
    print ("Supervisor registrado con éxito")
    print ("")
    print ("---------------------------")


def ingresar_operarios ():
    print ("Ingresar operarios")
    print ("Ingrese el codigo de identificación")
    codigoid.append (input())
    print ("Ingrese la estación de trabajo")
    estacón = int(input ())
    if (estacón >= 1) and (estacón <= 3):
        estación.append (estacón)
    else:
        print ("Estación no válida")        
    print ("Ingrese el nombre del operario")
    nombre.append (input())
    print ("Ingrese el apellido del operario")
    apellido.append (input())
    print ("Ingrese el día de nacimiento")
    while True:
        print ("Ingrese el día de nacimiento")
        dianaci = int(input())      
        if dianaci > 0 and dianaci < 32:
            print ("ingrese un dia de nacimiento valido")
        else:
            diadenacimiento.append (dianaci)
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        print ("Presione enter para continuar")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print ("Ingrese el mes de nacimiento")
        mesnaci = int(input())
        if mesnaci > 0 and mesnaci < 13:
            print ("ingrese un mes de nacimiento valido")
        else:
            mesdenacimiento.append (mesnaci)
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        print ("Presione enter para continuar")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            print ("Ingrese el año de nacimiento")
            añonaci = int(input())
            if añonaci > 0 and añonaci < 2024:
                print ("ingrese un año de nacimiento valido")
            elif añonaci > 2005 :
                print ("Debes de ser mayor de edad para trabajar en la empresa")
            else:
                añodenacimiento.append (añonaci)
                print ("Presione enter para continuar")
                input()
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
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
        print ("Fecha de nacimiento: ", diadenacimiento[i], "/", mesdenacimiento[i], "/" ,añodenacimiento[i])
        print ("Contraseña: ", contraseña[i])
        print ("---------------------------")


def simular_paso_del_tiempo():
    print("Simular paso del tiempo")
    for i in range (5):
        numeroest1 = randint(75, 120)      
        numeros_aleatoriosest1.append(numeroest1)
    for i in range (5):
        numeroest2 = randint(75, 120)
        numeros_aleatoriosest2.append(numeroest2)
    for i in range (5):
        numeroest3 = randint(75, 120)
        numeros_aleatorioest3.append(numeroest3)

def historial_de_producción ():
    i = 0
    print ("Historial de producción")
    print ("Estación 1")
    print ("Producto ", numeros_aleatoriosest1[i], numeros_aleatoriosest1[i+1], numeros_aleatoriosest1[i+2], numeros_aleatoriosest1[i+3], numeros_aleatoriosest1[i+4])
    print ("Estación 2")
    print ("Producto ", numeros_aleatoriosest2[i], numeros_aleatoriosest2[i+1], numeros_aleatoriosest2[i+2], numeros_aleatoriosest2[i+3], numeros_aleatoriosest2[i+4])
    print ("Estación 3")
    print ("Producto ", numeros_aleatorioest3[i], numeros_aleatorioest3[i+1], numeros_aleatorioest3[i+2], numeros_aleatorioest3[i+3], numeros_aleatorioest3[i+4])

def control_de_calidad ():
    for i in range (4):
     numeros_aleatoriosest1[i] = (numeros_aleatoriosest1[i]-numeros_aleatoriosest1[i]*0.1)
     numeros_aleatoriosest2[i] = (numeros_aleatoriosest2[i]-numeros_aleatoriosest2[i]*0.06)
     numeros_aleatorioest3[i] = (numeros_aleatorioest3[i]-numeros_aleatorioest3[i]*0.03)
    print ("Control de calidad realizado con éxito")
    input("presine enter para continuar ")


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

def reestablecer_contraseña (): 
    print ("Reestablecer contraseña")
    print("Ingrese el código de identificación: ")
    codigo = input()
    posicion = codigoid.index(codigo)
    contraseña[posicion] = (nombre[posicion]  + "."  + apellido[posicion] + str(añodenacimiento[posicion]))
    print("Contraseña reestablecida con éxito")
    

def cambiar_contraseña ():
    print ("Cambiar contraseña")
    print ("Ingrese el código de identificación")
    codigo = input()
    print ("Ingrese la contraseña actual")
    contraseñaactual = input()
    posicion = codigoid.index(codigo)
    if contraseñaactual == contraseña[posicion]:
        print ("Ingrese la nueva contraseña")
        contraseña[posicion] = input()
        print ("Contraseña cambiada con éxito")
    else:
        print ("Contraseña incorrecta")
        
ingresar_supervisor()
print ("Presione enter para continuar")
input()
os.system('cls' if os.name == 'nt' else 'clear')
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
    opcion = input("Ingrese su opción: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcion == "1":
        ingresar_operarios()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opcion == "2":
        mostrar_equipo_de_trabajo()
        print ("Presione enter para continuar")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')     
    elif opcion == "3":
        simulación = "s"
        simular_paso_del_tiempo()  
        print ("Presione enter para continuar")
        input()
        os.system('cls' if os.name == 'nt' else 'clear') 
    elif opcion == "4":
        if simulación == "s":
            historial_de_producción()
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print ("Favor de realizar la simulación del paso del tiempo")
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
    elif opcion == "5":
        if simulación == "s":
            control_de_calidad()
            os.system('cls' if os.name == 'nt' else 'clear')    
        else:
            print ("Favor de realizar la simulación del paso del tiempo")
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
    elif opcion == "6":
        if simulación == "s":
            pago_a_operarios()
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print ("Favor de realizar la simulación del paso del tiempo")
            print ("Presione enter para continuar")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
    elif opcion == "7":
        reestablecer_contraseña()
        print ("Presione enter para continuar")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opcion == "8":
        cambiar_contraseña()
        print ("Presione enter para continuar")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opcion == "9":
        print ("Gracias por utilizar el sistema")
        break