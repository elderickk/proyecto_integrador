# functions.py

MaxInventario = 1000

class Producto:
    def __init__(self, marca, modelo, tipo, year, precio):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.year = year
        self.precio = precio

productos = []
CantProductos = 0

def cargar_productos():
    global CantProductos
    try:
        with open('inventario.txt', 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')
                productos.append(Producto(datos[0], datos[1], datos[2], int(datos[3]), float(datos[4])))
                CantProductos += 1
    except FileNotFoundError:
        with open('inventario.txt', 'w') as archivo:
            pass

def guardar_productos():
    with open('inventario.txt', 'w') as archivo:
        for producto in productos:
            archivo.write(f"{producto.marca},{producto.modelo},{producto.tipo},{producto.year},{producto.precio}\n")

def ingresar():
    global CantProductos
    if CantProductos < MaxInventario:
        marca = input("Ingrese la marca del producto: ")
        modelo = input("Ingrese el nombre del producto: ")
        tipo = input("Ingrese el tipo de producto: ")
        year = int(input("Ingrese el año: "))
        precio = float(input("Ingrese el precio: $"))
        productos.append(Producto(marca, modelo, tipo, year, precio))
        CantProductos += 1
        guardar_productos()

def editar(cantidadproductos):
    if cantidadproductos > 0:
        mostrar(cantidadproductos)
        index = int(input("Numero de producto a editar: ")) - 1
        if 0 <= index < CantProductos:
            print("Ingrese los nuevos datos")
            productos[index].marca = input("Marca del Producto: ")
            productos[index].modelo = input("Nombre del producto: ")
            productos[index].tipo = input("Tipo de producto: ")
            productos[index].year = int(input("Año: "))
            productos[index].precio = float(input("Precio: $"))
            guardar_productos()
        else:
            print("Número de producto inválido.")
    else:
        print("No existen productos para editar.")

def buscar(cantidadproductos):
    if cantidadproductos > 0:
        print("1. Tipo")
        print("2. Nombre")
        print("3. Año")
        opcionb = int(input("Seleccione una opcion: "))
        
        if opcionb == 1:
            tipo = input("Ingrese el tipo de producto: ")
            for i in range(CantProductos):
                if productos[i].tipo == tipo:
                    print(f"Producto {i+1}")
                    print(f"Tipo: {productos[i].tipo}")
                    print(f"Nombre: {productos[i].modelo}")
                    print(f"Año: {productos[i].year}")
                    print(f"Precio: ${productos[i].precio:.2f}")
        elif opcionb == 2:
            nombre = input("Ingrese el nombre del producto: ")
            for i in range(CantProductos):
                if productos[i].modelo == nombre:
                    print(f"Producto {i+1}")
                    print(f"Tipo: {productos[i].tipo}")
                    print(f"Nombre: {productos[i].modelo}")
                    print(f"Año: {productos[i].year}")
                    print(f"Precio: ${productos[i].precio:.2f}")
        elif opcionb == 3:
            year = int(input("Ingrese el año del producto: "))
            for i in range(CantProductos):
                if productos[i].year == year:
                    print(f"Producto {i+1}")
                    print(f"Tipo: {productos[i].tipo}")
                    print(f"Nombre: {productos[i].modelo}")
                    print(f"Año: {productos[i].year}")
                    print(f"Precio: ${productos[i].precio:.2f}")
        else:
            print("Opción inválida.")
    else:
        print("No existen productos para buscar.")

def mostrar(cantidadproductos):
    if cantidadproductos > 0:
        for i in range(cantidadproductos):
            print(f"--Producto {i+1}--")
            print(f"Nombre: {productos[i].modelo}")
            print(f"Marca: {productos[i].marca}")
            print(f"Tipo: {productos[i].tipo}")
            print(f"Año: {productos[i].year}")
            print(f"Precio: ${productos[i].precio:.2f}")
    else:
        print("No existen productos para mostrar.")

def eliminar(cantidadproductos):
    global CantProductos
    if cantidadproductos > 0:
        mostrar(cantidadproductos)
        index = int(input("Numero de producto a eliminar: ")) - 1
        if 0 <= index < CantProductos:
            productos.pop(index)
            CantProductos -= 1
            guardar_productos()
            print("Producto eliminado.")
        else:
            print("Número de producto inválido.")
    else:
        print("No existen productos para eliminar.")
