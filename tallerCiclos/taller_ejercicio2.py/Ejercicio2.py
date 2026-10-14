# lista dada por el ejercicio
lista = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]

# lo mejor es usar len porque claramente la lista esta desorganizada
desorden = len(lista)  

for a in range(desorden): # rondas que se repite la revision 
    for b in range(0, desorden - 1): # conjunto de parejas que se corrigen arrancando desde posicion 0
        if lista[b] > lista[b + 1]:
            quieto = lista[b]         #Como no es mayor, el codigo dentro del if no se ejecuta y la pareja se queda quieta
            lista[b] = lista[b + 1]
            lista[b + 1] = quieto    #Como si es mayor, el programa entra al if y ejecuta el intercambio: el 4 pasa a la derecha y el 3 pasa a la izquierda en el segundo ciclo

        # buscando me di cuenta que para este ejercicio hay un metodo que se llama el metodo de la burbuja 
        # este selecciona 2 posiciones, compara entre 2 numeros y si el de la izquierda es mayor al de la derecha
        # cambia a otra pareja de elementos hasta que se organiza toda la lista 

print("Lista ordenada con ciclos:", lista)

# 2. VERIFICACIÓN CON FUNCIÓN PREDETERMINADA
lista_original = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]
lista_original.sort()  # .sort() es la función integrada de Python

print("Lista ordenada con .sort():", lista_original)

# Y sale pa paint