class Producto:
    def __init__(self, codigo: str | None, nombre: str | None, presentacion: str | None, descripcion: str | None, precio: float | None, categoria: str | None, url_imagen: str | None) -> None:
        if codigo is None or nombre is None or presentacion is None or descripcion is None or precio is None or categoria is None or url_imagen is None:
            raise ValueError("No hay suficiente data del Producto ingresado")
        self.codigo: str | None = codigo
        self.nombre: str | None = nombre
        self.presentacion: str | None = presentacion
        self.descripcion: str | None = descripcion
        self.precio: float | None = precio
        self.categoria: str | None = categoria
        self.url_imagen: str | None = url_imagen


    def mostrar_producto(self) -> None:
        print("Codigo: " + self.codigo, end=', ')
        print("Nombre: " + self.nombre, end=', ')
        print("Presentacion: " + self.presentacion, end=', ')
        print("Descripcion: " + self.descripcion, end=', ')
        print("Precio: " + self.precio, end=', ')
        print("Categoria: " + self.categoria)
