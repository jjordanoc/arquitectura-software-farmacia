from Venta import Venta
from Producto import Producto
from ProductoFisico import ProductoFisico
from typing import Optional, Dict, List
from Farmaceutico import Farmaceutico
from datetime import datetime

class Tienda:
    def __init__(self, direccion: str) -> None:
        self.direccion: str = direccion
        self.catalogo: Dict[str, Producto] = dict()
        self.productos: Dict[str, ProductoFisico] = dict()
        self.empleados: Dict[str, Farmaceutico] = dict()
        self.ventas: List[Venta] = list()

    def mostrar_ventas(self) -> None:
        for v in self.ventas:
            print(f'Cantidad vendida: {v.cantidades}, empleado: {v.empleado}, fecha: {v.fecha}, productos:')
            for p in v.productos:
                p.mostrar_producto()

    def realizar_venta(self) -> bool:
        dni: str = input("Ingrese DNI del farmaceutico que atiende: ")
        empleado: Optional[Farmaceutico] = self.empleados.get(dni)
        if (empleado is None):
            print("Debe ingresar el DNI de un empleado contratado.")
            return False
        venta: Venta = Venta(empleado, datetime.now())
        while True:
            codigo_fisico: str = input("Ingrese el codigo del producto a comprar (o -1 para dejar de agregar productos): ")
            if (int(codigo_fisico) == -1):
                break
            producto_fisico: Optional[ProductoFisico] = self.productos.get(codigo_fisico)
            if (producto_fisico is None):
                print("Debe ingresar el codigo de un producto existente.")
                return False
            print("Producto:")
            producto_fisico.mostrar_producto()
            cantidad: int = int(input("Ingresar la cantidad de este producto a adquirir: "))
            if not producto_fisico.disminuir_stock(cantidad):
                print("No hay stock suficiente de ese producto, intente de nuevo.")
            else:
                venta.agregar(producto_fisico, cantidad)
        self.ventas.append(venta)
        return True
    
    def abastecer_productos(self) -> bool:
        while True:
            codigo: str = input("Ingrese el codigo del producto del catalogo a abastecer (o -1 para dejar de agregar productos): ")
            if (int(codigo) == -1):
                break
            producto: Producto = self.productos.get(codigo)
            if producto is None:
                print("No existe dicho producto en el catalogo.")
                return False
            codigo_fisico: str = input("Ingrese el codigo fisico del nuevo producto: ")
            fecha_expiracion: datetime = datetime.strptime(input("Ingrese la fecha de expiracion del nuevo producto: "))
            stock: int = int(input("Ingrese la cantidad de este producto que desea abastecer: "))
            producto_fisico: ProductoFisico = ProductoFisico(codigo_fisico, producto, stock, fecha_expiracion)
            self.productos.update({codigo_fisico, producto_fisico})
        return True
        

    def actualizar_catalogo(self) -> bool:
        while True:
            codigo: str = input("Ingrese codigo del producto a agregar al catálogo (o -1 para dejar de agregar productos): ")
            if (int(codigo) == -1):
                break
            nombre: str = input("Ingrese nombre: ")
            presentacion: str = input("Ingrese presentacion: ")
            descripcion: str = input("Ingrese descripcion: ")
            precio: float = input("Ingrese precio: ")
            categoria: str = input("Ingrese categoria: ")
            url_imagen: str = input("Ingrese url de imagen: ")
            producto: Producto = Producto(codigo, nombre, presentacion, descripcion, precio, categoria, url_imagen)
            self.catalogo.update({codigo: producto})
        return True

    def contratar_empleados(self) -> bool:
        while True:
            dni: str = input("Ingrese DNI del farmaceutico (o -1 para dejar de contratar): ")
            if (int(dni) == -1):
                break
            nombre: str = input("Ingrese nombre del farmaceutico: ")
            empleado: Farmaceutico = Farmaceutico(dni, nombre)
            self.empleados.update({dni: empleado})
        return True
    
    def mostrar_productos(self) -> None:
        for codigo_fisico, producto_fisico in self.productos.items():
            producto_fisico.mostrar_producto()
    
    def mostrar_catalogo(self) -> None:
        for codigo, producto in self.catalogo.items():
            producto.mostrar_producto()

    def mostrar_empleados(self) -> None:
        for dni, empleado in self.empleados.items():
            empleado.mostrar_informacion()
