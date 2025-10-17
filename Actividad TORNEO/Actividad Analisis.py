#calcular el promedio de presiciom
#calcular puntaje total y promedio
#calificar a los alumnos con puntaje bajo, medio y alto.

import pandas as pd

#Acá cargo los datos.
df = pd.read_csv("TEST Analisis Datos.xlsx - Participant Data.csv")
print("Las 5 filas del archivo")
print(df.head(15))
print("-" * 80)

#1
df['Accuracy'] = df['Accuracy'].str.replace('%','').astype(float)

contador = 0
Accuracyacumulada = 0
for i in df['Accuracy']:
    Accuracyacumulada = Accuracyacumulada + 1
    contador = contador + 1

PromedioAccuracy = Accuracyacumulada / contador
print(f"La presicion promedio del curso es de {PromedioAccuracy}" )
print ("-" * 80)

#2

contador2 = 0
puntajeTotal = 0
for i in df['Score']:
    puntajeTotal = puntajeTotal + 1
    contador2 = contador2 +1

puntajePromedio = puntajeTotal / contador2
print(f"El puntaje promedio del curso es de {puntajePromedio}")
print ("-"*80)

#3

for i in range(15):
    if df['Score'][i] < 15000:
        print(f"El alumno {df['First Name'][i]} tiene puntaje bajo")
    elif df['Score'][i] > 17000:
        print(f"El alumno {df['First Name'][i]} tiene puntaje alto")
    else:
        print(f"El alumno {df['First Name'][i]} tiene puntaje medio")

print ("-"*80)