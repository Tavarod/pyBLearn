name = input('HOLA, por favor digita tu nombre ')
comprobarEdad = True
while comprobarEdad == True:
    edad = int(input('Que edad tienes,'))
    print(name)
    if edad > 70:
        print('Tu entrada es gratis')
    elif edad < 18:
        print('No puedes ingresar')
    elif edad > 17:
        print('Ingresa , paga en la caja por favor')
    else:
        print('ingrese una edad valida')
    break










