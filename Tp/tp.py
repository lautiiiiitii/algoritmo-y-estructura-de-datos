#TP Lautaro De Santis 
inventario = []

while True:
    
    print("\n--- ROBERTO, LA VENTA DE PELICULAS. ---")
    print("1. Registrar nueva pelicula")
    print("2. Mostrar todas las peliculas")
    print("3. Buscar pelicula por nombre")
    print("4. Cambiar precio de la pelicula")
    print("5. Reponer stock")
    print("6. Registrar nuevas reseñas")
    print("7. Registrar nueva compra")
    print("8. Eliminar juego del inventario")
    print("9. Salir")
    encontrado = False


    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            nombrePro = input("Nombre de la pelicula: ")
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
                nuevo_pelicula = {
                    "pelicula": nombrePro,
                    "precio": precio,
                    "stock": stock,
                    "valoracion": valoracion
                }
                inventario.append(nuevo_pelicula)
                print(f"pelicula {nombrePro} registrado con éxito.")

        case "2":
            if not inventario:
                print("No hay peliculas registrados aún.")
            else:
                print("\npeliculas registrdadas:")
                print("-------------------------")
                for i, pelicula in enumerate(inventario, 1):
                    print(f"{i}. Juego: {pelicula['pelicula']}")
                    print(f"   Precio: ${pelicula['precio']}")
                    print(f"   Stock: {pelicula['stock']}")
                    print(f"   Valoracion: {pelicula['valoracion']}★/5")
                    print("-------------------------")

        case "3":
            if not inventario:
                print("No hay peliculas registradas.")
            else:
                buscar_pro = input("Escribe el nombre de la pelicula que quieras buscar: ")
                
                for pelicula in inventario:
                    if pelicula['pelicula'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Pelicula: {pelicula['pelicula']}")
                        print(f"   Precio: ${pelicula['precio']}")
                        print(f"   Stock: {pelicula['stock']}")
                        print(f"   Valoracion: {pelicula['valoracion']}★/5")
                        print("-------------------------")
                        encontrado = True
                
                if encontrado == False:
                    print("No se encontro esa pelicula")
                    
        case "4":
            if not inventario:
                print("No hay peliculas registradas.")
            else:
                
                buscar_pro = input("Escribe el nombre de la pelicula a la que quieras cambiar el precio: ")
                
                for pelicula in inventario:
                    if pelicula['pelicula'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Pelicula: {pelicula['pelicula']}")
                        print(f"   Precio: ${pelicula['precio']}")
                        print(f"   Stock: {pelicula['stock']}")
                        print(f"   Valoracion: {pelicula['valoracion']}★/5")
                        print("-------------------------")
                        nuevo_precio = int(input("Cual es el nuevo precio? "))
                        if nuevo_precio <= 0:
                            print("Datos inválidos. Intenta de nuevo.")
                        else:
                            pelicula['precio'] = nuevo_precio
                            print("Nuevo precio: ")
                            print(f"   Precio: {pelicula['precio']}")
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro esa pelicula")

        case "5":
            if not inventario:
                print("No hay peliculas registradas.")
            else:
                
                buscar_pro = input("Escribe el nombre de la pelicula al que quieras agregar stcok: ")
                
                for pelicula in inventario:
                    if pelicula['pelicula'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Pelicula: {pelicula['pelicula']}")
                        print(f"   Precio: ${pelicula['precio']}")
                        print(f"   Stock: {pelicula['stock']}")
                        print(f"   Valoracion: {pelicula['valoracion']}★/5")
                        print("-------------------------")
                        nuevo_stock = int(input("Cuanto stock deséas agregar "))
                        if nuevo_stock <= 0:
                            print("Datos inválidos. Intenta de nuevo.")
                        else:
                            pelicula['stock'] = pelicula['stock'] + nuevo_stock
                            print("Nuevo stock: ")
                            print(f"   Stock: {pelicula['stock']}")
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro esa pelicula")
            
        case "6":
            for pelicula in inventario:
                    if pelicula['pelicula'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Pelicula: {pelicula['pelicula']}")
                        print(f"   Precio: ${pelicula['precio']}")
                        print(f"   Stock: {pelicula['stock']}")
                        print(f"   Valoracion: {pelicula['valoracion']}★/5")
                        print("-------------------------")
                        nueva_valoracion = int(input("Cual es la nueva valoracion? "))
                        if nueva_valoracion <= 0 or nueva_valoracion > 5:
                            print("Datos inválidos. Intenta de nuevo.")
                        else:
                            pelicula['valoracion'] = nueva_valoracion
                            print("Nueva valoracion: ")
                            print(f"   Valoracion: {pelicula['valoracion']}★/5")
                        encontrado = True
                        
            if encontrado == False:
                print("No se encontro esa pelicula")
                        
        case "7":
            if not inventario:
                print("No hay peliculas registradas.")
            else:
                buscar_pro = input("Escribe el nombre de la pelicula a la que quieras registrar compra: ")
                
                for pelicula in inventario:
                    if pelicula['pelicula'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Pelicula: {pelicula['pelicula']}")
                        print(f"   Precio: ${pelicula['precio']}")
                        print(f"   Stock: {pelicula['stock']}")
                        print(f"   Valoracion: {pelicula['valoracion']}★/5")
                        print("-------------------------")
                        nueva_compra = int(input("Cuanto stock quieres registrar como comprado "))
                        if nueva_compra <= 0:
                            print("Datos inválidos. Intenta de nuevo.")
                        else:
                            if nueva_compra > pelicula['stock']:
                                print("no tienes suficiente stock para realizar esa venta")
                            
                            else:
                                pelicula['stock'] = pelicula['stock'] - nueva_compra
                                if pelicula['stock'] == 0:
                                    print(f"Te has quedado sin stock de {pelicula['pelicula']}")
                                    inventario.remove(pelicula)
                                
                                else:
                                    print("Nuevo stock: ")
                                    print(f"   Stock: {pelicula['stock']}")
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro esa pelicula")
                    
        case "8":
            if not inventario:
                print("No hay peliculas registradas.")
            else:
                buscar_pro = input("Escribe el nombre de la pelicula a la que quieras borrar del inventario: ")
                
                for pelicula in inventario:
                    if pelicula['pelicula'] == buscar_pro:
                        inventario.remove(pelicula)
                        encontrado = True
                        
                if encontrado == False:
                    print("No se encontro ese pelicula")
    
        case "9":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intenta otra vez.")1
