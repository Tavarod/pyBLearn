#ciclo while
def calcular_cesantias():
    while True:
        try:
            dias_trabajados_str = input("Ingrese los dias trabajados: ")
            dias_trabajados_str = int(dias_trabajados_str)
            if 0 <= dias_trabajados_str <= 360:
                break
            else:
                print("╬Error: El numero de dias trabajados no puede ser menor a 0 ni mayor a 360╬")
        except ValueError:
            print("╬Error: Por favor ingrese un número entero válido para los días trabajados╬")

    while True:
        try:
            salario_base_str = input("Ingrese el salario base mensual (incluyendo auxilio de transporte si aplica): ")
            salario_base_str = float(salario_base_str)
            if salario_base_str >= 1623500:
                break
            else:
                print("╬El salario no puede ser menor a $1.623.500.╬")
        except ValueError:
            print("╬Error: Por favor ingrese un valor numérico válido para el salario.╬")

    cesantias = (salario_base_str * dias_trabajados_str) / 360
    return cesantias

colaborador = input("Por favor digite su nombre: ")
total_cesantias = calcular_cesantias()

print(f"Total cesantias para : {colaborador} es de ${total_cesantias:,.2f}")




