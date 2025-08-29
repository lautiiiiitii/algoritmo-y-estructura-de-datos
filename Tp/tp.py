#TP Emilio Fernandez, Benjamin Fernandez, Lautaro De Santis y Federico Tambuerelli
inventario = []

while True:
    
    print("\n--- HABLOMOS DE VIDEOJUEGOS TIENDA ---")
    print("1. Registrar nuevo juego")
    print("2. Mostrar todos los juegos")
    print("3. Buscar juego por nombre")
    print("4. Cambiar precio del juego")
    print("5. Reponer stock")
    print("6. Registrar nuevas reseñas")
    print("7. Registrar nueva compra")
    print("8. Eliminar juego del inventario")
    print("9. Salir")
    encontrado = False


    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            nombrePro = input("Nombre del juego: ")
            try:
                precio = float(input("Precio: "))
                stock =  int(input("Stock: "))
                valoracion = int(input("Valoracion (del 1 al 5): "))
            except ValueError:
                print("Precio o stock inválidas. Intenta de nuevo.")
                continue

            if precio <= 0 or stock <= 0 or valoracion > 5 or valoracion < 1:
                print("Datos inválidos. Intenta de nuevo.")
            else:
                nuevo_juego = {
                    "juego": nombrePro,
                    "precio": precio,
                    "stock": stock,
                    "valoracion": valoracion
                }
                inventario.append(nuevo_juego)
                print(f"juego {nombrePro} registrado con éxito.")

        case "2":
            if not inventario:
                print("No hay juegos registrados aún.")
            else:
                print("\njuegos registrados:")
                print("-------------------------")
                for i, juego in enumerate(inventario, 1):
                    print(f"{i}. Juego: {juego['juego']}")
                    print(f"   Precio: ${juego['precio']}")
                    print(f"   Stock: {juego['stock']}")
                    print(f"   Valoracion: {juego['valoracion']}★/5")
                    print("-------------------------")

        case "3":
            if not inventario:
                print("No hay juegos registrados.")
            else:
                buscar_pro = input("Escribe el nombre del juego que quieras buscar: ")
                
                for juego in inventario:
                    if juego['juego'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Juego: {juego['juego']}")
                        print(f"   Precio: ${juego['precio']}")
                        print(f"   Stock: {juego['stock']}")
                        print(f"   Valoracion: {juego['valoracion']}★/5")
                        print("-------------------------")
                        encontrado = True
                
                if encontrado == False:
                    print("No se encontro ese juego")
                    
        case "4":
            if not inventario:
                print("No hay juegos registrados.")
            else:
                
                buscar_pro = input("Escribe el nombre del juego al que quieras cambiar el precio: ")
                
                for juego in inventario:
                    if juego['juego'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Juego: {juego['juego']}")
                        print(f"   Precio: ${juego['precio']}")
                        print(f"   Stock: {juego['stock']}")
                        print(f"   Valoracion: {juego['valoracion']}★/5")
                        print("-------------------------")
                        nuevo_precio = int(input("Cual es el nuevo precio? "))
                        if nuevo_precio <= 0:
                            print("Datos inválidos. Intenta de nuevo.")
                        else:
                            juego['precio'] = nuevo_precio
                            print("Nuevo precio: ")
                            print(f"   Precio: {juego['precio']}")
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro ese juego")

        case "5":
            if not inventario:
                print("No hay juegos registrados.")
            else:
                
                buscar_pro = input("Escribe el nombre del juego al que quieras agregar stcok: ")
                
                for juego in inventario:
                    if juego['juego'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Juego: {juego['juego']}")
                        print(f"   Precio: ${juego['precio']}")
                        print(f"   Stock: {juego['stock']}")
                        print(f"   Valoracion: {juego['valoracion']}★/5")
                        print("-------------------------")
                        nuevo_stock = int(input("Cuanto stock deséas agregar "))
                        if nuevo_stock <= 0:
                            print("Datos inválidos. Intenta de nuevo.")
                        else:
                            juego['stock'] = juego['stock'] + nuevo_stock
                            print("Nuevo stock: ")
                            print(f"   Stock: {juego['stock']}")
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro ese juego")
            
        case "6":
            for juego in inventario:
                    if juego['juego'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Juego: {juego['juego']}")
                        print(f"   Precio: ${juego['precio']}")
                        print(f"   Stock: {juego['stock']}")
                        print(f"   Valoracion: {juego['valoracion']}★/5")
                        print("-------------------------")
                        nueva_valoracion = int(input("Cual es la nueva valoracion? "))
                        if nueva_valoracion <= 0 or nueva_valoracion > 5:
                            print("Datos inválidos. Intenta de nuevo.")
                        else:
                            juego['valoracion'] = nueva_valoracion
                            print("Nueva valoracion: ")
                            print(f"   Valoracion: {juego['valoracion']}★/5")
                        encontrado = True
                        
            if encontrado == False:
                print("No se encontro ese juego")
                        
        case "7":
            if not inventario:
                print("No hay juegos registrados.")
            else:
                buscar_pro = input("Escribe el nombre del juego al que quieras registrar compra: ")
                
                for juego in inventario:
                    if juego['juego'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Juego: {juego['juego']}")
                        print(f"   Precio: ${juego['precio']}")
                        print(f"   Stock: {juego['stock']}")
                        print(f"   Valoracion: {juego['valoracion']}★/5")
                        print("-------------------------")
                        nueva_compra = int(input("Cuanto stock quieres registrar como comprado "))
                        if nueva_compra <= 0:
                            print("Datos inválidos. Intenta de nuevo.")
                        else:
                            if nueva_compra > juego['stock']:
                                print("no tienes suficiente stock para realizar esa venta")
                            
                            else:
                                juego['stock'] = juego['stock'] - nueva_compra
                                if juego['stock'] == 0:
                                    print(f"Te has quedado sin stock de {juego['juego']}")
                                    inventario.remove(juego)
                                
                                else:
                                    print("Nuevo stock: ")
                                    print(f"   Stock: {juego['stock']}")
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro ese juego")
                    
        case "8":
            if not inventario:
                print("No hay juegos registrados.")
            else:
                buscar_pro = input("Escribe el nombre del juego al que quieras borrar del inventario: ")
                
                for juego in inventario:
                    if juego['juego'] == buscar_pro:
                        inventario.remove(juego)
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro ese juego")
    
        case "9":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intenta otra vez.")