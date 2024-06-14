import os
import json

os.system("cls")

#leer json
url_empleados = "./json/empleado.json"

def leer_archivo_json(url):
    try:
        with open(url,'r') as archivo: # leer archivo
            return json.load(archivo) # retornar lo que tenga el archivo
    except:
        return []
    
def guardar_archivo_json(url,data):
    try:
        with open(url,'w') as archivo: # leer archivo
            json.dump(data, archivo, indent=4)
    except:
        return []

    #falta validar int
def listar_empleados():
    os.system("cls")
    print("=== Listado De Empleados ===")
    empleados = leer_archivo_json(url_empleados)
    #print(empleados)
    headers = ['id_empleado','nombre','apellido','edad','sueldo','id_cargo']
    co_widths = [15,15,15,15,15]
    print(empleados)

def actualizar_empleado():   
    os.system("cls")
    print("Editar Empleado")
    empleados = leer_archivo_json(url_empleados)

    listar_empleados()
    id_empleado = input("Ingrese el id del empleado a modificar") 

    nombre = input("Ingrese el nombre del empleado >> ")  
    apellido = input("Ingrese el apellido del empleado >> ")
    edad = int(input("Ingrese la edad del empleado >> "))
    sueldo = int(input("Ingrese el sueldo del empleado >> "))
    id_cargo = input("Ingrese el id del cargo >> ")

    for empleado in empleados:
        if empleado['id_empleado'] == id_empleado:
            empleado['nombre'] = nombre
            empleado['apellido'] = apellido
            empleado['edad'] = edad
            empleado['sueldo'] = sueldo
            empleado['id_cargo'] = id_cargo
            break

    guardar_archivo_json(url_empleados,empleados)

def crear_empleado():
    os.system("cls")
    print("=== Ingresar Empleados ===")
    empleados = leer_archivo_json(url_empleados)

    id_empleado = input("Ingrese id Empleado >> ")
    nombre = input("Ingrese el nombre del empleado >> ")  
    apellido = input("Ingrese el apellido del empleado >> ")
    edad = int(input("Ingrese la edad del empleado >> "))
    sueldo = int(input("Ingrese el sueldo del empleado >> "))
    id_cargo = input("Ingrese el id del cargo >> ")
    # debes validar los input
    nuevo_empleado = {
        "id_empleado": id_empleado,
        "nombre": nombre,
        "apellido": apellido,
        "edad":edad,
        "sueldo_base": sueldo,
        "id_cargo": id_cargo
    }

    empleados.append(nuevo_empleado)
    guardar_archivo_json(url_empleados,empleados)

def eliminar_empleado():
    os.system("cls")
    print("=== Eliminar Empleados ===")

    empleados = leer_archivo_json(url_empleados)
    listar_empleados()
    id_empleado = input("Ingrese el id del empleado a eliminar >> ") 

    empleados_que_quedan = [] #variable auxiliar, que recorre todos los empleados que queremos dejar y omitirá al que queremos eliminar
    for empleado in empleados:
        if empleado['id_empleado'] != id_empleado:
            empleados_que_quedan.append(empleado)

    guardar_archivo_json(url_empleados,empleados_que_quedan)


def menu_general():
    os.system("cls")

    print("=== Menu ===")
    print("1. Crear")
    print("2. Actualizar")
    print("3. Listar")
    print("4. Eliminar")
    print("5. Salir")

def seleccionar_opcion(maxOpcion):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
        except:
            pass

        if opcion < 0 or opcion > maxOpcion:
            print("Error: Debes seleccionar una de las opciones disponibles.")
            print("Presione Enter para continuar")
        else:
            return opcion

def iniciarPrograma():
    while True:

        menu_general()
        opcion = seleccionar_opcion(5)
        if opcion == 1:
            print("Crear")
            crear_empleado()
        elif opcion == 2:
            print("Actualizar")
            actualizar_empleado()
        elif opcion == 3:
            print("Listar")
            listar_empleados()
        elif opcion == 4:
            print("Eliminar")
            eliminar_empleado()
        elif opcion == 5:
            print("Hasta Pronto")
            return #recordar que el return mata el ciclo While. 
        
        input("Presione Enter Para Continuar")

if __name__ == "__main__":
    iniciarPrograma()