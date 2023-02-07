años= int (360)
print ("Dime tu nombre, porfavor")
saludo= "hola"
nombre= input()
print(saludo)
print ("que edad tienes?")
edad= input()
print ("ahora dinos cuanto ganas ")
salario = int (input())
print ("cuantos dias trabajas al mes ")
dias_trabajados = int (input())
horas= int (8)
resultado = salario / dias_trabajados
print ("tu dia laboral equivale a --." + str(resultado))
print ("y tu hora laboral vale..." + str(resultado / horas))
cesantias= salario * dias_trabajados / años
print ("tus cesantias son de" + str(cesantias))



