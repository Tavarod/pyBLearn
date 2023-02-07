"""esta es lo que se hace con while se inicializa con una variable que es la que itera
 se coloca una condicion despues del while se inclementa esa variable o se cambia para evitar el bucle infinito """

comprobar = True

while comprobar == True:
    personas = int(input('Cantidad e personas a evaluar\n'))
    if personas > 1:
        comprobar = False
        print('NUMERO DE PERSONAS INGRESADO')
        salario_h = 0
        salario_m = 0
        edad_h = 0
        edad_m = 0
        escolaridad_h = 0
        escolaridad_m = 0
        conteo_h = 0
        conteo_m = 0

        i = 1
        while i <= personas:
            print('valor')
            salario = float(input('INGRESE SALARIO\n'))
            edad = float(input('INGRESE SU EDAD POR FAVOR\n'))
            escolaridad = float(input(' NIVEL DE ESTUDIOS:\n1)PRIMARIA\n2)SECUNDARIA\n3)TECNICO\n4)UNIVERSITARIO\n'))

            comprobar_genero = True

            while comprobar_genero == True:
                genero = input('GENERO DE NACIMIENTO (F)(M)\n')

                '.upper cambia el valor ingresado a mayuscula y el contrario es lower '
                if genero.upper() == 'M':
                    salario_h += salario
                    edad_h += edad
                    escolaridad_h += escolaridad
                    conteo_h += 1
                    comprobar_genero = False
                elif genero.upper() == 'F':
                    salario_m += salario
                    edad_m += edad
                    escolaridad_m += escolaridad
                    conteo_m += 1
                    comprobar_genero = False
                else:
                    print('P0R FAVOR SELECCIONE SU GENERO DE NACIMIENTO YA SEA MASCULINO(M) O FEMENINO(F)')
                i += 1

        '''aca van los promedios se inicializan en 0 para para cuando solo hay mueres o solo hombres'''
        promedio_salarioh = 0
        promedio_edadh = 0
        promedio_escolaridad_h = 0
        if conteo_h > 0:
            promedio_salarioh = salario_h / conteo_h
            promedio_edadh = edad_h / conteo_h
            promedio_escolaridad_h = escolaridad_h / conteo_h

        promedio_salariom = 0
        promedio_edadm = 0
        promedio_escolaridad_m = 0
        if conteo_m > 0:
            promedio_salariom = salario_m / conteo_m
            promedio_edadm = edad_m / conteo_m
            promedio_escolaridad_m = escolaridad_m / conteo_m


        print('Promedio salarial hombres: $', promedio_salarioh)
        print('Promedio edad hombres:', promedio_edadh)
        print('Promedio escolaridad hombres:', promedio_escolaridad_h)
        print('Promedio salario mujeres: $', promedio_salariom)
        print('Promedio edad mujeres:', promedio_edadm)
        print('promedio escolaridad mujeres:', promedio_escolaridad_m)

    else:
        print('El número de personas debe ser mayor que UNO , RECUERDE ES UN PROGRAMA DE PROMEDIOS')