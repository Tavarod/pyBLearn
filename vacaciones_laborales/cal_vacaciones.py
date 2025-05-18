def calcular_vacaciones():
    entrada_dias_laborados = int(input("Ingrese los dias laborados: "))
    try:
        dias_laborados = int(entrada_dias_laborados)
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido para los dias laborados.")
        return None # None indicar error y no se pudo calcular

    if dias_laborados > 360:
        print("Error: El numero de dias laborados no puede ser mayor a 360.")
        return 0

    elif dias_laborados < 0:
        print("Error: El numero de dias laborados no puede ser menor a 0.")
        return 0

    dias_vacaciones = (dias_laborados * 15) / 360
    return dias_vacaciones


