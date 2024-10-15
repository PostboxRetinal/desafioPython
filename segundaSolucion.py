import random
import string

def generar_contrasena():
  while True:
    try:
      longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
      if longitud <= 0:
        print("La longitud debe ser mayor que cero.")
        continue
      break
    except ValueError:
      print("Por favor, ingrese un número entero válido.")

  caracteres = string.ascii_letters + string.digits + string.punctuation
  contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
  print("Su contraseña generada es:", contrasena)

def generar_numeros_random():
  while True:
    try:
      cantidad = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))
      if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
        continue
      break
    except ValueError:
      print("Por favor, ingrese un número entero válido.")

  while True:
    try:
      limite_inferior = int(input("Ingrese el límite inferior del rango: "))
      limite_superior = int(input("Ingrese el límite superior del rango: "))
      if limite_inferior >= limite_superior:
        print("El límite inferior debe ser menor que el límite superior.")
        continue
      break
    except ValueError:
      print("Por favor, ingrese números enteros válidos.")

  numeros = [random.randint(limite_inferior, limite_superior) for i in range(cantidad)]
  print("Los números aleatorios generados son:", numeros)

def convertir_unidades():
  print("Opciones de conversión:")
  print("1. Convertir Celsius a Fahrenheit")
  print("2. Convertir Kilómetros a Millas")

  while True:
    try:
      opcion = int(input("Seleccione una opción: "))
      if opcion not in [1, 2]:
        print("Opción inválida. Por favor, seleccione 1 o 2.")
        continue
      break
    except ValueError:
      print("Por favor, ingrese un número entero válido.")

  if opcion == 1:
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "grados Celsius equivalen a", fahrenheit, "grados Fahrenheit.")
  elif opcion == 2:
    kilometros = float(input("Ingrese la distancia en kilómetros: "))
    millas = kilometros * 0.621371
    print(kilometros, "kilómetros equivalen a", millas, "millas.")


def calculadora():
  while True:
    try:
      numero1 = float(input("Ingrese el primer número: "))
      numero2 = float(input("Ingrese el segundo número: "))
      break
    except ValueError:
      print("Por favor, ingrese números válidos.")

  print("Operaciones disponibles:")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")

  while True:
    try:
      opcion = int(input("Seleccione una operación: "))
      if opcion not in [1, 2, 3, 4]:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue
      break
    except ValueError:
      print("Por favor, ingrese un número entero válido.")

  if opcion == 1:
    resultado = numero1 + numero2
    print("El resultado de la suma es:", resultado)
  elif opcion == 2:
    resultado = numero1 - numero2
    print("El resultado de la resta es:", resultado)
  elif opcion == 3:
    resultado = numero1 * numero2
    print("El resultado de la multiplicación es:", resultado)
  elif opcion == 4:
    if numero2 == 0:
      print("No se puede dividir entre cero.")
    else:
      resultado = numero1 / numero2
      print("El resultado de la división es:", resultado)


while True:
  print("\nMenú Principal:")
  print("1. Generador de Contraseñas")
  print("2. Generador de Números Aleatorios")
  print("3. Conversor de Unidades")
  print("4. Calculadora")
  print("5. Salir")

  while True:
    try:
      opcion = int(input("Seleccione una opción: "))
      if opcion not in [1, 2, 3, 4, 5]:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue
      break
    except ValueError:
      print("Por favor, ingrese un número entero válido.")


  if opcion == 1:
    generar_contrasena()
  elif opcion == 2:
    generar_numeros_random()
  elif opcion == 3:
    convertir_unidades()
  elif opcion == 4:
    calculadora()
  elif opcion == 5:
    print("¡Hasta luego!")
    break
