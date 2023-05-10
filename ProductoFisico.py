from Producto import Producto
from datetime import datetime

class ProductoFisico:
    def __init__(self, codigo_fisico: str, producto: Producto|dict, stock: int, fecha_expiracion: datetime|str) -> None:
        self.codigo_fisico: str = codigo_fisico
        self.stock: int = stock
        
        if isinstance(fecha_expiracion, str):
            self.fecha_expiracion: datetime = datetime.fromisoformat(fecha_expiracion)
        elif isinstance(fecha_expiracion, datetime):
            self.fecha_expiracion: datetime = fecha_expiracion

        if isinstance(producto, Producto):
            self.producto: Producto = producto
        elif isinstance(producto, dict):
            self.producto = Producto(**producto)
        
    
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