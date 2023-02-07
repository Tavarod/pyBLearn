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
elif tieneLaClaveSecreta == clave:
    print('Es valido para ingreso ')
else:
    print('No puede ingresar este lugar es solo para menores de edad')
