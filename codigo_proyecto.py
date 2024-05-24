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

def ingresar_supervisor():
    print("Ingresar supervisor")
    print("Ingrese el código de identificación")
    codigo = input()
    while codigo == "":
        print("Error: El código de identificación no puede estar vacío")
        print("Ingrese el código de identificación")
        codigo = input()
        if os.name == 'nt':
            os.system('cls')
    codigoid.append(codigo)
    if os.name == 'nt':
        os.system('cls')
    estación.append("Supervisor")
    print("Ingrese el nombre del supervisor")
    nombre_supervisor = input()
    while nombre_supervisor == "":
        print("Error: El nombre del supervisor no puede estar vacío")
        print("Ingrese el nombre del supervisor")
        nombre_supervisor = input()
        if os.name == 'nt':
            os.system('cls')
    nombre.append(nombre_supervisor)
    if os.name == 'nt':
        os.system('cls')
    print("Ingrese el apellido del supervisor")
    apellido_supervisor = input()
    while apellido_supervisor == "":
        print("Error: El apellido del supervisor no puede estar vacío")
        print("Ingrese el apellido del supervisor")
        apellido_supervisor = input()
        if os.name == 'nt':
            os.system('cls')
    apellido.append(apellido_supervisor)
    if os.name == 'nt':
        os.system('cls')
    while True:
        print("Ingrese el día de nacimiento")
        dianaci = int(input())
        if dianaci < 0 and dianaci > 32:
            print("Error: Ingrese un día de nacimiento válido")
        else:
            diadenacimiento.append(dianaci)
            if os.name == 'nt':
                os.system('cls')
            break
    while True:
        print("Ingrese el mes de nacimiento")
        mesnaci = int(input())
        if mesnaci < 1994 and mesnaci > 13:
            print("Error: Ingrese un mes de nacimiento válido")
        else:
            mesdenacimiento.append(mesnaci)
            if os.name == 'nt':
                os.system('cls')
            break
    while True:
        print("Ingrese el año de nacimiento")
        añonaci = int(input())
        if añonaci < 0 and añonaci > 2024:
            print("Error: Ingrese un año de nacimiento válido")
        elif añonaci > 2005:
            print("Error: El supervisor debe ser mayor de edad")
        else:
            añodenacimiento.append(añonaci)
            if os.name == 'nt':
                os.system('cls')
            break
    print("Ingrese la contraseña")
    contraseña_supervisor = input()
    while contraseña_supervisor == "":
        print("Error: La contraseña no puede estar vacía")
        print("Ingrese la contraseña")
        contraseña_supervisor = input()
        if os.name == 'nt':
            os.system('cls')
    contraseña.append(contraseña_supervisor)
    if os.name == 'nt':
        os.system('cls')
    print("---------------------------")
    print("Supervisor registrado con éxito")
    print("---------------------------")


def ingresar_operarios():
    print("Ingresar operarios")
    print("Ingrese el codigo de identificación")
    codigo = input()
    while codigo == "":
        print("Error: El código de identificación no puede estar vacío")
        print("Ingrese el codigo de identificación")
        codigo = input()
        if os.name == 'nt':
            os.system('cls')
    codigoid.append(codigo)
    if os.name == 'nt':
        os.system('cls')
    while True:
        print("Ingrese la estación de trabajo")
        estacón = int(input())
        if (estacón >= 1) and (estacón <= 3):
            estación.append(estacón)
            if os.name == 'nt':
                os.system('cls')
            break
        else:
            print("Estación no válida")
    print("Ingrese el nombre del operario")
    nombre_operario = input()
    while nombre_operario == "":
        print("Error: El nombre del operario no puede estar vacío")
        print("Ingrese el nombre del operario")
        nombre_operario = input()
        if os.name == 'nt':
            os.system('cls')
    nombre.append(nombre_operario)
    if os.name == 'nt':
        os.system('cls')
    print("Ingrese el apellido del operario")
    apellido_operario = input()
    while apellido_operario == "":
        print("Error: El apellido del operario no puede estar vacío")
        print("Ingrese el apellido del operario")
        apellido_operario = input()
        if os.name == 'nt':
            os.system('cls')
    apellido.append(apellido_operario)
    if os.name == 'nt':
        os.system('cls')
    while True:
        print("Ingrese el día de nacimiento")
        dianaci = int(input())
        if dianaci < 0 and dianaci > 32:
            print("Error: Ingrese un día de nacimiento válido")
        else:
            diadenacimiento.append(dianaci)
            if os.name == 'nt':
                os.system('cls')
            break
    while True:
        print("Ingrese el mes de nacimiento")
        mesnaci = int(input())
        if mesnaci < 0 and mesnaci > 13:
            print("Error: Ingrese un mes de nacimiento válido")
        else:
            mesdenacimiento.append(mesnaci)
            if os.name == 'nt':
                os.system('cls')
            break
    while True:
        print("Ingrese el año de nacimiento")
        añonaci = int(input())
        if añonaci < 1994 and añonaci > 2024:
            print("Error: Ingrese un año de nacimiento válido")
        elif añonaci > 2005:
            print("Debes de ser mayor de edad para trabajar en la empresa")
        else:
            añodenacimiento.append(añonaci)
            if os.name == 'nt':
                os.system('cls')
            break
    print("Ingrese la contraseña")
    contraseña_operario = input()
    while contraseña_operario == "":
        print("Error: La contraseña no puede estar vacía")
        print("Ingrese la contraseña")
        contraseña_operario = input()
        if os.name == 'nt':
            os.system('cls')
    contraseña.append(contraseña_operario)
    if os.name == 'nt':
        os.system('cls')
    print("Operario registrado con éxito")


