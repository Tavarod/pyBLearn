decicion = True
while decicion == True:
    decicion = str(input('desea contibuar\n si-no\n'))
    if decicion.upper == 'si':
        decicion = False
    elif decicion.upper == 'no':
        decicion = False
    else:
        print('seleccione si-no')