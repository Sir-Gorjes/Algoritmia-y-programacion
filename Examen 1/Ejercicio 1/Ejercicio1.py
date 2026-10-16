# creo variables = 0 para poder meterle los precios del menu 
total = 0
# creo variable en true para que mientras este en true se pueda ordenar con un while
pedir = True

print("¡Bienvenido a El Gordo Gorjes (ElGGs)!")
print("\n--- MENÚ DE COMIDA RÁPIDA ---")
print("\n1. Hamburguesa Especial - $15.000")
print("\n2. Perro Caliente - $10.000")
print("\n3. Salchipapa Familiar - $18.000")
print("\n4. Porción de Papas Fritas - $6.000")
print("\n5. Gaseosa - $4.000")
print("\n6. Finalizar pedido y pagar")

# comienzo con el while y pongo el menu a la vista para que puedan seleccionar las opciones que quieran
# habia colocado el menu debajo del while perp eso tambien se repetia entonces mas bien lo pongo antes de el while

while pedir:
    # creo una vaiable en la que el usuario pueda ingresar las opciones del menu y que la vea reflejada con Print
    opcion = input("\nIngrese el número de la opción que desea pedir: ") 

    # y que dependiendo de la opcion que elija, se le sume el monto a la variable "Total" hasta que pedir sea false para cortar el ciclo
    if opcion == "1":
        total = total + 15000
        print("-> Agregado: Hamburguesa Especial ($15.000)")
    elif opcion == "2":
        total = total + 10000
        print("-> Agregado: Perro Caliente ($10.000)")
    elif opcion == "3":
        total = total + 18000
        print("-> Agregado: Salchipapa Familiar ($18.000)")
    elif opcion == "4":
        total = total + 6000
        print("-> Agregado: Porción de Papas Fritas ($6.000)")
    elif opcion == "5":
        total = total + 4000
        print("-> Agregado: Gaseosa ($4.000)")
    elif opcion == "6":
        pedir = False
        print("\nProcesando la cuenta...")
    # cuando pedir sea false se corta el ciclo while, ya que el programa ve como si no tubiera que repetir mas    
    
    else:
        # mensaje a la ratatuil
        print("\n¡Ups! Nuestro chefcito busco por toda la cocina y no encontro ese tipo de queso.")
        print(" Y Linguini tampoco sabe prepararlo.")

# y aqui comienzan los dolorosos :(
print("\n==================================")
print("  TOTAL A PAGAR: $", total)
print("==================================")
print("¡Gracias por su compra! vuelva pronto")