#prima basico
def calcular_prima_interactivo():
  """Calcula la prima con los datos que le da el usuario."""
  try:
      dias_trabajados = int(input("Ingrese el número de días trabajados: "))
      salario_base = float(input("Ingrese el salario base mensual (incluyendo auxilio de transporte si aplica): "))

      if dias_trabajados > 360 or dias_trabajados < 0:
        print("Error: El numero de dias trabajados no puede ser menor a 0 ni mayor a 360")
        return

      cesantias = (salario_base * dias_trabajados) / 360
      print(f"El valor de la prima es: ${cesantias:,.2f}") #Formato de moneda

  except ValueError:
      print("Error: Por favor, ingrese valores numéricos válidos.")


print(calcular_prima_interactivo())