import random
import string
import ipywidgets as widgets
from IPython.display import display, clear_output

# Funciones
def generar_contrasena(longitud):
  caracteres = string.ascii_letters + string.digits + string.punctuation
  contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
  return contrasena

def generar_numeros_random(cantidad, limite_inferior, limite_superior):
  numeros = [random.randint(limite_inferior, limite_superior) for i in range(cantidad)]
  return numeros

def convertir_unidades(valor, opcion):
  if opcion == 'Celsius a Fahrenheit':
    resultado = (valor * 9/5) + 32
    unidad_resultado = 'Fahrenheit'
  elif opcion == 'Kilómetros a Millas':
    resultado = valor * 0.621371
    unidad_resultado = 'Millas'
  else:
    resultado = None
    unidad_resultado = None
  return resultado, unidad_resultado

def calculadora(numero1, numero2, operacion):
  if operacion == 'Suma':
    resultado = numero1 + numero2
  elif operacion == 'Resta':
    resultado = numero1 - numero2
  elif operacion == 'Multiplicación':
    resultado = numero1 * numero2
  elif operacion == 'División':
    if numero2 == 0:
      resultado = 'Error: División entre cero'
    else:
      resultado = numero1 / numero2
  else:
    resultado = None
  return resultado

# Interfaz con widgets
output = widgets.Output()

menu_principal = widgets.Dropdown(
    options=['Generador de Contraseñas', 'Generador de Números Aleatorios', 'Conversor de Unidades', 'Calculadora'],
    value='Generador de Contraseñas',
    description='Seleccionar:',
    style={'description_width': 'initial'}
)

longitud_contrasena = widgets.IntSlider(value=12, min=8, max=32, step=1, description='Longitud:')
generar_contrasena_button = widgets.Button(description='Generar Contraseña')

cantidad_numeros = widgets.IntText(value=10, description='Cantidad:')
limite_inferior_numeros = widgets.IntText(value=1, description='Límite Inferior:')
limite_superior_numeros = widgets.IntText(value=100, description='Límite Superior:')
generar_numeros_button = widgets.Button(description='Generar Números')

conversor_unidad_dropdown = widgets.Dropdown(options=['Celsius a Fahrenheit', 'Kilómetros a Millas'], value='Celsius a Fahrenheit', description='Convertir:')
valor_unidad = widgets.FloatText(value=0, description='Valor:')
convertir_unidad_button = widgets.Button(description='Convertir')
numero1_calculadora = widgets.FloatText(value=0, description='Número 1:')
numero2_calculadora = widgets.FloatText(value=0, description='Número 2:')
operacion_calculadora = widgets.Dropdown(options=['Suma', 'Resta', 'Multiplicación', 'División'], value='Suma', description='Operación:')
calcular_button = widgets.Button(description='Calcular')

def on_menu_change(change):
  with output:
    clear_output()
    if change['new'] == 'Generador de Contraseñas':
      display(longitud_contrasena, generar_contrasena_button)
    elif change['new'] == 'Generador de Números Aleatorios':
      display(cantidad_numeros, limite_inferior_numeros, limite_superior_numeros, generar_numeros_button)
    elif change['new'] == 'Conversor de Unidades':
      display(conversor_unidad_dropdown, valor_unidad, convertir_unidad_button)
    elif change['new'] == 'Calculadora':
      display(numero1_calculadora, numero2_calculadora, operacion_calculadora, calcular_button)

def on_generar_contrasena_clicked(b):
  with output:
    clear_output()
    contrasena = generar_contrasena(longitud_contrasena.value)
    print('Contraseña generada:', contrasena)

def on_generar_numeros_clicked(b):
  with output:
    clear_output()
    numeros = generar_numeros_random(cantidad_numeros.value, limite_inferior_numeros.value, limite_superior_numeros.value)
    print('Números generados:', numeros)

def on_convertir_unidad_clicked(b):
  with output:
    clear_output()
    resultado, unidad_resultado = convertir_unidades(valor_unidad.value, conversor_unidad_dropdown.value)
    if resultado is not None:
      print(f'{valor_unidad.value} {conversor_unidad_dropdown.value.split(" a ")[0]} equivalen a {resultado} {unidad_resultado}')
    else:
      print('Error en la conversión')

def on_calcular_clicked(b):
  with output:
    clear_output()
    resultado = calculadora(numero1_calculadora.value, numero2_calculadora.value, operacion_calculadora.value)
    if resultado is not None:
      print('Resultado:', resultado)
    else:
      print('Error en la operación')

# Asociar eventos a los botones
menu_principal.observe(on_menu_change, names='value')
generar_contrasena_button.on_click(on_generar_contrasena_clicked)
generar_numeros_button.on_click(on_generar_numeros_clicked)
convertir_unidad_button.on_click(on_convertir_unidad_clicked)
calcular_button.on_click(on_calcular_clicked)

# Mostrar el menú principal y el output
display(menu_principal, output)
