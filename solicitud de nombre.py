print('PRIMER NOMBRE')
name1 = str(input())
print('SEGUNDO NOMBRE')
name2 = str(input())
print('PRIMER APELLIDO')
surname1 = str(input())
print('SEGUNDO APELLIDO')
surname2 = str(input())
lista = ['CEDULA DE CIUDADANIA','TARJETA DE INDENTIDAD','CEDULA DE EXTRANGERIA','PASAPORTE']
print('1)CEDULA DE CIUDADANIA\n2)TARJETA DE INDENTIDAD\n3)CEDULA DE EXTRANGERIA\n4)PASAPORTE')
tipoid = int(input())


if tipoid in range(1, 4):
    print('NUMERO DE IDENTIFICACION SIN PUNTOS')
    numero_id = str(input())

    if tipoid == 1:
        print(name1 + name2 + surname1 + surname2 + lista[0] + numero_id)
    if tipoid == 2:
        print(name1 + name2 + surname1 + surname2 + lista[1] + numero_id)
    if tipoid == 3:
        print(name1 + name2 + surname1 + surname2 + lista[2] + numero_id)
    if tipoid == 4:
        print(name1 + name2 + surname1 + surname2 + lista[3] + numero_id)

if tipoid <= 0:
    print('ESCOGA UNA OPCION VALIDA')
    print('1)CEDULA DE CIUDADANIA\n2)TARJETA DE INDENTIDAD\n3)CEDULA DE EXTRANGERIA\n4)PASAPORTE')
    tipoidB = int(input())
    if tipoidB > 4:
        print('ERROR ESCRIBA DE NUEVO TODOS LOS DATOS')
    if tipoidB <= 0:
        print('ERROR ESCRIBA DE NUEVO TODOS LOS DATOS')

if tipoid > 4:
    print('ESCOGA UNA OPCION VALIDA')
    print('1)CEDULA DE CIUDADANIA\n2)TARJETA DE INDENTIDAD\n3)CEDULA DE EXTRANGERIA\n4)PASAPORTE')
    tipoidC = int(input())
    if tipoidC > 4:
        print('ERROR ESCRIBA DE NUEVO TODOS LOS DATOS')
    if tipoidC <= 0:
        print('ERROR ESCRIBA DE NUEVO TODOS LOS DATOS')

    else:
        print('NUMERO DE IDENTIFICACION SIN PUNTOS')
        numero_id = str(input())

    if tipoid in range(1):
        print(name1 + name2 + surname1 + surname2 + lista[0] + numero_id)
    if tipoid in range(2):
        print(name1 + name2 + surname1 + surname2 + lista[1] + numero_id)
    if tipoid in range(3):
        print(name1 + name2 + surname1 + surname2 + lista[2] + numero_id)
    if tipoid in range(4):
        print(name1 + name2 + surname1 + surname2 + lista[3] + numero_id)





