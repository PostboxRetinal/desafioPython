import random
import string

def generar_contrasena():
  longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
  caracteres = string.ascii_letters + string.digits + string.punctuation
  contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
  print("Su contraseña generada es:", contrasena)

def generar_numeros_random():
  cantidad = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))
  limite_inferior = int(input("Ingrese el límite inferior del rango: "))
  limite_superior = int(input("Ingrese el límite superior del rango: "))
  numeros = [random.randint(limite_inferior, limite_superior) for i in range(cantidad)]
  print("Los números aleatorios generados son:", numeros)

def convertir_unidades():
  print("Opciones de conversión:")
  print("1. Convertir Celsius a Fahrenheit")
  print("2. Convertir Kilómetros a Millas")
  opcion = int(input("Seleccione una opción: "))

  if opcion == 1:
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "grados Celsius equivalen a", fahrenheit, "grados Fahrenheit.")
  elif opcion == 2:
    kilometros = float(input("Ingrese la distancia en kilómetros: "))
    millas = kilometros * 0.621371
    print(kilometros, "kilómetros equivalen a", millas, "millas.")
  else:
    print("Opción inválida.")

def calculadora():
  numero1 = float(input("Ingrese el primer número: "))
  numero2 = float(input("Ingrese el segundo número: "))
  print("Operaciones disponibles:")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")
  opcion = int(input("Seleccione una operación: "))

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
  else:
    print("Opción inválida.")

while True:
  print("\nMenú Principal:")
  print("1. Generador de Contraseñas")
  print("2. Generador de Números Aleatorios")
  print("3. Conversor de Unidades")
  print("4. Calculadora")
  print("5. Salir")

  opcion = int(input("Seleccione una opción: "))

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
  else:
    print("Opción inválida. Por favor, seleccione una opción válida.")
