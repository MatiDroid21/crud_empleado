import os
import json

os.system("cls")

# crear la ruta para cargos.json
url_cargos = './json/cargos.json'

def leer_archivo_json(url):
    try:
        with open(url,'r') as archivo: # leer archivo
            return json.load(archivo) # retornar lo que tenga el archivo
    except:
        return []
    

def guardar_json(url,data):
    try:
        with open(url,"w") as archivo:
            json.dump(data,archivo,indent=4)
    except:
        return[]
    
def listar_cargos():
    import os
    os.system("cls")
    print("=== Cargos ===")
    cargos = leer_archivo_json(url_cargos)

    #definir encabezados
    headers = ['id_cargo', 'nombre',]
    
    # Imprimir encabezados
    header_format = "{:<15} {:<15}"
    print(header_format.format(*headers))
    
    # Imprimir datos de cargos
    for cargo in cargos:
        print("{:<15} {:<20}".format(
            cargo['id_cargo'], 
            cargo['nombre'], 
        ))

def actualizar_cargo():
    os.system("cls")
    cargos = leer_archivo_json(url_cargos)
    listar_cargos()
    id_cargo = input("Ingrese el id del cargo a modificar >> ")
    nombre = input("Ingrese el nombre del cargo a modificar >> ")

    for cargo in cargos:
        if cargo['id_cargo'] == id_cargo:
            cargo['nombre'] == nombre
            break

    guardar_json(url_cargos,cargos)

def crear_cargo():
    os.system("cls")
    print("Crear un cargo")
    cargos = leer_archivo_json(url_cargos)

    id_cargo = input("Ingrese el id de cargo >> ")
    nombre = input("Ingrese el nombre del cargo >> ")

    nuevo_cargo = {
        "id_cargo":id_cargo,
        "nombre":nombre
    }

    cargos.append(nuevo_cargo)
    guardar_json(url_cargos,cargos)

def eliminar_cargo():
    os.system("cls")
    print("=== Eliminar Algun Cargo ===")
    cargos = leer_archivo_json(url_cargos)
    listar_cargos()

    id_cargo = input("Ingrese el cargo a eliminar >> ")
    cargos_restantes = []
    for cargo in cargos:
        if cargo['id_cargo'] != id_cargo:
            cargos_restantes.append(cargo)

    guardar_json(url_cargos,cargos_restantes)

def menu_general():
    os.system("cls")
    print("=== Menu Cargos ===")
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
            crear_cargo()
        elif opcion == 2:
            print("Actualizar")
            actualizar_cargo()
        elif opcion == 3:
            print("Listar")
            listar_cargos()
        elif opcion == 4:
            print("Eliminar")
            eliminar_cargo()
        elif opcion == 5:
            print("Hasta Pronto")
            return #recordar que el return mata el ciclo While. 
        
        input("Presione Enter Para Continuar")

if __name__ == "__main__":
    iniciarPrograma()