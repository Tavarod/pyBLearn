subsidioTransporte = 117172
año = 360
mes = 30
dia = 8

aprobarSalario = True
while aprobarSalario == True:
    salarioColaborador = float(input())
    if salarioColaborador > 999999:
        print('SALARIO APROVADO')

pagoPensionEmpleaor = 12 * salarioColaborador / 100
pagoPensionEmpeado = 4 * salarioColaborador / 100

print(pagoPensionEmpleaor)
print(pagoPensionEmpeado)




