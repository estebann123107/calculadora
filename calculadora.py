from funciones import suma, resta, multiplicacion, division
print("Bienvenido a la calculaora")

while True:
  try:
    numero1=int(input("Ingresa el primer numero: "))
    numero2=int(input("Ingresa el segundo numero: "))
  except ValueError:
    print("Entrada inválida. Por favor, ingresa solo números enteros.")
    print("---------------------------")
    continue

  print("--------------OPERACIONES------------------ ")
  print("1. suma")
  print("2. resta")
  print("3. multiplicacion")
  print("4. Division")
  print("5. Salir")
  print("---------------------------")

  try:
    op=int(input("seleccione una opcion: "))
  except ValueError:
    print("Entrada inválida. Por favor, ingresa un número para la opción.")
    print("---------------------------")
    continue

  print("---------------------------")

  if op == 5:
    print("fin")
    break

  if op == 1:
    print("Suma: ", suma(numero1,numero2))

  elif op == 2:
    print("Resta: ", resta(numero1,numero2))

  elif op == 3:
    print("Multiplicacion: ", multiplicacion(numero1,numero2))

  elif op == 4:
    result_division = division(numero1, numero2)
    if result_division is None:
      print("No se puede dividir por cero.")
    else:
      print("Division: ", result_division)
  else:
    print("Opcion invalida, por favor intente de nuevo.")

  print("---------------------------")