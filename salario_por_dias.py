smlv = True
while smlv:
    smlv_user = float(input("Ingrese su salario diario: "))
    if smlv_user > 32999:
        for day in range(1, 31):
            salario_acumulado = smlv_user * day
            print(day, salario_acumulado)
        smlv = False
    else:
        print("Usted gana menos de un smlv")



