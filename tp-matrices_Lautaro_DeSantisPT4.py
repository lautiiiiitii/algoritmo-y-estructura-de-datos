
# matrices_parte4.py

# Ejercicio 16: Resta de dos matrices de números decimales
def resta_matrices(m1, m2):
    filas, columnas = len(m1), len(m1[0])
    return [[m1[i][j] - m2[i][j] for j in range(columnas)] for i in range(filas)]

# Ejercicio 17: Producto de dos matrices de números decimales
def producto_matrices(m1, m2):
    filas_m1, columnas_m1 = len(m1), len(m1[0])
    filas_m2, columnas_m2 = len(m2), len(m2[0])
    if columnas_m1 != filas_m2:
        raise ValueError("Las dimensiones no son compatibles para multiplicar.")
    resultado = [[0 for _ in range(columnas_m2)] for _ in range(filas_m1)]
    for i in range(filas_m1):
        for j in range(columnas_m2):
            for k in range(columnas_m1):
                resultado[i][j] += m1[i][k] * m2[k][j]
    return resultado

# Ejercicio 18: Transpuesta de una matriz de números decimales
def transponer_matriz(matriz):
    return [list(fila) for fila in zip(*matriz)]

# Ejercicio 19: Inversa de una matriz cuadrada de números decimales
def inversa_matriz(matriz):
    import numpy as np
    matriz_np = np.array(matriz)
    if matriz_np.shape[0] != matriz_np.shape[1]:
        raise ValueError("La matriz no es cuadrada.")
    try:
        inversa = np.linalg.inv(matriz_np)
        return inversa.tolist()
    except np.linalg.LinAlgError:
        raise ValueError("La matriz no es invertible.")
