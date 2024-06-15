import os
import csv

os.system("cls")
FIELDNAMES_PRODUCTOS = ['id_producto', 'nombre_producto', 'precio', 'stock']

DIR_PRODUCTOS = "./productos.csv"

def leer_archivo_csv(DIR_PRODUCTOS):
    try:
        with open(DIR_PRODUCTOS, mode="r", newline='') as archivo:
            data = csv.DictReader(archivo)
            return list(data)
    except FileNotFoundError:
        return []
    
def guardar_archivo_csv(DIR_PRODUCTOS, data, FIELDNAMES_PRODUCTOS):
    try:
        with open(DIR_PRODUCTOS, mode="w", newline='',encoding="utf-8") as archivo:
            data_csv = csv.DictWriter(archivo, fieldnames=FIELDNAMES_PRODUCTOS)
            data_csv.writeheader()
            data_csv.writerows(data)
    except Exception as e:
        print(f"Error al guardar archivo: {e}")

def listar_productos():
    import os
    os.system("cls")
    print("=== Listado De Productos ===")
    productos = leer_archivo_csv(DIR_PRODUCTOS)
    fieldnames = ['id_producto','nombre_producto','precio','stock']

    fieldnames_format = "{:<15} {:<30} {:<15} {:<15}"
    print(fieldnames_format.format(*fieldnames))

    for producto in productos:
        print("{:<15} {:<30} {:<15} {:<15}".format(
            producto['id_producto'],
            producto['nombre_producto'],
            producto['precio'],
            producto['stock']
        ))

def menu_general():
    os.system("cls")

    print("=== Menu ===")
    print("1. Crear")
    print("2. Actualizar")
    print("3. Listar")
    print("4. Eliminar")
    print("5. Salir")

def seleccionar_opcion(maxOpcion):
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
            if 0 <= opcion <= maxOpcion:
                return opcion
            else:
                print("Error: Debes seleccionar una de las opciones disponibles.")
        except ValueError:
            print("Error: Debes ingresar un número.")
        input("Presione Enter para continuar")

def crear_productos():
    os.system("cls")
    print("<=== Registrar Nuevo Producto ===>")
    productos = leer_archivo_csv(DIR_PRODUCTOS)

    id_producto = input("Ingrese id Producto >> ")
    nombre_producto = input("Ingrese nombre producto >> ")
    precio = int(input("Ingrese precio producto >> "))
    stock = int(input("Ingrese stock del producto >> "))

    nuevo_producto = {
        "id_producto": id_producto,
        "nombre_producto": nombre_producto,
        "precio": precio,
        "stock": stock
    }

    productos.append(nuevo_producto)
    
    guardar_archivo_csv(DIR_PRODUCTOS, productos, FIELDNAMES_PRODUCTOS)

def modificar_producto():
    os.system("cls")
    print("=== Modificar Producto ===")
    productos = leer_archivo_csv(DIR_PRODUCTOS)

    id_producto = input("Ingresa el id del producto a modificar >> ")

    nombre_producto = input("Ingrese el nombre del producto >> ")
    precio = int(input("Ingrese precio del producto >> "))
    stock = int(input("Ingrese stock de producto >> "))

    for producto in productos:
        if producto['id_producto'] == id_producto:
            producto['nombre_producto'] = nombre_producto
            producto['precio'] = precio
            producto['stock'] = stock
            break

    guardar_archivo_csv(DIR_PRODUCTOS,productos,FIELDNAMES_PRODUCTOS)

def eliminar_producto():
    os.system("cls")
    print("=== Eliminar Producto ===")
    
    productos = leer_archivo_csv(DIR_PRODUCTOS)
    listar_productos()
    id_producto = input("Ingrese el id de producto a eliminar >> ")

    productos_en_lista = []
    for producto in productos:
        if producto['id_producto'] != id_producto:
            productos_en_lista.append(producto)

    guardar_archivo_csv(DIR_PRODUCTOS,productos_en_lista,FIELDNAMES_PRODUCTOS)



def iniciarPrograma():
    while True:
        menu_general()
        opcion = seleccionar_opcion(5)
        if opcion == 1:
            crear_productos()
        elif opcion == 2:
            modificar_producto()
        elif opcion == 3:
            #print("Listar")
            listar_productos()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            print("Hasta Pronto")
            return #recordar que el return mata el ciclo While. 
        
        input("Presione Enter Para Continuar")

if __name__ == "__main__":
    iniciarPrograma()
