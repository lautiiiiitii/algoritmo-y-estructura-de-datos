# Ejercicio 11: Escribir un método que dada una matriz de enteros y dos enteros que representan índices de fila, intercambie las filas correspondientes de la matriz.
def intercambiar_filas(matriz, fila1, fila2):
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz

# Ejercicio 12: Escribir un método que dada una matriz de enteros y dos enteros que representan índices de columna, intercambie las columnas correspondientes de la matriz.
def intercambiar_columnas(matriz, col1, col2):
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]
    return matriz

# Ejercicio 13: Escribir un método que dada una matriz de enteros rote la matriz a derecha. Se define rotar lamatriz a derecha como la operación que mueve cada uno de los elementos de la matriz una posición a la derecha. 
#En caso de que un elemento al ser movido a la derecha no tenga lugar en la fila en la que se encontraba originalmente, el mismo debe ser puesto en la primera posición de la siguiente fila. 
#En caso que el elemento que no tiene lugar en la fila se encontrara en la última fila, el mismo debe ser llevado a la primera posición de la primera fila.
def rotar_derecha(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    plano = [elem for fila in matriz for elem in fila]
    plano = [plano[-1]] + plano[:-1]  # rotar a derecha
    return [plano[i*columnas:(i+1)*columnas] for i in range(filas)]

# Ejercicio 14: Escribir un método que dada una matriz de enteros rote la matriz a izquierda. Se define rotar la matriz a izquierda como la operación que mueve cada uno de los elementos de la matriz una posición a la izquierda. 
#En caso de que un elemento al ser movido a la izquierda no tenga lugar en la fila en la que se encontraba originalmente, el mismo debe ser puesto en la última posición de la fila anterior. 
#En caso que el elemento que no tiene lugar en la fila se encontrara en la primera fila, el mismo debe ser llevado a la última posición de la última fila.
def rotar_izquierda(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    plano = [elem for fila in matriz for elem in fila]
    plano = plano[1:] + [plano[0]]  # rotar a izquierda
    return [plano[i*columnas:(i+1)*columnas] for i in range(filas)]

# Ejercicio 15: Escribir un método que dadas dos matrices de dobles devuelva una nueva matriz que represente la suma de las matrices que se le pasaron.
def suma_matrices(m1, m2):
    filas, columnas = len(m1), len(m1[0])
    return [[m1[i][j] + m2[i][j] for j in range(columnas)] for i in range(filas)]
