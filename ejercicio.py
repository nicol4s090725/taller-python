
from funcion import agregar_producto, mostrar_recibo

mi_carrito = []

print("--- BIENVENIDO AL SUPERMERCADO ---")

while True:
    print("1. Agregar producto")
    print("2. Ver recibo y salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_producto(mi_carrito)
    elif opcion == "2":
        mostrar_recibo(mi_carrito)
        break 
    else:
        print("Opción no válida, intenta de nuevo.")
