class Producto:
    def __init__(self, codigo: str, nombre: str, presentacion: str, descripcion: str, precio: float, categoria: str, url_imagen: str) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.presentacion: str = presentacion
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.categoria: str = categoria
        self.url_imagen: str = url_imagen

    def mostrar_producto(self) -> None:
        print("Codigo: " + self.codigo, end=', ')
        print("Nombre: " + self.nombre, end=', ')
        print("Presentacion: " + self.presentacion, end=', ')
        print("Descripcion: " + self.descripcion, end=', ')
        print("Precio: " + self.precio, end=', ')
        print("Categoria: " + self.categoria)
