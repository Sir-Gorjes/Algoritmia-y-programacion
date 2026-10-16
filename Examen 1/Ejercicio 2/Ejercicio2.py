# como "si" es lo unico que nos importa para comenzar el proceso, se crea una variable = si
continuar = "si"

print("\n--- BIENVENID@S A LA SALA DE JUEGOS Arcade-mia de Mancos - TARIFA DE ENTRADA ---")

# listo, para comenzar con el while se necesita saber la edad. entonces lo primero es un input y despues las condiciones
while continuar == "si":
    
    # se pide la edad en entero para que no vaya a haber problemas de: tengo 17 y medio o asi...
    edad = int(input("Ingrese la edad del cliente: "))

    # las condiciones
    if edad < 5:
        print("-> La entrada es GRATIS ($0).")
    elif edad <= 18:
        print("-> El precio de la entrada es: $5")
    else:
        print("-> El precio de la entrada es: $10")
    
    # y aqui cumplo con lo que decia sobre los familiares pa que se repita el while y puedan entrar
    continuar = input("\n¿Desea ingresar la edad de otro cliente? Responda con (si/no): ")
    continuar = continuar.lower() # se me habia olvidado esto pa que lo lea siempre en minuscula 

print("\n¡Gracias por usar el sistema de la sala de juegos!")


# las entradas en este caso serian: La edad del cliente y respuesta para continuar (si/no) 
# Y las salidas serian: Precio de la entrada y el mensaje de despedida
# me paso que cuando tenia que poner la edad sin querer puse "si" cuando lo estaba probando
# segun la IA hay que poner esto para corregirlo pero como no se que es no lo voy a usar (if not entrada.isdigit():)
# tengo que preguntarle al profe sobre eso