palabra = input("Ingrese una palabra: ")
n = len(palabra) # pa contar los elementos

# el primer ciclo controla la cantidad de elementos de la cadena comenzando desde 1... (1, 2, 3...)
for elementos in range(1, n + 1):
    
    # El segundo ciclo controla donde empieza la cadena 2
    for inicio in range(n - elementos + 1):
        fin = inicio + elementos
        subcadena = palabra[inicio:fin]
        print(subcadena)

# esto lo que hace es que primero escriba de a una letra, despues de a 2 y asi susecivamente
# algo similar a lo de la burbuja del anterior ejercicio