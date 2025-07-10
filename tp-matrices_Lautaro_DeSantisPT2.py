# Ejercicio 6: Escribir un método que dada una matriz de enteros devuelva la columna que contiene el máximo elemento de la matriz.
def columna_del_maximo(matriz):
    max_valor = float('-inf')
    columna_resultado = -1
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] > max_valor:
                max_valor = matriz[i][j]
                columna_resultado = j
    return columna_resultado

# Ejercicio 7: Escribir un método que dada una matriz de enteros devuelva la posición que contiene el máximo elemento de la matriz.
def posicion_maximo(matriz):
    max_valor = float('-inf')
    pos = (-1, -1)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > max_valor:
                max_valor = matriz[i][j]
                pos = (i, j)
    return pos

# Ejercicio 8: Escribir un método que dada una matriz de enteros y un entero, devuelva la posición de la matriz en la que se encuentra ese entero, o un valor que indique que el entero no se encuentra en la matriz.
def buscar_elemento(matriz, elemento):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == elemento:
                return (i, j)
    return -1

# Ejercicio 9: Escribir un método que dada una matriz de enteros y un entero que representa un índice de fila, devuelva la suma de los elementos de esa fila.
def suma_fila(matriz, fila):
    return sum(matriz[fila])

# Ejercicio 10: Escribir un método que dada una matriz de enteros y un entero que representa un índice de columna, devuelva la suma de los elementos de esa columna.
def suma_columna(matriz, columna):
    return sum(fila[columna] for fila in matriz)
