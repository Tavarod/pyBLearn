#funcion calculo cesantias
def calcular_cesantias(valor):
    dias_trabajados = int(input("Ingrese el número de días trabajados: "))
    salario_base = float(input("Ingrese el salario base mensual (incluyendo auxilio de transporte si aplica): "))
    try:

        if salario_base < 1623500:
            print("El salario no puede ser menor a $1.623.500")
            return None

        if dias_trabajados > 360 or dias_trabajados < 0:
            print("Error: El numero de dias trabajados no puede ser menor a 0 ni mayor a 360")
            return None
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido.")

    cesantias = (salario_base * dias_trabajados) / 360
    print(f"El valor de las cesantías es: ${cesantias:,.2f}")  # Formato de moneda
    return cesantias

colaborador = input("Por favor digite su nombre: ")
calcular_cesantias(colaborador)



