numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 < numero2:
    print("El número menor es:", numero1)
elif numero2 < numero1:
    print("El número menor es:", numero2)
else:
    print("Los dos números son iguales")