from datetime import datetime
import pytest
from Tienda import *

class TestClass:

    def test_crear_farmaceutico_correctamente(self):
        """
        Precondicion: Ninguna.
        Test Steps: Proceder a crear un Farmaceutico.
        Test Data: Ingresar los datos de un Farmaceutico como DNI y Nombre. Todo como string y dni debe ser longitud 8.
        Expected Result: Un farmaceutico existe, caso contrario no existe.
        """ 
        farmaceutico : Farmaceutico = Farmaceutico("71737699", "Renato Aurelio")
        assert farmaceutico is not None, "No se creo el farmaceutico correctamente"

    def test_crear_farmaceutico_incorrectamente(self):
        """
        Precondicion: Ninguna.
        Test Steps: Proceder a crear un Farmaceutico.
        Test Data: Ingresar los datos de un Farmaceutico como DNI y Nombre. Todo como string y dni debe ser longitud distinta de 8.
        Expected Result: Un farmaceutico no deberia existir.
        """ 
        with pytest.raises(ValueError) as excinfo:
            farmaceutico : Farmaceutico = Farmaceutico("202110069", "Jose Chachi")

        assert str(excinfo.value) == "El dni es incorrecto"

    def test_crear_producto_correctamente(self):
        """
        Precondicion: Ninguna.
        Test Steps: Proceder a crear un Producto.
        Test Data: Ingresar los datos de un Producto como codigo: "123", nombre: "manzana", presentacion: "rojisima", descripcion: "roja cuadrada", precio unitario: 128.10, categoria: "fruta" y url_imagen: "manzana.gfif". Todo en string, excepto el precio unitario como float.
        Expected Result: Un Producto existe, otro caso no existe.
        """
        producto: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        assert producto is not None, "No se creo el producto correctamente"
        
    def test_crear_producto_correctamente(self):
        """
        Precondicion: Ninguna.
        Test Steps: Proceder a crear un Producto.
        Test Data: Ingresar los datos parcialmente de un Producto como codigo: "123" y precio unitario: 123.01. Todo en string, excepto el precio unitario como float.
        Expected Result: Un Producto existe, otro caso no existe.
        """
        with pytest.raises(ValueError) as excinfo:
            producto: Producto = Producto(codigo = "123", nombre = None, presentacion=None, descripcion=None, precio=123.01, categoria=None, url_imagen=None)
            
        assert str(excinfo.value) == "No hay suficiente data del Producto ingresado"

    def test_reducir_stock_correctamente(self):
        """
        Precondicion: Crear un Producto y crear un ProductoFisico con un stock fijo a evaluar. Tener un valor menor o igual al stock fijado.
        Test Steps: Proceder a crear un Producto, luego un ProductoFisico. Despues, reducir el stock del ProductoFisico por una cantidad permitida (menor o igual al stock).
        Test Data: Ingresar los datos de un Producto como codigo: "123", nombre: "manzana", presentacion: "rojisima", descripcion: "roja cuadrada", precio unitario: 128.10, categoria: "fruta" y url_imagen: "manzana.gfif". Todo en string, excepto el precio unitario como float.
                   Ingresar los datos de un ProductoFisico como el codigo_fisico: "123", producto: Producto, stock = 100, fecha_expiracion = datetime. Notese que el codigo_fisico debe ser el Producto.codigo y el producto insertado debe existir.
                   Reducir el stock del ProductoFisico por una cantidad valida que debe ser menor o igual al stock, en este caso 50.
        Expected Result: Se espera que el ProductoFisico tenga al final un stock de 50 debido a la reduccion.
        """
        producto: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        product_fisico: ProductoFisico = ProductoFisico("123", producto, 100, datetime.now())
        
        product_fisico.disminuir_stock(50)
        
        assert product_fisico.stock == 50
    
    def test_reducir_stock_incorrectamente(self):
        """
        Precondicion: Crear un Producto y crear un ProductoFisico con un stock fijo a evaluar. Tener un valor mayor al stock fijado.
        Test Steps: Proceder a crear un Producto, luego un ProductoFisico. Despues, reducir el stock del ProductoFisico por una cantidad no permitida (mayor al stock).
        Test Data: Ingresar los datos de un Producto como codigo: "123", nombre: "manzana", presentacion: "rojisima", descripcion: "roja cuadrada", precio unitario: 128.10, categoria: "fruta" y url_imagen: "manzana.gfif". Todo en string, excepto el precio unitario como float.
                   Ingresar los datos de un ProductoFisico como el codigo_fisico: "123", producto: Producto, stock = 100, fecha_expiracion = datetime. Notese que el codigo_fisico debe ser el Producto.codigo y el producto insertado debe existir.
                   Reducir el stock del ProductoFisico por una cantidad valida que debe ser menor o igual al stock, en este caso 200.
        Expected Result: Si bien es cierto no resulta en error. Se espera que el ProductoFisico tenga al final un stock de 100 debido a que no se dio la reduccion de 200.
        """
        producto: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        product_fisico: ProductoFisico = ProductoFisico("123", producto, 100, datetime.now())
        
        product_fisico.disminuir_stock(200)
        
        assert product_fisico.stock == 100
    
    def test_agregar_producto_en_tienda_correctamente(self):
        """
        Precondicion: Debe existir un Farmaceutico, Producto, ProductoFisico y una Venta.
        Test Steps: Agregar un producto a la venta y luego buscar el producto en arrglo de productos
        Test Data:  Para el Farmaceutico: dni: "71737699" y nombre: "Renato Aurelio".
                    Para el Producto: codigo: "123", nombre: "manzana", presentacion: "rojisima", descripcion: "roja cuadrada", precio unitario: 128.10, categoria: "fruta" y url_imagen: "manzana.gfif".
                    Para los ProductoFisico: codigo: "123", producto: Producto, stock: 100, fecha de expiración: fecha actual.
                    Para la Venta: fecha de venta: fecha actual, empleado: Farmaceutico.
                    Al momento de agregar el producto se usa la cantidad de 1.
        Expected Result: Que el producto se encuentre en el arreglo de productos en la venta.
        """
        farmaceutico : Farmaceutico = Farmaceutico("71737699", "Renato Aurelio")
        producto: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        product_fisico: ProductoFisico = ProductoFisico("123", producto, 100, datetime.now())
        venta: Venta = Venta(cantidades=None, productos=None, fecha=datetime.now(),empleado=farmaceutico)
        
        venta.agregar(product_fisico,1)
        assert venta.verificar_producto(product_fisico.codigo_fisico) == True


    def test_agregar_producto_en_tienda_incorrectamente(self):
        """
        Precondicion: Debe existir un Farmaceutico, Producto, ProductoFisico y una Venta.
        Test Steps: Agregar un producto físico a la venta y luego buscar el producto en el arreglo de productos.
        Test Data:  Para el Farmaceutico: dni: "71737699" y nombre: "Renato Aurelio".
                    Para el Producto: codigo: "123", nombre: "manzana", presentacion: "rojisima", descripcion: "roja cuadrada", precio unitario: 128.10, categoria: "fruta" y url_imagen: "manzana.gfif".
                    Para los ProductoFisico: codigo: "123", producto: Producto, stock: 100, fecha de expiración: fecha actual.
                    Para la Venta: fecha de venta: fecha actual, empleado: Farmaceutico.
                    Al momento de agregar el producto se usa la cantidad de -67.
        Expected Result: Que el producto no se encuentre en el arreglo de productos en la venta.
        """
        farmaceutico : Farmaceutico = Farmaceutico("71737699", "Renato Aurelio")
        producto: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        product_fisico: ProductoFisico = ProductoFisico("123", producto, 100, datetime.now())
        venta: Venta = Venta(cantidades=None, productos=None, fecha=datetime.now(),empleado=farmaceutico)
        
        venta.agregar(product_fisico, -67)
        assert venta.verificar_producto(product_fisico.codigo_fisico) == False
    

    def test_remover_productos_en_tienda_correctamente(self):
        """
        Precondicion: Debe existir un Farmaceutico, Producto, ProductoFisico y una Venta.
        Test Steps: Agregar un producto físico a la venta, luego eliminarlo y finalmente buscar el producto en el arreglo de cantidades de la venta. 
        Test Data:  Para el Farmaceutico: dni: "71737699" y nombre: "Renato Aurelio".
                    Para el Producto: codigo: "123", nombre: "manzana", presentacion: "rojisima", descripcion: "roja cuadrada", precio unitario: 128.10, categoria: "fruta" y url_imagen: "manzana.gfif".
                    Para los ProductoFisico: codigo: "123", producto: Producto, stock: 100, fecha de expiración: fecha actual.
                    Para la Venta: fecha de venta: fecha actual, empleado: Farmaceutico.
                    Al momento de agregar y remover el producto se usa la cantidad de 10.
        Expected Result: Se tuvo que haber reducido la cantidad a 0 del arreglo de cantidades en venta. 
        """
        farmaceutico : Farmaceutico = Farmaceutico("71737699", "Renato Aurelio")
        producto: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        product_fisico: ProductoFisico = ProductoFisico("123", producto, 100, datetime.now())
        venta: Venta = Venta(cantidades=None, productos=None, fecha=datetime.now(),empleado=farmaceutico)
        venta.agregar(product_fisico, 10)
        venta.remover(product_fisico, 10)
        
        assert venta.cantidades[venta.productos.index(product_fisico)] == 0


    def test_remover_productos_en_tienda_incorrectamente(self):
        """
        Precondicion: Debe existir un Farmaceutico, Producto, dos ProductoFisico y una Venta.
        Test Steps: Agregar un producto físico a la venta, luego eliminar otro producto físico de la venta.
        Test Data:  Para el Farmaceutico: dni: "71737699" y nombre: "Renato Aurelio".
                    Para el Producto: codigo: "123", nombre: "manzana", presentacion: "rojisima", descripcion: "roja cuadrada", precio unitario: 128.10, categoria: "fruta" y url_imagen: "manzana.gfif".
                    Para el ProductoFisico 1: codigo: "123", producto: Producto, stock: 100, fecha de expiración: fecha actual.
                    Para el ProductoFisico 2: codigo: "1234", producto: Producto, stock: 500, fecha de expiración: fecha actual.
                    Para la Venta: fecha de venta: fecha actual, empleado: Farmaceutico.
                    Al momento de agregar el primer producto y eliminar el segundo producto se usa la cantidad de 10.
        Expected Result: No se debería remover el producto físico, retorna falso.
        """
        farmaceutico : Farmaceutico = Farmaceutico("71737699", "Renato Aurelio")
        producto: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        product_fisico: ProductoFisico = ProductoFisico("123", producto, 100, datetime.now())
        product_fisico_dos: ProductoFisico = ProductoFisico("1234", producto, 500, datetime.now())
        venta: Venta = Venta(cantidades=None, productos=None, fecha=datetime.now(),empleado=farmaceutico)
        venta.agregar(product_fisico, 10)
        
        assert venta.remover(product_fisico_dos, 10) == False

    def test_producto_no_existe(self):
        """
        Precondicion: Debe existir un Farmaceutico, Producto, dos ProductoFisico y una Venta.
        Test Steps: Agregar un producto físico cualquiera y luego verificar si un producto con un código muy similar existe
        Test Data:  Para el Farmaceutico: dni: "71737699" y nombre: "Renato Aurelio".
                    Para el Producto: codigo: "123", nombre: "manzana", presentacion: "rojisima", descripcion: "roja cuadrada", precio unitario: 128.10, categoria: "fruta" y url_imagen: "manzana.gfif".
                    Para el ProductoFisico 1: codigo: "123", producto: Producto, stock: 100, fecha de expiración: fecha actual.
                    Para la Venta: fecha de venta: fecha actual, empleado: Farmaceutico.
                    Al momento de agregar el primer producto se usa la cantidad de 10 y al momento de verificar el producto se usa el código 1234.
        Expected Result: No se debería remover el producto físico, retorna falso.
        """
        farmaceutico : Farmaceutico = Farmaceutico("71737699", "Renato Aurelio")
        producto: Producto = Producto("123","manzana","rojisima","roja cuadrada",128.10,"fruta","manzana.gfif")
        product_fisico: ProductoFisico = ProductoFisico("123", producto, 100, datetime.now())
        venta: Venta = Venta(cantidades=None, productos=None, fecha=datetime.now(),empleado=farmaceutico)
        venta.agregar(product_fisico, 100)

        assert venta.verificar_producto("1234") == False