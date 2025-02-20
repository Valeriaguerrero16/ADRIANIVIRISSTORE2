import sys  # Importamos sys para poder cerrar el programa con sys.exit()

# Lista para almacenar los productos del carrito
carrito = []

# Diccionario de productos disponibles con su precio
productos_disponibles = {
    "1": ("Labial Rare Beauty", 20.0),
    "2": ("Rímel Benefit", 25.0),
    "3": ("Base Sephora", 30.0),
    "4": ("Rubor Rare Beauty", 22.0),
    "5": ("Paleta de sombras Benefit", 35.0)
}

def mostrar_menu():
    """Muestra el menú principal con las opciones disponibles."""
    print("\n--- Adrianiviris Store ---")
    print("1. Agregar productos al carrito")
    print("2. Ver carrito")
    print("3. Eliminar productos")
    print("4. Pagar")
    print("5. Salir")

def agregar_producto():
    """Permite al usuario agregar productos al carrito."""
    print("\nProductos disponibles:")
    for key, (nombre, precio) in productos_disponibles.items():
        print(f"{key}. {nombre} - ${precio:.2f}")
    
    opcion = input("Ingrese el número del producto que desea agregar: ")
    if opcion in productos_disponibles:
        carrito.append(productos_disponibles[opcion])
        print(f"{productos_disponibles[opcion][0]} agregado al carrito.")
    else:
        print("Opción inválida.")

def ver_carrito():
    """Muestra los productos en el carrito y el total a pagar."""
    if not carrito:
        print("\nEl carrito está vacío.")
    else:
        print("\nProductos en el carrito:")
        for i, (nombre, precio) in enumerate(carrito, 1):
            print(f"{i}. {nombre} - ${precio:.2f}")
        total = sum(map(lambda x: x[1], carrito))  # Calcula el total a pagar
        print(f"Total a pagar: ${total:.2f}")

def eliminar_producto():
    """Permite al usuario eliminar un producto del carrito."""
    if not carrito:
        print("\nEl carrito está vacío.")
        return
    
    ver_carrito()
    try:
        indice = int(input("Ingrese el número del producto que desea eliminar: ")) - 1
        if 0 <= indice < len(carrito):
            eliminado = carrito.pop(indice)
            print(f"{eliminado[0]} eliminado del carrito.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada no válida. Intente de nuevo.")

def pagar():
    """Finaliza la compra y vacía el carrito si el usuario confirma el pago."""
    if not carrito:
        print("\nNo hay productos en el carrito para pagar.")
        return
    
    ver_carrito()
    confirmacion = input("¿Desea proceder con el pago? (sí/no): ").strip().lower()
    if confirmacion == "sí":
        print("Pago realizado con éxito. Gracias por su compra!")
        carrito.clear()  # Vacía el carrito después del pago
    else:
        print("Pago cancelado.")

def main():
    """Ejecuta el programa, mostrando el menú y procesando la elección del usuario."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_carrito()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            pagar()
        elif opcion == "5":
            print("Gracias por visitar Adrianiviris Store. ¡CHAITO!")
            sys.exit()  # Termina la ejecución del programa
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
