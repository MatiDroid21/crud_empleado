import os
import json

os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, "r") as archivo:
        return json.load(archivo)
    
def menuGeneral():
    os.system("cls")
    print("1. Crear Empleado")
    print("2. Modificar Empleado")
    print("3. Eliminar Empleado")
    print("4. Listar Empleados")
    print("5. Salir")

def elegirOpcion(maxOpcion):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
        except:
                pass

        if opcion < 1 or opcion > maxOpcion:
                input("Opcion invalida, presione enter para reintentar")
        else:
                return opcion

def iniciarPrograma():    
    while True:
        menuGeneral()
        opcion = elegirOpcion(5)
        if opcion == 1:
            print("Crear Empleado")
        elif opcion == 2:
            print("Modificar Empleado")
        elif opcion == 3:
            print("Eliminar Empleado")
        elif opcion == 4:
            print("Listar Empleados")
            empleados = cargar_json("crud/empleados.json") #! nombre del archivo json a importar
            print(empleados)
            input("Presione enter para continuar")
        elif opcion == 5:
            print("Salir")
            break
        else:
            print("Opcion invalida")
            input("Presione enter para continuar")

iniciarPrograma()

