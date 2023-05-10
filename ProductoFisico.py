from Producto import Producto
from datetime import datetime

class ProductoFisico:
    def __init__(self, codigo_fisico: str, producto: Producto, stock: int, fecha_expiracion: datetime) -> None:
        self.codigo_fisico: str = codigo_fisico
        self.producto: Producto = producto
        self.stock: int = stock
        self.fecha_expiracion: datetime = fecha_expiracion
    
    def disminuir_stock(self, cantidad: int) -> bool:
        if self.stock - cantidad >= 0:
            self.stock -= cantidad
            return True
        else:
            return False

    def mostrar_producto(self) -> None:
        self.producto.mostrar_producto()
        print("Codigo_fisico: " + self.codigo_fisico, end=', ')
        print("Stock: " + str(self.stock), end=', ')
        print("Fecha de expiracion: " + str(self.fecha_expiracion))