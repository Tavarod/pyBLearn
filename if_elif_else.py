print('Por favor digita tu nombre')
nombreDelUsuario = str(input())
edadUsuario = int(input('Por favor ingre su edad\n'))
if edadUsuario <= 18:
    print('es menor de edad ' + nombreDelUsuario +' jaime andresy el valor de la entrada es de 100US')
elif edadUsuario >= 70:
    print('Usted es de la tercera edad don ' + nombreDelUsuario + ' y no puede ingresar') 
else:
    print('es mayor de edad y no puede ingresar esto es para niños')


