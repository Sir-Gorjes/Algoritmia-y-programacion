# 1. pedimos datos al usuario
dia = input("Ingrese el día de la semana: ")
dd = int(input("Ingrese el número del día (DD): "))
mm = int(input("Ingrese el número del mes (MM): "))

dia = dia.lower()

# 2. ponemos la condicion de rechazo
if dd > 31 or mm > 12:
    print("Error en la fecha")
elif dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and dia != "viernes":
    print("Error en el dia de la semana")

# 3. ahora si comenzamos con las condiciones de los dias 
else:
    # lunes, martes o miercoles (examen)
    if dia == "lunes" or dia == "martes" or dia == "miercoles":
        examen = input("¿Hubo exámenes hoy? (si/no): ")
        if examen == "si":
            aprobados = int(input("Cantidad de alumnos aprobados: "))
            reprobados = int(input("Cantidad de alumnos reprobados: "))
            total = aprobados + reprobados
            porcentaje = (aprobados / total) * 100
            print("El porcentaje de aprobados fue:", porcentaje, "%")
        elif examen == "no":
            print("Se salvaron")

    # jueves (practica)
    elif dia == "jueves":
        asistencia = float(input("Ingrese el porcentaje de asistencia: "))
        if asistencia > 50:
            print("asistió la mayoría")
        else:
            print("no asistió la mayoría")

    # viernes (viajeros)
    elif dia == "viernes":
        if dd == 1 and (mm == 1 or mm == 7):
            print("Comienzo de nuevo ciclo")
            alumnos = int(input("Ingrese la cantidad de alumnos: "))
            arancel = float(input("Ingrese el arancel por alumno: "))
            ingreso_total = alumnos * arancel
            print("El ingreso total es de: $", ingreso_total)

# y salio pa pintura