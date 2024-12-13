import random

# Función para crear un producto
def crear_producto(nombre, precio):
    return {'nombre': nombre, 'precio': int(precio)}

# Función para agregar un producto al carrito
def agregar_al_carrito(carrito, producto):
    carrito.append(producto)

# Función para calcular el total del carrito
def calcular_total(carrito):
    return sum(producto['precio'] for producto in carrito)

# Función para aplicar un descuento
def aplicar_descuento(total, descuento):
    return total * (1 - descuento)