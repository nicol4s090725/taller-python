
def agregar_producto(lista_carrito):
    nombre = input("Nombre del producto: ")
    precio = float(input(f"Precio de {nombre}: "))
    cantidad = int(input(f"Cantidad de {nombre}: "))
    
    item = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    lista_carrito.append(item)
    print(f" {nombre} agregado correctamente.\n")

def mostrar_recibo(lista_carrito):
    print("\n" + "="*20)
    print("      RECIBO")
    print("="*20)
    total_general = 0
    
    for p in lista_carrito:
        subtotal = p["precio"] * p["cantidad"]
        total_general += subtotal
        print(f"{p['nombre']} x{p['cantidad']}: ${subtotal}")
    
    print("-" * 20)
    print(f"TOTAL A PAGAR: ${total_general}")
    print("="*20)