# main.py

from functions import (
    cargar_productos,
    ingresar,
    editar,
    buscar,
    mostrar,
    eliminar,
    CantProductos
)

def opcionmenu():
    print("Seleccione una opcion:")
    print("1. Ingresar producto")
    print("2. Editar producto")
    print("3. Buscar producto")
    print("4. Mostrar productos")
    print("5. Eliminar producto")
    print("0. Salir")
    return int(input("Opcion: "))

def procesar(opcion):
    if opcion == 1:
        ingresar()
    elif opcion == 2:
        editar(CantProductos)
    elif opcion == 3:
        buscar(CantProductos)
    elif opcion == 4:
        mostrar(CantProductos)
    elif opcion == 5:
        eliminar(CantProductos)
    elif opcion == 0:
        pass
    else:
        print("Opción inválida.")

cargar_productos()

while True:
    opcion = opcionmenu()
    if opcion == 0:
        break
    procesar(opcion)
