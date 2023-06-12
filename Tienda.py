from Venta import Venta
from Producto import Producto
from ProductoFisico import ProductoFisico
from typing import Optional, Dict, List
from Farmaceutico import Farmaceutico
from datetime import datetime, date
from json import JSONEncoder
from collections import namedtuple
import json

class MyEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, (date, datetime)):
            return object.isoformat()
        if isinstance(object, Farmaceutico) or isinstance(object, Producto) or isinstance(object, ProductoFisico) or isinstance(object, Tienda) or isinstance(object, Venta) :
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)

class Tienda:
    def __init__(self, direccion: str) -> None:
        self.direccion: str = direccion
        self.catalogo: Dict[str, Producto] = dict()
        self.productos: Dict[str, ProductoFisico] = dict()
        self.empleados: Dict[str, Farmaceutico] = dict()
        self.ventas: List[Venta] = list()

    def load(self) -> None:
        db = open("Tienda.json")
        tienda_dict = json.load(db)
        self.direccion = tienda_dict["direccion"]

        for venta in tienda_dict["ventas"]:            
            self.ventas.append(Venta(**venta))

        for key in tienda_dict["productos"]:
            self.productos[key] = ProductoFisico(**tienda_dict["productos"][key])

        for key in tienda_dict["catalogo"]:
            if self.catalogo.get(key) is None:
                self.catalogo[key] = Producto(**tienda_dict["catalogo"][key])

        for key in tienda_dict["empleados"]:
            if self.empleados.get(key) is None:
                self.empleados[key] = Farmaceutico(**tienda_dict["empleados"][key])

        db.close()

    def save(self) -> None:
        db = open("Tienda.json", 'w')
        db.write(MyEncoder().encode(self))
        db.close()

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
        venta: Venta = Venta(cantidades=None, productos=None, empleado=empleado, fecha=datetime.now())
        while True:
            codigo_fisico: str = input("Ingrese el codigo del producto a comprar (o -1 para dejar de agregar productos): ")
            if (codigo_fisico == "-1"):
                break
            
            existir : bool = venta.verificar_producto(codigo_fisico)
            if not existir: return False

            producto_fisico: Optional[ProductoFisico] = self.productos.get(codigo_fisico)
  
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
            producto: Producto = self.catalogo.get(codigo)
            if producto is None:
                print("No existe dicho producto en el catalogo.")
                return False
            codigo_fisico: str = input("Ingrese el codigo fisico del nuevo producto: ")
            fecha_expiracion: datetime = datetime.strptime(input("Ingrese la fecha de expiracion del nuevo producto: "), "%d-%m-%Y")
            stock: int = int(input("Ingrese la cantidad de este producto que desea abastecer: "))
            producto_fisico: ProductoFisico = ProductoFisico(codigo_fisico=codigo_fisico, producto=producto,stock=stock, fecha_expiracion=fecha_expiracion)
            self.productos.update({codigo_fisico: producto_fisico})
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
            producto: Producto = Producto(codigo=codigo,nombre=nombre,presentacion=presentacion,descripcion=descripcion,precio=precio,categoria=categoria,url_imagen=url_imagen)
            self.catalogo.update({codigo: producto})
        return True

    def contratar_empleados(self) -> bool:
        while True:
            dni: str = input("Ingrese DNI del farmaceutico (o -1 para dejar de contratar): ")
            if (int(dni) == -1):
                break
            nombre: str = input("Ingrese nombre del farmaceutico: ")
            empleado: Farmaceutico = Farmaceutico(dni=dni,nombre=nombre)
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

