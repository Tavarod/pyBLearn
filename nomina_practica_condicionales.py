año = float(360)
smlv = 1000000
print('Por favor , diganos su salario : ')
dig_salario = float(input())
print('Dias que trabajo :')
dt = float(input())
total = float(dig_salario / smlv)
if dig_salario <= 999999:
    print('Usted no gana un salario minimo legal vigente, cambie de empleo ')
    print('Su salario deberia ser de :', smlv)
    print('Y esto es lo que le debio haber ganado por los dias que trabajo :', (smlv / 30) * dt)
elif total <= 2:
    subtra = 106454
    cesantias: float = (dt * dig_salario) / año
    prima: float = (dt * dig_salario) / año
    print('usted tiene derecho a subsidio de transporte')
    print('Su salario mensual es de :', dig_salario + subtra)
    print('Cesantias = ', cesantias)
    print('Prima = ', prima)
    TOTALa = (dig_salario + subtra + cesantias + prima)
    print('Liquidacion por los dias trabajados:', TOTALa)
else:
    subtra = 106454
    cesantias: float = (dt * dig_salario) / año
    prima: float = (dt * dig_salario) / año
    print('usted NO tiene derecho a subsidio de transporte')
    print('Su salario mensual es de :', dig_salario)
    print('Cesantias = ', cesantias)
    print('Prima = ', prima)
    TOTALb = (dig_salario + cesantias + prima)
    print('Liquidacion por los dias trabajados:', TOTALb)





