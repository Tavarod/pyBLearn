#solicitar nombres y apellidos
while True:
    #comprobar primer nombre
    primer_nombre = input("Su primer nombre por favor : ")
    if primer_nombre.isalpha():
        print(f"guardado¡¡{primer_nombre}!!")
        #comprobar segundo nombre
        segundo_nombre = input("Su segundo nombre por favor : ")
        if segundo_nombre.isalpha():
            print(f"guardado¡¡{segundo_nombre}!!")
            #comprobar primer apellido
            primer_apellido = input("Su primer apellido por favor : ")
            if primer_apellido.isalpha():
                print(f"guardado¡¡{primer_apellido}!!")
                #comprobar segundo apellido
                segundo_apellido = input("Su segundo apellido por favor : ")
                if segundo_apellido.isalpha():
                    print(f"guardado¡¡{segundo_apellido}!!")
                    break
                else:
                    print("apellido no valido")
            else:
                print("apellido no valido")
        else:
            print("nombre no valido")
    else:
        print("nombre no valido")

# Mostrar saludo con los nombres y apellidos ingresados
print(f"{primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}")

#solicitar y validar salario
#se ha utilizado el método isdigit de las cadenas de caracteres para verificar si el salario es un número
#Son método Python isdigit () para detectar una cadena que consta de sólo números

while True:
    salario = input("Ingrese su salario: ")
    if salario.isdigit():
        salario = int(salario)
        if salario >= 1160000:
            print("Salario ingresado")
            break
        else:
            print("Usted gana menos de un salario mínimo, no es posible realizar el cálculo")
    else:
        print("Valor no valido")








