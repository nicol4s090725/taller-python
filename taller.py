# punto 1
nota1 = float(input("ingresa tu primera nota: "))
nota2 = float(input("ingresa tu segunda nota: "))
nota3 = float(input("ingresa tu cuarta nota: "))
nota4 = float(input("ingresa tu cuarta nota: "))
def notas(nota1,nota2,nota3,nota4):
  promedio = (nota1+nota2+nota3+nota4)/4
  return promedio
promedio = (nota1+nota2+nota3+nota4)/4
print("tu definitiva es: ", promedio  )
  
if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
      print(" la nota mayor es: ", nota1)
elif nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
      print("la mayor nota es:", nota2)
elif nota3 > nota2 and nota3 > nota1 and nota3 > nota4:
  print("la mayor nota es: ", nota3)
else:
  print( " la mayor nota es: ", nota4)

if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
      print(" la nota menor es: ", nota1)
elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
      print("la menor nota es:", nota2)
elif nota3 < nota2 and nota3 < nota1 and nota3 < nota4:
  print("la menor nota es: ", nota3)
else:
  print( " la menor nota es: ", nota4)


#punto 2
estudiantes = [
    ("ana", 4.5),
    ("luis",2.8),
    ("maria",3.2),
    ("pedro", 2.5),
    ("sofia",4.0)
]
def aprobados(lista):
    resultado = []
    for nombre, nota in lista:
        if nota >= 3.0:
            resultado.append((nombre,nota))
    return resultado
estudiantes_aprobados= aprobados(estudiantes)
print("estudiantes aprobados: ")
for nombre, nota in estudiantes_aprobados:
    print(nombre, "con nota", nota)

#punto3

agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado con teléfono {telefono}")

def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"{nombre} -> {agenda[nombre]}")
    else:
        print(f"El contacto {nombre} no existe en la agenda")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado")
    else:
        print(f"No se encontró el contacto {nombre}")


agregar_contacto("Ana", "123456")
agregar_contacto("Luis", "987654")
buscar_contacto("Ana")
eliminar_contacto("Luis")
buscar_contacto("Luis")

#punto 4
inventario = {
    "manzanas": {"precio": 1500, "cantidad": 10},
    "bananas": {"precio": 2205, "cantidad": 8},
    "naranjas": {"precio": 1000, "cantidad": 5}
}


def agregar_producto(nombre, precio, cantidad):
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print(f"Producto {nombre} agregado con precio {precio} y cantidad {cantidad}")

def valor_total():
    total = 0
    for producto, datos in inventario.items():
        total += datos["precio"] * datos["cantidad"]
    return total


agregar_producto("peras", 2500, 7)

print("Inventario actual:")
for producto, datos in inventario.items():
    print(f"{producto}: precio {datos['precio']}, cantidad {datos['cantidad']}")

print("Valor total del inventario:", valor_total())

#punto 5
palabras = ["perro", "gato", "pez", "gato", "perro"]
frecuencias = {}
for palabra in palabras:
  if palabra in frecuencias:
    frecuencias[palabra]+=1
  else:
    frecuencias[palabra]= 1
print("frecuencia en palabras")
for palabra, cantidad in frecuencias.items():
  print(palabra , ":", cantidad)

#punto 6 
# Diccionario con temperaturas semanales por ciudad
temperaturas = {
    "Bogotá": [18, 20, 19, 21, 22, 20, 19],
    "Medellín": [25, 26, 27, 28, 29, 27, 26],
    "Cali": [30, 31, 32, 33, 34, 32, 31]
}

for ciudad, lista in temperaturas.items():
    # Inicializamos con el primer valor de la lista
    mas_frio = lista[0]
    mas_caliente = lista[0]

    # Recorremos todas las temperaturas de la ciudad
    for temp in lista:
        if temp < mas_frio:
            mas_frio = temp
        if temp > mas_caliente:
            mas_caliente = temp

    print(f"{ciudad}: más fría = {mas_frio}, más caliente = {mas_caliente}")

#punto 7
rangos = [
    ((4.5, 5.0), "A"),
    ((4.0, 4.4), "B"),
    ((3.0, 3.9), "C"),
    ((2.0, 2.9), "D"),
    ((0.0, 1.9), "F")
]

def convertir_nota(nota):
    if nota >= 4.5:
        return "A"
    elif nota >= 4.0:
        return "B"
    elif nota >= 3.0:
        return "C"
    elif nota >= 2.0:
        return "D"
    else:
        return "F"
estudiantes = [
    ("Ana", 4.7),
    ("Luis", 3.5),
    ("María", 2.8),
    ("Pedro", 1.5),
    ("Sofía", 4.2)
]
print("Reporte de estudiantes:")
for nombre, nota in estudiantes:
    letra = convertir_nota(nota)
    print(nombre, "→ nota numérica:", nota, ", nota en letra:", letra)

#punto 8 


carrito = []


def agregar_producto(nombre, precio, cantidad=1):
    carrito.append((nombre, precio, cantidad))
    print(f"{cantidad} x {nombre} agregado(s) al carrito")


def aplicar_descuento(total, porcentaje):
    descuento = total * (porcentaje / 100)
    return total - descuento


def calcular_total():
    total = 0
    for nombre, precio, cantidad in carrito:
        total += precio * cantidad
    return total


agregar_producto("Camisa", 50, 2)
agregar_producto("Zapatos", 120, 1)
agregar_producto("Pantalón", 80, 1)

total = calcular_total()
print("Total sin descuento:", total)


total_con_descuento = aplicar_descuento(total, 10)
print("Total con 10% de descuento:", total_con_descuento)

#punto 9
productos = [
    ("Camisa", "Ropa"),
    ("Pantalón", "Ropa"),
    ("Zapatos", "Calzado"),
    ("Sandalias", "Calzado"),
    ("Laptop", "Electrónica"),
    ("Celular", "Electrónica")
]


agrupados = {}

for producto, categoria in productos:
    if categoria in agrupados:
        agrupados[categoria].append(producto)  
    else:
        agrupados[categoria] = [producto]       

print("Productos agrupados por categoría:")
for categoria, lista in agrupados.items():
    print(categoria, ":", lista)


#punto 10


candidatos = ["Ana", "Luis", "María"]


votos = ["Ana", "Luis", "Ana", "Pedro", "María", "Luis", "Ana"]


conteo = {}
for nombre in candidatos:
    conteo[nombre] = 0

votos_invalidos = 0


for voto in votos:
    if voto in candidatos:
        conteo[voto] += 1    
    else:
        votos_invalidos += 1 


total_validos = 0
for cantidad in conteo.values():
    total_validos += cantidad


ganador = None
max_votos = 0
for candidato, cantidad in conteo.items():
    if cantidad > max_votos:
        max_votos = cantidad
        ganador = candidato


porcentaje = (max_votos / total_validos) * 100


print("Resultados:")
for candidato, cantidad in conteo.items():
    print(candidato, ":", cantidad, "votos")
print("Votos inválidos:", votos_invalidos)
print("Ganador:", ganador, "con", round(porcentaje, 2), "% de los votos válidos")

