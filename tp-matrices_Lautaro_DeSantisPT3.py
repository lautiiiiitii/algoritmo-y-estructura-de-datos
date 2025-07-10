
# matrices_parte3.py

# Ejercicio 11: Intercambiar dos filas dadas de una matriz
def intercambiar_filas(matriz, fila1, fila2):
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz

# Ejercicio 12: Intercambiar dos columnas dadas de una matriz
def intercambiar_columnas(matriz, col1, col2):
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]
    return matriz

# Ejercicio 13: Rotar la matriz a la derecha (elemento por elemento)
def rotar_derecha(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    plano = [elem for fila in matriz for elem in fila]
    plano = [plano[-1]] + plano[:-1]  # rotar a derecha
    return [plano[i*columnas:(i+1)*columnas] for i in range(filas)]

# Ejercicio 14: Rotar la matriz a la izquierda (elemento por elemento)
def rotar_izquierda(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    plano = [elem for fila in matriz for elem in fila]
    plano = plano[1:] + [plano[0]]  # rotar a izquierda
    return [plano[i*columnas:(i+1)*columnas] for i in range(filas)]

# Ejercicio 15: Suma de dos matrices de números decimales
def suma_matrices(m1, m2):
    filas, columnas = len(m1), len(m1[0])
    return [[m1[i][j] + m2[i][j] for j in range(columnas)] for i in range(filas)]
