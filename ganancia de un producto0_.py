'''Calcular la diferencia porcentual entre dos valores
Para calcular la diferencia porcentual entre dos valores V1 y V2 podemos usar la siguiente fórmula.
V1 es el valor inicial y V2 es el valor final.
Diferencia porcentual = ((V2-V1) /V1) *100'''
#aca van los string del informe
costo = '\Esto vale el producto=='
costodistri = '\Precio sugerido por el distribuidor=='
veinteporcien = '\Precio con el 20 porciento=='
#perdida con respecto a la ganancia del 20 porciento
perdida_veinte = 'Esto es lo que pierde=='
precio_compra = 1950
margen20 = 0.20
precio_sugerido = 2100
#ganando el 20%
precio_gana20 = (precio_compra * margen20) + precio_compra
print('---------------INFORME---------------☺☺☺')
#porcentaje entre el precio sugerido y el precio al 20 porciento
perdida = ((((precio_gana20 - precio_sugerido) / precio_sugerido) * 100))
perdidaUS = (precio_gana20 - precio_sugerido)
#porcentaje de ganancia con el precio sugerido
gana2 = ((((precio_sugerido - precio_compra) / precio_compra) * 100))
resumen = [ costo, precio_compra , costodistri, precio_sugerido ]
resumen2 = [ veinteporcien, precio_gana20, perdida_veinte, perdidaUS ]
print(resumen)
print(resumen2)
print('\n ')
print('---------------PORCENTAJES---------------♪♪♪♪♪♪♪♪♪')
print('PORCENTAJE DE GANANCIA CON EL PRECIO SUGERIDO=', gana2, 'porciento')
print('LA DIFERENCIA EN PORCENTAJE , ENTRE PRECIO SUGERIDO Y PRECIO DE VENTA AL 20 PORCIENTO ES DE =,', perdida, 'porciento')

















