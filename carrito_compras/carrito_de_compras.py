#script sencillo de uso de diccionarios en python
carrito = [
    {"id": 123, "nombre": "Laptop", "cantidad": 1},
    {"id": 321, "nombre": "Bateria", "cantidad": 1},
    {"id": 123, "nombre": "Laptop", "cantidad": 1},  # Laptop agregada de nuevo
    {"id": 425, "nombre": "Teclado", "cantidad": 1},
    {"id": 321, "nombre": "Bateria", "cantidad": 2},  # Bateria agregada de nuevo, quizás con más cantidad
    {"id": 123, "nombre": "Laptop", "cantidad": 1},  # Otra vez Laptop
]

#procesa carrito
carrito_agrupado = {}
for producto in carrito:
    id_actual = producto["id"]
    nombre_actual = producto["nombre"]
    cantidad_actual = producto["cantidad"]

    #verifica si el producto ya existe en el carrito
    if id_actual in carrito_agrupado:
        #si existe, actualiza la cantidad
        carrito_agrupado[id_actual]["cantidad"] += cantidad_actual
    else:
        #si no existe, agrega el producto
        carrito_agrupado[id_actual] = {"nombre": nombre_actual, "cantidad": cantidad_actual}

#convierte carrito en lista de productos agrupados
carrito_final = [{"id": id, "nombre": producto["nombre"], "cantidad": producto["cantidad"]} for id, producto in carrito_agrupado.items(
)]

#print carrito final
print("Productos agregados correctamente")
for producto in carrito_final:
    print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")

