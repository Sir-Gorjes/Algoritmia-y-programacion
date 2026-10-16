# se crea la caja como una variable vacia ya que la maquina va a ir empacando las bolsas de arroz y se van a ir agregando a la caja
caja = 0
maquina = "si"
# se coloca la variable maquina en "si" para que el while se pueda repetir mientras la maquina este encendida

# aqui comenzamos con el while para que mientras la maquina este encendida se pueda seguir empacando bolsas de arroz
while maquina == "si":
    hay_bolsa = input("\n¿Hay una bolsa en la máquina? (si/no): ").lower()

    if hay_bolsa == "si":
        print("1. Vaciando arroz en la bolsa...")
        print("2. Sellando bolsa...")
        print("3. ¡Bolsa empacada en la caja!")
        caja = caja + 1  # Le sumamos 1 a la variable
        
    else:
        print("¡Alerta! No hay bolsa. Coloque una para continuar.")

    print("Cantidad de bolsas en la caja:", caja)
    maquina = input("\n¿La máquina sigue encendida? (si/no): ").lower() #para que lo tome en minuscula y no haya problemas

print("\nMáquina apagada. Caja final lista para distribución:", caja)
# en caso de que la maquina se apague, se muestra el contenido final de la caja y se termina el programa

#las entradas serian: si hay bolsa y si la maquina sigue encendida
#las salidas serian: el mensaje de empacado, el contenido de la caja y el mensaje de que la maquina se apago