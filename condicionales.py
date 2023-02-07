import datetime

print('El condicional if sirve para poder tomar decisiones de rumbo dentro de nuestro progrograma')
print('ESTE PROGRAMA LE DICE SI CUANTO SUMA SU LIQUIDACION')

año = float(360)
smlv = 1000000
subtra = 106454
print('Por favor , diganos su salario : ')
dig_salario = float(input())
total = float(dig_salario / smlv)
#print(total)
print('Dias que trabajo :')
dt = float(input())
cesantias: float = (dt * dig_salario) / año
prima: float = (dt * dig_salario) / año

if dig_salario <= 999999:
    print('Usted no gana un salario minimo legal vigente, cambie de empleo ')
    print('Su salario deberia ser de :', smlv)
    print('Y esto es lo que le debio haber ganado por los dias que trabajo :', (smlv / 30) * dt)

elif (total <= 2):
    print('usted tiene derecho a subsidio de transporte')
    print('Su salario mensual es de :', dig_salario + subtra)
    print('Cesantias = ', cesantias)
    print('Prima = ', prima)
    TOTALa = dig_salario + subtra +cesantias +prima
    print(TOTALa)

else:
    print('usted NO tiene derecho a subsidio de transporte')
    print('Su salario mensual es de :' , dig_salario )
    print('Cesantias = ', cesantias)
    print('Prima = ', prima)
    TOTALb = dig_salario + cesantias + prima
    print(TOTALb)


