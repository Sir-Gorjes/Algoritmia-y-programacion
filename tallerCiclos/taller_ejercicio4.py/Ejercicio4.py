# creamos un diccionario en donde el sujeto esta a la izquierda de : y lo que lo acompaña esta a la derecha
notas_de_estudiantes = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
} # diccionario inicial

#  creamos tambien un diccionario vacío donde guardaremos las calificaciones finales
graduados = {} # diccionario final

# hago un ciclo para recorrer el diccionario estudiante por estudiante, donde la variable "estudiante" va a ser el nombre de cada uno
for estudiante in notas_de_estudiantes:
    nota = notas_de_estudiantes[estudiante]  # obtenemos la nota numérica
    
    # y le digo al programa de que en base a la nota, de un resultado usando condicionales 
    if nota >= 91:
        grado = "Pendiente"
    elif nota >= 81:
        grado = "Superaste las expectativas mi querido padawan"
    elif nota >= 71:
        grado = "Aceptable"
    else:
        grado = "Paila, sigue intentando"
    
    # casi por ultimo le decimos que; en el diccionario que teniamos vacio, anota el nombre de cada uno y asígnale el valor de la variable "grado"
    graduados[estudiante] = grado

# con el nuevo diccionario lleno imprimimos el resultado final
print(graduados)

# y listo chocolisto