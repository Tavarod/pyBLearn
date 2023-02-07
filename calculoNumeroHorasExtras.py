horaEntrada = float(input('Ingrese hora de entrada, sistema horario de 24 horas\n'))
horaSalida = float(input('Ingrese hora de salida, sistema horario de 24 horas\n'))
dia = 24
if horaEntrada == horaSalida:
    horasExtras = dia - 8
    print(dia, ' Horas, que trabajo en su turno')
    print(horasExtras, ' Horas extras que trabajo en su turno')

elif horaEntrada > horaSalida:
    dia1 = horaEntrada - 24
    dia2 = 24 - horaSalida - 24
    dia1Positivo = abs(dia1)
    dia2Positivo = abs(dia2)
    horasTrabajadas = dia1Positivo + dia2Positivo
    print(horasTrabajadas ,' Horas,trabajo hoy')
    if horasTrabajadas > 8:
        horasExtras = horasTrabajadas - 8
        print('El total de Horas extras el día de hoy es de hoy es de, ', horasExtras)

else:
    horasTrabajadas2 = horaEntrada - horaSalida
    valorPositivo = abs(horasTrabajadas2)
    print(valorPositivo, ' Horas, trabajado hoy')
    if valorPositivo > 8:
        horasExtras = valorPositivo - 8
        print('El total de Horas extras el día de hoy es de hoy es de, ', horasExtras)

