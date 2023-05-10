from typing import List
from datetime import datetime

from Farmaceutico import Farmaceutico
from ProductoFisico import ProductoFisico

class Venta:
    def __init__(self, empleado: Farmaceutico|dict, fecha: datetime) -> None:
        self.cantidades: List[int] = list()
        self.productos: List[ProductoFisico] = list()
        self.fecha: datetime = fecha
        if isinstance(empleado, Farmaceutico):
            self.empleado: Farmaceutico = empleado
        elif isinstance(empleado, dict):
            self.empleado = Farmaceutico(**empleado)

    def agregar(self, producto_fisico: ProductoFisico, cantidad: int) -> None:
        if (producto_fisico in self.productos):
            self.cantidades[self.productos.index(producto_fisico)] += cantidad
        else:
            self.productos.append(producto_fisico)
            self.cantidades.append(cantidad)

    def remover(self, producto_fisico: ProductoFisico, cantidad: int) -> bool:
        if (cantidad == 0):
            return False
        if (producto_fisico in self.productos):
            if (self.cantidades[self.productos.index(producto_fisico)] - cantidad >= 0):
                self.cantidades[self.productos.index(producto_fisico)] -= cantidad
                return True
            else:
                return False
        else:
            return False

    def mostrar_productos(self) -> None:
        for p_f in self.productos:
            print("---------------------------------------------")
            print(p_f.mostrar_producto())
        print("---------------------------------------------")