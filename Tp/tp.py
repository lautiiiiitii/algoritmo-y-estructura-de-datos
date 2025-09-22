# TP Lautaro De Santis
usuarios = {}  # diccionario: {"usuario": {"password": "xxx", "coleccion": []}}
usuario_actual = None

def menu_principal():
    print("\n--- COLECCIÓN DE PELÍCULAS ---")
    print("1. Registrar nueva película")
    print("2. Mostrar todas las películas")
    print("3. Buscar película por nombre")
    print("4. Cambiar la valoración de una película")
    print("5. Agregar o cambiar reseña")
    print("6. Eliminar película de la colección")
    print("7. Cerrar sesión")
    print("8. Salir")
    return input("Elige una opción: ")

def mostrar_coleccion(coleccion):
    if not coleccion:
        print("No hay películas en tu colección aún.")
    else:
        print("\nPelículas en tu colección:")
        print("-------------------------")
        for i, pelicula in enumerate(coleccion, 1):
            print(f"{i}. {pelicula['pelicula']} ({pelicula['valoracion']}★/5)")
            if pelicula['reseña']:
                print(f"   Reseña: {pelicula['reseña']}")
            print("-------------------------")


while True:
    if not usuario_actual:
        print("\n--- BIENVENIDO ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Elige un nombre de usuario: ")
            if nombre in usuarios:
                print("Ese usuario ya existe.")
            else:
                password = input("Elige una contraseña: ")
                usuarios[nombre] = {"password": password, "coleccion": []}
                print("Usuario registrado con éxito.")

        elif opcion == "2":
            nombre = input("Usuario: ")
            password = input("Contraseña: ")
            if nombre in usuarios and usuarios[nombre]["password"] == password:
                usuario_actual = nombre
                print(f"¡Bienvenido {usuario_actual}!")
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

    else:
        coleccion = usuarios[usuario_actual]["coleccion"]
        opcion = menu_principal()

        if opcion == "1":
            nombreP = input("Nombre de la película: ")
            try:
                valoracion = int(input("Valoración (1 a 5): "))
            except ValueError:
                print("Valoración inválida.")
                continue
            if 1 <= valoracion <= 5:
                nueva_pelicula = {"pelicula": nombreP, "valoracion": valoracion, "reseña": ""}
                coleccion.append(nueva_pelicula)
                print(f"Película '{nombreP}' registrada en tu colección.")
            else:
                print("La valoración debe estar entre 1 y 5.")

        elif opcion == "2":
            mostrar_coleccion(coleccion)

        elif opcion == "3":
            buscar = input("Escribe el nombre de la película: ")
            encontrado = False
            for pelicula in coleccion:
                if pelicula['pelicula'].lower() == buscar.lower():
                    print(f"\nPelícula: {pelicula['pelicula']} ({pelicula['valoracion']}★/5)")
                    if pelicula['reseña']:
                        print(f"Reseña: {pelicula['reseña']}")
                    encontrado = True
            if not encontrado:
                print("No se encontró esa película.")

        elif opcion == "4":
            buscar = input("Película a cambiar valoración: ")
            for pelicula in coleccion:
                if pelicula['pelicula'].lower() == buscar.lower():
                    try:
                        nueva_val = int(input("Nueva valoración (1 a 5): "))
                    except ValueError:
                        print("Valoración inválida.")
                        break
                    if 1 <= nueva_val <= 5:
                        pelicula['valoracion'] = nueva_val
                        print("Valoración actualizada.")
                    else:
                        print("La valoración debe estar entre 1 y 5.")
                    break
            else:
                print("No se encontró esa película.")

        elif opcion == "5":
            buscar = input("Película a reseñar: ")
            for pelicula in coleccion:
                if pelicula['pelicula'].lower() == buscar.lower():
                    pelicula['reseña'] = input("Escribe tu reseña: ")
                    print("Reseña guardada.")
                    break
            else:
                print("No se encontró esa película.")

        elif opcion == "6":
            buscar = input("Película a eliminar: ")
            for pelicula in coleccion:
                if pelicula['pelicula'].lower() == buscar.lower():
                    coleccion.remove(pelicula)
                    print("Película eliminada.")
                    break
            else:
                print("No se encontró esa película.")

        elif opcion == "7":
            print(f"Sesión cerrada de {usuario_actual}.")
            usuario_actual = None

        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
