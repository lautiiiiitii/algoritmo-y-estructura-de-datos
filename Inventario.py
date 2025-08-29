inventario = []

while True:
    
    print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
    print("1. Registrar nuevo producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto por nombre")
    print("4. Cambiar precio del producto")
    print("5. Reponer stock")
    print("6. Registrar nueva compra")
    print("7. Eliminar producto del inventario")
    print("8. Salir")
    encontrado = False


    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            nombrePro = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: "))
                stock =  int(input("Stock: "))
            except ValueError:
                print("Precio o stock inválidas. Intenta de nuevo.")
                continue

            if precio <= 0 or stock <= 0:
                print("Datos inválidos. Intenta de nuevo.")
            else:
                nuevo_producto = {
                    "producto": nombrePro,
                    "precio": precio,
                    "stock": stock
                }
                inventario.append(nuevo_producto)
                print(f"Producto {nombrePro} registrado con éxito.")

        case "2":
            if not inventario:
                print("No hay productos registrados aún.")
            else:
                print("\nProductos registrados:")
                print("-------------------------")
                for i, producto in enumerate(inventario, 1):
                    print(f"{i}. Producto: {producto['producto']}")
                    print(f"   Precio: ${producto['precio']}")
                    print(f"   Stock: {producto['stock']}")
                    print("-------------------------")

        case "3":
            if not inventario:
                print("No hay productos registrados.")
            else:
                buscar_pro = input("Escribe el nombre del producto que quieras buscar: ")
                
                for producto in inventario:
                    if producto['producto'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Producto: {producto['producto']}")
                        print(f"   Precio: ${producto['precio']}")
                        print(f"   Stock: {producto['stock']}")
                        print("-------------------------")
                        encontrado = True
                
                if encontrado == False:
                    print("No se encontro ese producto")
                    
        case "4":
            if not inventario:
                print("No hay productos registrados.")
            else:
                
                buscar_pro = input("Escribe el nombre del producto al que quieras cambiar el precio: ")
                
                for producto in inventario:
                    if producto['producto'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Producto: {producto['producto']}")
                        print(f"   Precio: ${producto['precio']}")
                        print(f"   Stock: {producto['stock']}")
                        print("-------------------------")
                        nuevo_precio = int(input("Cual es el nuevo precio? "))
                        producto['precio'] = nuevo_precio
                        print("Nuevo precio: ")
                        print(f"   Precio: {producto['precio']}")
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro ese producto")

        case "5":
            if not inventario:
                print("No hay productos registrados.")
            else:
                
                buscar_pro = input("Escribe el nombre del producto al que quieras agregar stcok: ")
                
                for producto in inventario:
                    if producto['producto'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Producto: {producto['producto']}")
                        print(f"   Precio: ${producto['precio']}")
                        print(f"   Stock: {producto['stock']}")
                        print("-------------------------")
                        nuevo_stock = int(input("Cuanto stock deséas agregar "))
                        producto['stock'] = producto['stock'] + nuevo_stock
                        print("Nuevo stock: ")
                        print(f"   Stock: {producto['stock']}")
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro ese producto")
                        
        case "6":
            if not inventario:
                print("No hay productos registrados.")
            else:
                buscar_pro = input("Escribe el nombre del producto al que quieras registrar compra: ")
                
                for producto in inventario:
                    if producto['producto'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Producto: {producto['producto']}")
                        print(f"   Precio: ${producto['precio']}")
                        print(f"   Stock: {producto['stock']}")
                        print("-------------------------")
                        nueva_compra = int(input("Cuanto stock quieres registrar como comprado "))
                        if nueva_compra > producto['stock']:
                            print("no tienes suficiente stock para realizar esa venta")
                            
                        else:
                            producto['stock'] = producto['stock'] - nueva_compra
                            if producto['stock'] == 0:
                                print(f"Te has quedado sin stock de {producto['producto']}")
                                inventario.remove(producto)
                                
                            else:
                                print("Nuevo stock: ")
                                print(f"   Stock: {producto['stock']}")
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro ese producto")
                    
        case "7":
            if not inventario:
                print("No hay productos registrados.")
            else:
                buscar_pro = input("Escribe el nombre del producto al que quieras registrar compra: ")
                
                for producto in inventario:
                    if producto['producto'] == buscar_pro:
                        inventario.remove(producto)
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro ese producto")
    
        case "8":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intenta otra vez.")