def mostrar_equipo_de_trabajo():
    print("Equipo de trabajo")
    listatrabajadores = ""
    print ("Código de identificación" + "\t" + "Estación de trabajo" + "\t" + "Nombre" + "\t"+"\t" + "Apellido" + "\t" + "Fecha de nacimiento"+"\n")
    for i in range (len(codigoid)):
        listatrabajadores += "\t"  + str(codigoid[i]) + "\t" + "\t" + "\t" + str(estación[i]) + "\t" +"\t" + str(nombre[i]) + "\t"+"\t" + str(apellido[i]) + "\t" +"\t" + str(diadenacimiento[i]) + "/" + str(mesdenacimiento[i]) + "/" + str(añodenacimiento[i]) + "\n"
        print (listatrabajadores)
    print("---------------------------")
    
def simular_paso_del_tiempo():
    print("Simular paso del tiempo")
    for i in range(5):
        numeroest1 = randint(75, 120)
        numeros_aleatoriosest1.append(numeroest1)
    for i in range(5):
        numeroest2 = randint(75, 120)
        numeros_aleatoriosest2.append(numeroest2)
    for i in range(5):
        numeroest3 = randint(75, 120)
        numeros_aleatorioest3.append(numeroest3)
    print("")
    print("---------------------------")
    print("Simulación realizada con éxito")
    print("")
    print("---------------------------")


def historial_de_producción():
    print("Historial de producción")
    listaproducida1 = ""
    for i in range(5):
        listaproducida1 += str(numeros_aleatoriosest1[i]) + "\t"
    print("Estación 1" + "\t", listaproducida1)
    listaproducida2 = ""
    for i in range(5):
        listaproducida2 += str(numeros_aleatoriosest2[i]) + "\t"
    print("Estación 2" + "\t", listaproducida2)
    listaproducida3 = ""
    for i in range(5):
        listaproducida3 += str(numeros_aleatorioest3[i]) + "\t"
    print("Estación 3" + "\t", listaproducida3)
    print("---------------------------")


def control_de_calidad():
    for i in range(4):
        numeros_aleatoriosest1[i] = int(numeros_aleatoriosest1[i] - numeros_aleatoriosest1[i] * 0.1)
        numeros_aleatoriosest2[i] = int(numeros_aleatoriosest2[i] - numeros_aleatoriosest2[i] * 0.06)
        numeros_aleatorioest3[i] = int(numeros_aleatorioest3[i] - numeros_aleatorioest3[i] * 0.03)
    print("Control de calidad realizado con éxito")
    input("presine enter para continuar ")


