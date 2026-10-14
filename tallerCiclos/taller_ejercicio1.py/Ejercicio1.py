precio = 1.90

#Menu del ejercicio como referencia
while True:
    print("--- MENU DE TOPPINGS ---")
    print("0. Sin topping ($1.90)")
    print("1. Frutas (+$0.50)")
    print("2. Granola (+$1.50)")
    print("3. Oreo (+$1.00)")
    print("4. Brownie (+$0.75)")
    
    opcion = input("Seleccione una opcion (0-4): ")
    
    # Si la opcion esta dentro de las seleccionables, funciona
    if opcion in ["0", "1", "2", "3", "4"]:
        # Si la opcion no esta dentro de las seleccionables 'break'
        break
    
    print("Opción inválida. Intente nuevamente.\n")

# Si elige una opcion correcta, se comienzan a anexar los precios de los toppings
if opcion == "1":
    precio = precio + 0.50
elif opcion == "2":
    precio = precio + 1.50
elif opcion == "3":
    precio = precio + 1.00
elif opcion == "4":
    precio = precio + 0.75

print("\nEl total a pagar es: $", precio)