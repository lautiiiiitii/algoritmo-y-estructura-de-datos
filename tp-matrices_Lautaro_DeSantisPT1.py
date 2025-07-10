# Ejercicio 1: Escribir un método que dada una matriz de enteros devuelva la suma de los elementos que contiene la matriz.
def suma_matriz(matriz):
    return sum(sum(fila) for fila in matriz)

# Ejercicio 2: Escribir un método que dada una matriz de enteros devuelva la cantidad de elementos positivos que contiene la matriz.
def contar_positivos(matriz):
    return sum(1 for fila in matriz for elem in fila if elem > 0)

# Ejercicio 3: Escribir un método que dada una matriz de enteros y un entero que representa un índice de fila, devuelva la columna que contiene el máximo elemento de esa fila.
def columna_maximo_en_fila(matriz, fila):
    return matriz[fila].index(max(matriz[fila]))

# Ejercicio 4: Escribir un método que dada una matriz de enteros y un entero que representa un índice de columna, devuelva la fila que contiene el máximo elemento de esa columna.
def fila_maximo_en_columna(matriz, columna):
    return max(range(len(matriz)), key=lambda i: matriz[i][columna])

# Ejercicio 5: Escribir un método que dada una matriz de enteros devuelva la fila que contiene el máximo elemento de la matriz.
def fila_del_maximo(matriz):
    max_valor = float('-inf')
    fila_resultado = -1
    for i, fila in enumerate(matriz):
        if max(fila) > max_valor:
            max_valor = max(fila)
            fila_resultado = i
    return fila_resultado
