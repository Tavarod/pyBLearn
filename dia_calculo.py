print('Digite su salario')
mes = float(input())
dia = float(mes / 30)
# print(mes / 30 / 8) otra forma de sacar el dia
hora: float = float(dia / 8)
print('hora ordinaria', hora)
hed = hora / 100 * 25 + hora
print('Hora extra diurna:$', hed)
hn = hora / 100 * 35 + hora
print('Hora nocturna', hn)
hen = hora / 100 * 75 + hora
print('Hora extra nocturna', hen)
hora_dominical = hora / 100 * 75 + hora
print('Hora dominical', hora_dominical)
hedfd = hora / 100 * 100 + hora
print('Hora extra dominical festiva diurna', hedfd)
hedfn = hora / 100 * 150 + hora
print('Hora extra dominical festiva nocturna', hedfn)

print('\nDIA DE LA SEMANA\n1)LUNES\n2)MARTES\n3)MIERCOLES\n4)JUEVES\n5)VIERNES\n6)SABADO\n7)DOMINGO')
print('ESCOGA EL NUMERAL CORRESPONDIENTE AL DIA,:')
num1 = 'LUNES'
num2 = 'MARTES'
num3 = 'MIERCOLES'
num4 = 'JUEVES'
num5 = 'VIERNES'
num6 = 'SABADO'
num7 = 'DOMINGO'
dia_de_la_semana = int(input())
day = []
if dia_de_la_semana == 1:
    print(num1)
    day.append('lunes')
if dia_de_la_semana == 2:
    print(num2)
    day.append('Martes')
if dia_de_la_semana == 3:
    print(num3)
    day.append('Miercoles')
if dia_de_la_semana == 4:
    print(num4)
    day.append('Jueves')
if dia_de_la_semana == 5:
    print(num5)
    day.append('Viernes')
if dia_de_la_semana == 6:
    print(num6)
    day.append('Sabado')
if dia_de_la_semana == 7:
    print(num7)
    day.append('Domingo')

if dia_de_la_semana == 7:
    print('En consecuencia, tanto el domingo como el festivo son días de descanso remunerado, es decir, que están '
          '\npagados dentro del salario normal del trabajador, por lo que no se descuentan de ese salario mensual o '
          '\nquincenal pactado')
    htd = float(input('Numero de HORAS trabajadas:'))
    v0: float = htd * hora_dominical
    print('HOY', day, 'USTED GANO:',)
    print(v0)
    horas_extras_dominical = float(input('CUANTAS HORAS EXTRAS TRABAJO?,'))
    if horas_extras_dominical > 0:
        print('1)Hora extra dominical festiva diurna\n2)Hora extra dominical festiva nocturna\n')
        the = int(input())
        if the == 1:
            print('EL VALOR DE SUS HORAS EXTRAS DOMINICALES FESTIVAS DIURNAS ES DE:', )
            v1: float = horas_extras_dominical * hedfd
            print(v1)
            print('ESTO ES LO QUE USTED GANO POR TRABAJAR UN DOMINGO\n', v1 + v0)
        if the == 2:
            print('EL VALOR DE SUS HORAS EXTRAS DOMINICALES FESTIVAS NOCTURNA ES DE:', )
            v2: float = horas_extras_dominical * hedfn
            print(v2)
else:
    ht = float(input('Numero de HORAS trabajadas:'))
    if ht > 8:
        print('La jornada laboral en Colombia es de máximo 8 horas, de acuerdo al artículo 611 del código sustantivo '
              'del trabajo.')
        print('Estas son sus horas extras ', ht - 8,'\n¿quiere hacer el alculo de su salario con sus horas extras?')
        print('\n1=si\n2=no')
        pregunta = int(input())
        if pregunta == 1:
            user_money_day = (mes / 30 / 8) * 8
            horas_extras = ht - 8
            print('1)Hora extra diurna\n2)Hora extra nocturna\n3)Hora extra dominical festiva '
                  'diurna\n4)Hora extra dominical festiva nocturna\n')
            the = int(input())
            if the == 1:
                print('EL VALOR DE SUS HORAS EXTRAS DIURNAS ES DE:', )
                v1: float = horas_extras * hed
                print(v1)
                print('ESTO ES LO QUE USTED GANO HOY  \n', day, v1 + user_money_day)

            if the == 2:
                print('EL VALOR DE SUS HORAS EXTRAS NOCTURNAS ES DE:', )
                v2: float = horas_extras * hen
                print(v2)
                print('ESTO ES LO QUE USTED GANO\n', day, v2 + user_money_day)

            if the == 3:
                print('EL VALOR DE SUS HORAS EXTRAS DOMINICALES FESTIVAS DIURNAS ES DE:', )
                v3: float = horas_extras * hedfd
                print(v3)
                print('ESTO ES LO QUE USTED GANO\n', day, v3 + user_money_day)

            if the == 4:
                print('EL VALOR DE SUS HORAS EXTRAS DOMINICALES FESTIVAS NOCTURNA ES DE:', )
                v4: float = horas_extras * hedfn
                print(v4)
                print('ESTO ES LO QUE USTED GANO\n', day, v4 + user_money_day)


    else:
        #user_money_day ,valor de dia total de trabajo
        user_money_day = ht * hora
        print('HOY', day, 'USTED GANO', user_money_day)
        horas_extras = float(input('CUANTAS HORAS EXTRAS TRABAJO?,'))
        if horas_extras > 0:
            print('1)Hora extra diurna\n2)Hora extra nocturna\n3)Hora extra dominical festiva '
              'diurna\n4)Hora extra dominical festiva nocturna\n')
        the = int(input())
        if the == 1:
            print('EL VALOR DE SUS HORAS EXTRAS DIURNAS ES DE:', )
            v1: float = horas_extras * hed
            print(v1)
            print('ESTO ES LO QUE USTED GANO HOY  \n', day, v1 + user_money_day)

        if the == 2:
            print('EL VALOR DE SUS HORAS EXTRAS NOCTURNAS ES DE:', )
            v2: float = horas_extras * hen
            print(v2)
            print('ESTO ES LO QUE USTED GANO\n', day, v2 + user_money_day)

        if the == 3:
            print('EL VALOR DE SUS HORAS EXTRAS DOMINICALES FESTIVAS DIURNAS ES DE:', )
            v3: float = horas_extras * hedfd
            print(v3)
            print('ESTO ES LO QUE USTED GANO\n', day, v3 + user_money_day)

        if the == 4:
            print('EL VALOR DE SUS HORAS EXTRAS DOMINICALES FESTIVAS NOCTURNA ES DE:', )
            v4: float = horas_extras * hedfn
            print(v4)
            print('ESTO ES LO QUE USTED GANO\n', day, v4 + user_money_day)
