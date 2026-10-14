dia = input("Ingrese un dia de la semana: ")
dia = dia.lower()  # Esto es pa que las letras que introduscan las lea en minusculas

if dia == "lunes":
    print("Es inicio de semana. Ánimo con tus actividades")
elif dia == "viernes":
    print("Llego el viernes. Ya casi podemos descansar, solo falta un poquito")
elif dia == "sabado" or dia == "domingo":
    print("¡Es fin de semana! Momento de descansar")
else:
    print("Es un día entre semana común y corriente :(")