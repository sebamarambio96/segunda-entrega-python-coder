from datetime import datetime


class Tiendas():
    paga_impuestos = True

    def __init__(self, nombre):
        self.nombre_tienda = nombre


class Productos(Tiendas):
    def __init__(self, nombre_tienda, nombre_producto, precio):
        super().__init__(nombre_tienda)
        self.nombre_producto = nombre_producto
        self.precio = precio


class Clientes(Tiendas):
    def __init__(self, nombre_tienda, rut, productos, descuento):
        super().__init__(nombre_tienda)
        self.rut = rut
        self.productos = productos
        self.fecha = datetime.now()
        self.descuento = descuento

    def __str__(self):
        return f"Rut del cliente: {self.rut}, Fecha de inscripción: {self.fecha}, Compró en la tienda: {self.nombre_tienda}"

    def calcular_total(self):
        total = 0
        for x in self.productos:
            total += x.precio
        return total

    def detalle_de_compra(self):
        boleta = 'DETALLE DE COMPRA:\n'
        for x in self.productos:
            boleta += f"- Producto: '{x.nombre_producto}' Precio: ${x.precio}\n"
        boleta += f"PRECIO TOTAL: ${self.calcular_total()}"
        return boleta

