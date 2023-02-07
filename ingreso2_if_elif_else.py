print('Por favor digite su nombre\n')
nombreDelUsuario = str(input())
print('Por favor digite su edad')
edadUsuario = float(input())
clave = 'fedora'
tieneLaClaveSecreta = clave
print('tiene la clave secreta , digitela porfavor')
tieneLaClaveSecreta = input()

if edadUsuario < 18:
    print('Es valido para el ingreso')
    print('A)Carrusel , B)Pscina de pelotas C)Pscina de gelatina')
    opcion = input()
    if opcion == 'A' :
        print('Tercera puerta a la derecha')
    if opcion == 'B' :
        print('Segunda puerta arriba')
    if opcion == 'C' :
        print('Baje al sotano')        

elif tieneLaClaveSecreta == clave:
    print('Es valido para ingreso ')
else:
    print('No puede ingresar este lugar es solo para menores de edad')
