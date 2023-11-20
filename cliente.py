def crear_cliente(nombre, direccion, correo, telefono):
    # Crea y devuelve un diccionario que representa a un cliente con información proporcionada
    return {"nombre": nombre, "direccion": direccion, "correo": correo, "telefono": telefono, "carrito": []}

def comprar_producto(cliente, producto, cantidad):
    # Añade un diccionario al carrito del cliente con información sobre el producto y la cantidad
    cliente["carrito"].append({"producto": producto, "cantidad": cantidad})

def mostrar_carrito(cliente):
    # Muestra el contenido del carrito de un cliente
    print(f"Carrito de {cliente['nombre']}:")
    for item in cliente["carrito"]:
        producto = item["producto"]
        cantidad = item["cantidad"]
        print(f"Producto: {producto['nombre']}, Cantidad: {cantidad}")
