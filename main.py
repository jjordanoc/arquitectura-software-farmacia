from Tienda import Tienda

def menu() -> None:
    babel_farma: Tienda = Tienda("Av. Reducto 187")
    print("Bienvenido a BabelFarma!")
    print("Ingresa la contraseña de administrador:")

    contrasenia: str = input("Contraseña: ")

    
    if (contrasenia == "1234"):
        opcion: int = -1
        while True:
            
            print("Ingrese una opcion:")
            print("\t1. Contratar empleado")
            print("\t2. Actualizar catalogo")
            print("\t3. Abastecer productos")
            print("\t4. Mostrar empleados")
            print("\t5. Salir")
            opcion: int = int(input("Opcion: "))
            
            if opcion == 5:
                break
            
            if opcion == 1:
                babel_farma.contratar_empleados()
            elif opcion == 2:
                babel_farma.actualizar_catalogo()
            elif opcion == 3:
                babel_farma.abastecer_productos()
            elif opcion == 4:
                babel_farma.mostrar_empleados()

        

    else:
        while True:
            print("Ingrese una opcion:")
            print("\t1. Visualizar catalogo")
            print("\t2. Visualizar productos")
            print("\t3. Comprar productos")
            print("\t4. Salir")
            opcion: int = int(input("Opcion: "))
            if opcion == 4:
                break
            elif opcion == 1:
                babel_farma.mostrar_catalogo()
            elif opcion == 2:
                babel_farma.mostrar_productos()
            elif opcion == 3:
                babel_farma.realizar_venta()
         
        
menu()