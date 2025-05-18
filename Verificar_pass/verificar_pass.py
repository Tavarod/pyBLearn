def verificar_pass(password):
    mensaje_error = []
    caracteres_especiales = ['@', '#', '$', '%', '&', '*', '+', '-', '=', '?', '/', '|', '~', '>', '<', ',', '.', '°',]

    if len(password) < 8:
        mensaje_error.append('el pass debe tener al menos 8 caracteres \u2639')

        mayuscula = False
        numero = False
        especial = False

        for caracter in password:
            if caracter.isupper():
                mayuscula = True
            elif caracter.isdigit():
                numero = True
            elif caracter in caracteres_especiales:
                especial = True

        if not mayuscula:
            mensaje_error.append('el pass debe tener al menos una mayuscula \u2639')
        if not numero:
            mensaje_error.append('el pass debe tener al menos un numero \u2639')
        if not especial:
            mensaje_error.append('el pass debe tener al menos un caracter especial \u2639')

        if not mensaje_error:
            return None #valido
        else:
            return "Contraseña no válida: " + ", ".join(mensaje_error) #no valido


password = input("Ingrese su contraseña: ")
print(verificar_pass(password))

