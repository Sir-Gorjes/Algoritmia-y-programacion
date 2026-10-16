# se crea la caja como una lista vacia ya que la maquina va a ir empacando las bolsas de arroz y se van a ir agregando a la caja
caja = []
maquina = "si"
# se coloca la variable maquina en "si" para que el while se pueda repetir mientras la maquina este encendida

# aqui comenzamos con el while para que mientras la maquina este encendida se pueda seguir empacando bolsas de arroz
while maquina == "si":
    hay_bolsa = input("\n¿Hay una bolsa en la máquina? (si/no): ").lower()

    if hay_bolsa == "si":
        print("1. Vaciando arroz en la bolsa...")
        print("2. Sellando bolsa...")
        print("3. ¡Bolsa empacada en la caja!")
        caja.append("1 Bolsa de arroz")
        # esto es para que cada vez que se empaca una bolsa de arroz, se agregue a la lista de la caja
    else:
        print("¡Alerta! No hay bolsa. Coloque una para continuar.")

    print("Contenido de la caja:", caja)
    maquina = input("\n¿La máquina sigue encendida? (si/no): ").lower() #para que lo tome en minuscula y no haya problemas

print("\nMáquina apagada. Caja final lista para distribución:", caja)
# en caso de que la maquina se apague, se muestra el contenido final de la caja y se termina el programa

#las entradas serian: si hay bolsa y si la maquina sigue encendida
#las salidas serian: el mensaje de empacado, el contenido de la caja y el mensaje de que la maquina se apago y la caja final lista para distribucion