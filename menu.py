# main.py

# Importa todas las funciones y clases de los archivos tienda.py, cliente.py y producto.py
from tienda import *
from cliente import *
from producto import *

# Define una función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    # Imprime el menú
    print("\nMenu:")
    print("1. Agregar cliente")
    print("2. Ver clientes")
    print("3. Comprar producto")
    print("4. Mostrar carrito de cliente")
    print("5. Mostrar productos disponibles")
    print("6. Salir")
    # Solicita al usuario que seleccione una opción y la devuelve
    return input("Seleccione una opción: ")

# Define la función principal del programa
def main():
    # Crea un objeto tienda utilizando la función crear_tienda() (que se espera que esté definida en tienda.py)
    tienda = crear_tienda()

    # Bucle principal del programa
    while True:
        # Obtiene la opción del usuario llamando a la función mostrar_menu()
        opcion = mostrar_menu()

        # Evalúa la opción del usuario y realiza la acción correspondiente
        if opcion == '1':
            agregar_cliente(tienda)
        elif opcion == '2':
            mostrar_clientes(tienda)
        elif opcion == '3':
            comprar_producto(tienda)
        elif opcion == '4':
            mostrar_carrito(tienda)
        elif opcion == '5':
            mostrar_productos(tienda)
        elif opcion == '6':
            # Guarda clientes y productos antes de salir y luego imprime un mensaje de despedida
            guardar_clientes(tienda)
            guardar_productos(tienda)
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            # Si el usuario ingresa una opción no válida, imprime un mensaje de error
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Verifica si este script se está ejecutando directamente
if __name__ == "__main__":
    # Llama a la función principal main() si el script se ejecuta directamente
    main()
