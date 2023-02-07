print ("hola, como te llamas")
nombre=input()
print ("que edad tienes")
edad=input()
año=360
print ("cual es tu salario?")
salario= int (input()) 
vdia= salario / int (30)
print ("cuantos dias trabajaste")
diastrabajados= int (input())
cesantias= salario * (diastrabajados/año)
print ("el valor de tu cesantias es de " + str (cesantias))

