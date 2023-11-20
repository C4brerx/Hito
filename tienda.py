# tienda.py

# Define una función para crear una tienda con listas vacías de clientes y productos
def crear_tienda():
    return {"clientes": [], "productos": []}

# Añade un cliente a la lista de clientes de la tienda
def agregar_cliente(tienda, cliente):
    tienda["clientes"].append(cliente)

# Muestra la información de todos los clientes de la tienda
def mostrar_clientes(tienda):
    print("Lista de clientes:")
    for cliente in tienda["clientes"]:
        print(f"Nombre: {cliente['nombre']}, Dirección: {cliente['direccion']}, Correo: {cliente['correo']}, Teléfono: {cliente['telefono']}")

# Guarda la información de los clientes en un archivo
def guardar_clientes(tienda):
    with open(tienda["archivo_clientes"], 'w') as archivo:
        for cliente in tienda["clientes"]:
            linea = f"{cliente['nombre']},{cliente['direccion']},{cliente['correo']},{cliente['telefono']}\n"
            archivo.write(linea)

# Carga la información de los clientes desde un archivo
def cargar_clientes(tienda):
    try:
        with open(tienda["archivo_clientes"], 'r') as archivo:
            for linea in archivo:
                datos_cliente = linea.strip().split(',')
                nombre, direccion, correo, telefono = datos_cliente
                cliente = {"nombre": nombre, "direccion": direccion, "correo": correo, "telefono": telefono, "carrito": []}
                tienda["clientes"].append(cliente)
    except FileNotFoundError:
        pass

# Añade un producto a la lista de productos de la tienda
def agregar_producto(tienda, producto):
    tienda["productos"].append(producto)

# Muestra la información de todos los productos de la tienda
def mostrar_productos(tienda):
    print("Lista de productos:")
    for producto in tienda["productos"]:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")

# Guarda la información de los productos en un archivo
def guardar_productos(tienda):
    with open(tienda["archivo_productos"], 'w') as archivo:
        for producto in tienda["productos"]:
            linea = f"{producto['nombre']},{producto['precio']}\n"
            archivo.write(linea)

# Carga la información de los productos desde un archivo
def cargar_productos(tienda):
    try:
        with open(tienda["archivo_productos"], 'r') as archivo:
            for linea in archivo:
                datos_producto = linea.strip().split(',')
                nombre, precio = datos_producto
                producto = {"nombre": nombre, "precio": float(precio)}
                tienda["productos"].append(producto)
    except FileNotFoundError:
        pass
