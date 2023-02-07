passCon = True
while passCon == True:
    pass1 = int(input('Por favor digite su contraseña'))
    pass2 = int(input('Confirme su contraseña'))
    if pass1 == pass2:
        print('Pass load')
    elif pass1 != pass2:
        print('Confinmacion Invalida')
        passCon = False
        break
confirIdent = True
while confirIdent == True:
    identUser = int(input('Por favor digite su número de identificacion\n'))
    if identUser > 50000000:
        print('Esta es su identificacion', identUser)
        valPass = True
    else:
        print('Por favor , digite un número de cedula valido')
        confirIdent = False









