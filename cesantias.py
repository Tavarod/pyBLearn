"""Calcula las cesantías, pide los datos al usuario."""

def calcular_cesantias():

  try:
      dias_trabajados = int(input("Ingrese el número de días trabajados: "))
      salario_base = float(input("Ingrese el salario base mensual (incluyendo auxilio de transporte si aplica): "))

      if dias_trabajados > 360 or dias_trabajados < 0:
        print("Error: El numero de dias trabajados no puede ser menor a 0 ni mayor a 360")
        return None

      cesantias = (salario_base * dias_trabajados) / 360
      print(f"El valor de las cesantías es: ${cesantias:,.2f}") #Formato de moneda
      return cesantias

  except ValueError:
      print("Error: Por favor, ingrese valores numéricos válidos.")
      return None


print(calcular_cesantias())

"""
El razonamiento detrás del único return en este ejercicio es que se utiliza para terminar la ejecución de la función en 
casos excepcionales, como cuando los días trabajados ingresados están fuera del rango permitido 
(menor que 0 o mayor que 360). La idea es detener la función en ese momento para evitar cálculos incorrectos.

En el caso de la línea donde calculas las cesantías y las imprimes, el propósito es mostrar el resultado en pantalla, 
no necesariamente terminar la función. Si quisieras devolver el valor de cesantias, podrías hacerlo agregando un return 
cesantias después de imprimir el resultado. Esto permitiría utilizar el valor calculado en otros contextos 
fuera de la función.
"""
