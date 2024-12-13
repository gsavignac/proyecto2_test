import pkg.utils

def obtener_datos_producto():
    while True:
        nombre = input('Ingrese el nombre del producto: ')
        if nombre:
            break
        print("El nombre del producto no puede estar vacío.")

    while True:
        try:
            precio = float(input('Ingrese el precio del producto: '))
            if precio > 0:
                break
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            print("Ingrese un precio válido.")

    return nombre, precio


# Obtener datos de los productos con validación
producto1, precio1 = obtener_datos_producto()
producto2, precio2 = obtener_datos_producto()
producto3, precio3 = obtener_datos_producto()


# Función lambda para aplicar un descuento del 10%
descuento_10 = lambda total: pkg.utils.aplicar_descuento(total, 0.1)

productos = [
    pkg.utils.crear_producto( producto1, precio1 ),
    pkg.utils.crear_producto( producto2, precio2 ),
    pkg.utils.crear_producto( producto3, precio3 )
]

# Crear un carrito vacío
carrito = []

# Agregar productos al carrito
pkg.utils.agregar_al_carrito(carrito, productos[0])
pkg.utils.agregar_al_carrito(carrito, productos[1])

# Calcular el total
total = pkg.utils.calcular_total(carrito)
print('Total sin descuento:', total)

# Aplicar descuento y mostrar el nuevo total
total_con_descuento = descuento_10(total)
print('Total con descuento del 10%:', total_con_descuento)