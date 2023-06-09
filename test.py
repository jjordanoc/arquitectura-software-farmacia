from datetime import datetime
import pytest
from Tienda import *

class TestClass:

    def test_createFarmaceuticoSucceded(self):
        """
        Precondicion: Need to create a Farmaceutico
        Test Steps: Proceed to create a Farmaceutico
        Test Data: Enter Farmaceutico data as DNI and a Name
        Expected Result: A Farmaceutico exists, otherwise is None
        """ 
        farmaceutico : Farmaceutico = Farmaceutico("71737699", "Renato Aurelio")
        assert farmaceutico is not None, "No se creo el farmaceutico correctamente"

    def test_createProductSucceded(self):
        """
        Precondicion:
        Test Steps:
        Test Data:
        Expected Result:
        """
        product: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        assert product is not None, "No se creo el producto correctamente"

    def test_reduceStockSucceded(self):
        """
        Precondicion:
        Test Steps:
        Test Data:
        Expected Result:
        """
        product: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        realProduct: ProductoFisico = ProductoFisico("123", product, 100, datetime.now())
        
        realProduct.disminuir_stock(50)
        
        assert realProduct.stock == 50
    
    def test_reduceStockFailed(self):
        """
        Precondicion:
        Test Steps:
        Test Data:
        Expected Result:
        """
        product: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        realProduct: ProductoFisico = ProductoFisico("123", product, 100, datetime.now())
        
        realProduct.disminuir_stock(200)
        
        assert realProduct.stock == 100
    
    def test_agregar_producto_en_tienda(self):
        """
        Precondicion:
        Test Steps:
        Test Data:
        Expected Result:
        """
        farmaceutico : Farmaceutico = Farmaceutico("71737699", "Renato Aurelio")
        product: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        realProduct: ProductoFisico = ProductoFisico("123", product, 100, datetime.now())
        venta: Venta = Venta(cantidades=None, productos=None, fecha=datetime.now(),empleado=farmaceutico)
        
        venta.agregar(realProduct,1)
        assert realProduct in venta.productos

    def test_producto_no_existe(self): # Still work in progress!
        """
        Precondicion:
        Test Steps:
        Test Data:
        Expected Result:
        """
        farmaceutico : Farmaceutico = Farmaceutico("71737699", "Renato Aurelio")
        venta: Venta = Venta(cantidades=None, productos=None, fecha=datetime.now(),empleado=farmaceutico)
        assert venta.verificar_producto("un codigo cualquiera")
