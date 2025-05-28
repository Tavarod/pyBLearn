def calcular_cesantias_valor(salario_base_num, dias_trabajados_num):
    """
    Calcula el valor de las cesantías.
    Lanza ValueError si las reglas de ingreso de datos no se cumplen.
    """

    # Validación de reglas de ingreso de datos
    if salario_base_num < 0:
        raise ValueError("El salario base no puede ser negativo.")


    # la condición original era (dias_trabajados > 360 or dias_trabajados < 0) cambio por la siguiente para mayor claridad:
    if not (0 <= dias_trabajados_num <= 360):
        raise ValueError("Días trabajados deben estar entre 0 y 360.")
        # Si la regla es estrictamente > 0, entonces:
        # if dias_trabajados_num <= 0 or dias_trabajados_num > 360:
        #     raise ValueError("Días trabajados deben ser > 0 y <= 360.")

    # Cálculo principal
    cesantias_calculadas = (salario_base_num * dias_trabajados_num) / 360

    return cesantias_calculadas