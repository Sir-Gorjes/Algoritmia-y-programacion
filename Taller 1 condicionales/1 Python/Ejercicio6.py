letra = input("Ingrese una sola letra: ")

if len(letra) != 1:
    print("No se puede procesar el dato. Debe ingresar solo un carácter")
else:
    vocal = letra.lower()
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        print("es vocal")
    else:
        print("no es vocal")


# se usa la funcion len() con el fin de que cuando el usuario coloque cualquier cosa, esta cuente el numero de caracteres
# != estos 2 simnbolos juntos, son lo contrario a ==. significan diferente de...