def pago_a_operarios():
    print("Pago a operarios")
    pagototalest1 = 0
    cantidadproducidaest1 = 0
    print("Estación 1")
    for i in range(5):
        if numeros_aleatoriosest1[i] > 100:
            pagototalest1 += 15.00
        cantidadproducidaest1 += numeros_aleatoriosest1[i]
    pagototalest1 += cantidadproducidaest1 * pagoporunidaddedolorin
    print("El pago total de la estación 1 es de: ", pagototalest1)
    pagototalest2 = 0
    cantidadproducidaest2 = 0
    print("Estación 2")
    for i in range(5):
        if numeros_aleatoriosest2[i] > 100:
            pagototalest2 += 15.00
        cantidadproducidaest2 += numeros_aleatoriosest2[i]
    pagototalest2 += cantidadproducidaest2 * pagoporunidaddedolorin
    print("El pago total de la estación 2 es de: ", pagototalest2)
    pagototalest3 = 0
    cantidadproducidaest3 = 0
    print("Estación 3")
    for i in range(5):
        if numeros_aleatorioest3[i] > 100:
            pagototalest3 += 15.00
            cantidadproducidaest3 += numeros_aleatorioest3[i]
    pagototalest3 += cantidadproducidaest3 * pagoporunidaddedolorin
    print("El pago total de la estación 3 es de: ", pagototalest3)


def reestablecer_contraseña():
    print("Reestablecer contraseña")
    print("Ingrese el código de identificación: ")
    codigo = input()
    posicion = codigoid.index(codigo)
    contraseña[posicion] = (nombre[posicion] + "." + apellido[posicion] + str(añodenacimiento[posicion]))
    print("Contraseña reestablecida con éxito")


def cambiar_contraseña():
    print("Cambiar contraseña")
    print("Ingrese el código de identificación")
    codigo = input()
    print("Ingrese la contraseña actual")
    contraseñaactual = input()
    posicion = codigoid.index(codigo)
    if contraseñaactual == contraseña[posicion]:
        print("Ingrese la nueva contraseña")
        contraseña[posicion] = input()
        print("Contraseña cambiada con éxito")
    else:
        print("Contraseña incorrecta")


ingresar_supervisor()
print("Presione enter para continuar")
input()
if os.name == 'nt':
    os.system('cls')
while True:
    print("Bienvenido al sistema de registro de usuarios")
    print("Seleccione una opción")
    print("1. Ingresar operarios")
    print("2. Mostrar equipo de trabajo")
    print("3. Simular paso del tiempo")
    print("4. Historial de reproduccion")
    print("5. Control de calidad")
    print("6. Pago a operarios")
    print("7. Reestablecer contraseña")
    print("8. Cambiar contraseña")
    print("9. Salir")
    opcion = input("Ingrese su opción: ")
    if os.name == 'nt':
        os.system('cls')
    if opcion == "1":
        ingresar_operarios()
        if os.name == 'nt':
            os.system('cls')
    elif opcion == "2":
        mostrar_equipo_de_trabajo()
        print("Presione enter para continuar")
        input()
        if os.name == 'nt':
            os.system('cls')
    elif opcion == "3":
        simulación = "s"
        simular_paso_del_tiempo()
        print("Presione enter para continuar")
        input()
        if os.name == 'nt':
            os.system('cls')
    elif opcion == "4":
        if simulación == "s":
            historial_de_producción()
            print("Presione enter para continuar")
            input()
            if os.name == 'nt':
                os.system('cls')
        else:
            print("Favor de realizar la simulación del paso del tiempo")
            print("Presione enter para continuar")
            input()
            if os.name == 'nt':
                os.system('cls')
    elif opcion == "5":
        if simulación == "s":
            control_de_calidad()
            if os.name == 'nt':
                os.system('cls')
        else:
            print("Favor de realizar la simulación del paso del tiempo")
            if os.name == 'nt':
                os.system('cls')
    elif opcion == "6":
        if simulación == "s":
            pago_a_operarios()
            if os.name == 'nt':
                os.system('cls')
        else:
            print("Favor de realizar la simulación del paso del tiempo")
            if os.name == 'nt':
                os.system('cls')
    elif opcion == "7":
        reestablecer_contraseña()
        if os.name == 'nt':
            os.system('cls')
    elif opcion == "8":
        cambiar_contraseña()
        if os.name == 'nt':
            os.system('cls')
    elif opcion == "9":
        print("---------------------------")
        print("")
        print("Gracias por utilizar el sistema")
        print("")
        print("---------------------------")
        break
