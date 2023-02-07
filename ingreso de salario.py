#solicitar nombres y apellidos
primer_nombre = input("Ingrese su primer nombre: ")
segundo_nombre = input("Ingrese su segundo nombre: ")
primer_apellido = input("Ingrese su primer apellido: ")
segundo_apellido = input("Ingrese su segundo apellido: ")

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