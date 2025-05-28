def verificar_dia_entero(dia):
    try:
        numero = float(dia) # convierte a float para manejar 1.0
        if numero == int(numero): # verifica si es un entero
            return int(numero)
        else:
            return None # no es un entero
    except (ValueError, TypeError):# Si no se puede convertir a float o es un tipo incorrecto
        return None
