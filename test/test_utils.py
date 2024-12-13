import unittest
from pkg.utils import crear_producto, agregar_al_carrito, calcular_total, aplicar_descuento

class TestUtils(unittest.TestCase):
    # ... pruebas existentes para crear_producto

    def test_agregar_al_carrito(self):
        # Agregar un producto a un carrito vacío
        carrito = []
        producto = crear_producto("Camiseta", 15)
        agregar_al_carrito(carrito, producto)
        self.assertEqual(carrito, [producto])

        # Agregar múltiples productos
        producto2 = crear_producto("Pantalón", 30)
        agregar_al_carrito(carrito, producto2)
        self.assertEqual(len(carrito), 2)

    def test_calcular_total(self):
        # Carrito vacío
        carrito = []
        self.assertEqual(calcular_total(carrito), 0)

        # Carrito con un producto
        carrito = [crear_producto("Libro", 20)]
        self.assertEqual(calcular_total(carrito), 20)

        # Carrito con múltiples productos
        carrito = [crear_producto("Zapatos", 50), crear_producto("Gorra", 10)]
        self.assertEqual(calcular_total(carrito), 60)

    def test_aplicar_descuento(self):
        # Descuento válido
        total = 100
        descuento = 0.2
        self.assertEqual(aplicar_descuento(total, descuento), 80)

        # Descuento máximo (100%)
        total = 50
        descuento = 1
        self.assertEqual(aplicar_descuento(total, descuento), 0)

        # Descuento negativo (no aplica descuento)
        total = 80
        descuento = -0.1
        self.assertEqual(aplicar_descuento(total, descuento), 80)