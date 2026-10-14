año = int(input("Ingrese un año: "))

if año / 400 == int(año / 400):
    print("El año es bisiesto")
elif año / 100 == int(año / 100):
    print("El año NO es bisiesto")
elif año / 4 == int(año / 4):
    print("El año es bisiesto")
else:
    print("El año NO es bisiesto")

    # % es lo que sobra, el residuo al dividir entre algo. Algo asi como % = (4/2) = 2