import sys  # Para cuando el usuaro quiera salir 

# Lista donde se guardarán los productos que el usuario agregue
carrito = []

# Diccionario que contiene los productos disponibles junto con sus precios
productos_disponibles = {
    "1": ("Labial Rare Beauty", 20.0),
    "2": ("Rímel Benefit", 25.0),
    "3": ("Base Sephora", 30.0),
    "4": ("Rubor Rare Beauty", 22.0),
    "5": ("Paleta de sombras Benefit", 35.0)
}

# ----------------------------------------------------------------------------------------------------------
def mostrar_menu():
    """Muestra las opciones que el usuario puede elegir."""
    print("\n--- Adrianiviris Store ---")
    print("1. Agregar productos al carrito")
    print("2. Ver carrito")
    print("3. Eliminar productos")
    print("4. Pagar")
    print("5. Salir")

# -------------------------------------------------------------------------------------------------------------
def agregar_producto():
    """Permite agregar productos al carrito."""
    print("\nProductos disponibles:")
    for key, (nombre, precio) in productos_disponibles.items():  # Recorre los productos y los mostramos
        print(f"{key}. {nombre} - ${precio:.2f}")
    
    opcion = input("Ingrese el número del producto que desea agregar: ")
    if opcion in productos_disponibles:  # Si la opción ingresada está en la lista de productos
        carrito.append(productos_disponibles[opcion])  # Agrega el producto al carrito
        print(f"{productos_disponibles[opcion][0]} agregado al carrito.")
    else:
        print("Opción inválida.")  # Si el usuario ingresa una opción incorrecta

# ----------------------------------------------------------------------------------------------------------
def ver_carrito():
    """Muestra los productos agregados al carrito y el total a pagar."""
    if not carrito:  # Si el carrito está vacío
        print("\nEl carrito está vacío.")
    else:
        print("\nProductos en el carrito:")
        for i, (nombre, precio) in enumerate(carrito, 1):  # Recorre los productos del carrito
            print(f"{i}. {nombre} - ${precio:.2f}")
        total = sum(map(lambda x: x[1], carrito))  # Calcula el total sumando los precios
        print(f"Total a pagar: ${total:.2f}")

# -----------------------------------------------------------------------------------------------------------
def eliminar_producto():
    """Permite eliminar un producto del carrito."""
    if not carrito:  # Si el carrito está vacío
        print("\nEl carrito está vacío.")
        return  # Salimos de la función
    
    ver_carrito()  # Muestra el carrito antes de eliminar
    try:
        indice = int(input("Ingrese el número del producto que desea eliminar: ")) - 1  # Se obtiene el índice
        if 0 <= indice < len(carrito):  # Verifica que el índice sea válido
            eliminado = carrito.pop(indice)  # Elimina el producto del carrito
            print(f"{eliminado[0]} eliminado del carrito.")
        else:
            print("Número inválido.")  # Mensajito  de error si el número no es válido
    except ValueError:  # Si el usuario ingresa algo que no es un número
        print("Entrada no válida. Intente de nuevo.")

# --------------------------------------------------------------------------------------------------------------
def pagar():
    """Finaliza la compra y vacía el carrito si el usuario confirma el pago."""
    if not carrito:  # Si el carrito está vacío, no hay nada que pagar
        print("\nNo hay productos en el carrito para pagar.")
        return
    
    ver_carrito()  # Muestra el carrito antes de proceder con el pago
    confirmacion = input("¿Desea proceder con el pago? (sí/no): ").strip().lower()  # Pide la confirmación
    if confirmacion == "sí":  # Si el usuario confirma el pago
        print("Pago realizado con éxito. ¡Gracias por su compra!")
        carrito.clear()  # Vacia el carrito después de pagar
    else:
        print("Pago cancelado.")  # Mensajito si el usuario cancela el pago

# -----------------------------------------------------------------------------------------------------------------
def main():
    """Muestra el menú y ejecuta la opción elegida por el usuario."""
    while True:  # Bucle infinito para que el menú siga apareciendo hasta que el usuario elija salir
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
            sys.exit()  # Cierra el programa
        else:
            print("Opción no válida. Intente de nuevo.")  # Si el usuario elige una opción incorrecta

# ---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":  # Punto de entrada del programa
    main()  # Llamamos a la función principal para iniciar el programa

