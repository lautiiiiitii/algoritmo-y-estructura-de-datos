
# matrices_parte1.py

# Ejercicio 1: Suma total de los elementos de la matriz
def suma_matriz(matriz):
    return sum(sum(fila) for fila in matriz)

# Ejercicio 2: Cantidad de elementos positivos en la matriz
def contar_positivos(matriz):
    return sum(1 for fila in matriz for elem in fila if elem > 0)

# Ejercicio 3: Índice de la columna que contiene el máximo valor de una fila dada
def columna_maximo_en_fila(matriz, fila):
    return matriz[fila].index(max(matriz[fila]))

# Ejercicio 4: Índice de la fila que contiene el máximo valor de una columna dada
def fila_maximo_en_columna(matriz, columna):
    return max(range(len(matriz)), key=lambda i: matriz[i][columna])

# Ejercicio 5: Índice de la fila que contiene el valor máximo de toda la matriz
def fila_del_maximo(matriz):
    max_valor = float('-inf')
    fila_resultado = -1
    for i, fila in enumerate(matriz):
        if max(fila) > max_valor:
            max_valor = max(fila)
            fila_resultado = i
    return fila_resultado
