
# matrices_parte2.py

# Ejercicio 6: Índice de la columna que contiene el valor máximo de toda la matriz
def columna_del_maximo(matriz):
    max_valor = float('-inf')
    columna_resultado = -1
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] > max_valor:
                max_valor = matriz[i][j]
                columna_resultado = j
    return columna_resultado

# Ejercicio 7: Posición (i, j) del valor máximo de la matriz
def posicion_maximo(matriz):
    max_valor = float('-inf')
    pos = (-1, -1)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > max_valor:
                max_valor = matriz[i][j]
                pos = (i, j)
    return pos

# Ejercicio 8: Posición de un valor dado en la matriz, o -1 si no está
def buscar_elemento(matriz, elemento):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == elemento:
                return (i, j)
    return -1

# Ejercicio 9: Suma de los elementos de una fila dada
def suma_fila(matriz, fila):
    return sum(matriz[fila])

# Ejercicio 10: Suma de los elementos de una columna dada
def suma_columna(matriz, columna):
    return sum(fila[columna] for fila in matriz)
