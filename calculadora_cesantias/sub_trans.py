# Colombia 2025 XD salario minimo de popo
SMLV_OFICIAL_ACTUAL = 1423500 # Salario Mínimo Mensual Legal Vigente
VALOR_AUXILIO_OFICIAL = 200000   # Monto del Auxilio de Transporte
LIMITE_MULTIPLO_SMLV = 2           # El límite es 2 veces el SMLV

def calcular_monto_subsidio(salario_empleado_actual):
    """
    Calcula el monto del auxilio de transporte basado en el salario del empleado.
    """
    # aquí se valida, de que salario_empleado_actual sea número y no negativo
    if not isinstance(salario_empleado_actual, (int, float)):
        raise TypeError("El salario del empleado debe ser un valor numérico.")
    if salario_empleado_actual < 0:
        raise ValueError("El salario del empleado no puede ser negativo.")

    # 1. Calcular el umbral para tener derecho al subsidio Esto es 2 veces el SMLV
    umbral_maximo_para_subsidio = LIMITE_MULTIPLO_SMLV * SMLV_OFICIAL_ACTUAL

    # 2. Comparar el salario del empleado con este umbral:
    if salario_empleado_actual <= umbral_maximo_para_subsidio:
        # Si el salario del empleado es MENOR O IGUAL al umbral (2 SMLMV), entonces SÍ tiene derecho al subsidio.
        return VALOR_AUXILIO_OFICIAL # Devuelve el monto completo del subsidio
    else:
        # Si el salario del empleado es MAYOR al umbral (más de 2 SMLMV), entonces NO tiene derecho al subsidio. , sería un descaro XD
        return 0.0 # Devuelve 0 como monto del subsidio