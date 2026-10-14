candidato = input("Elija un candidato por el cual votar (A, B o C): ")
candidato = candidato.upper()

if candidato == "A":
    print("Usted ha votado por el partido rojo")
elif candidato == "B":
    print("Usted ha votado por el partido verde")
elif candidato == "C":
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")