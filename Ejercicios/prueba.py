import random
import time
import turtle




# Dimensiones del tablero
ANCHO = 500
ALTO = 500

# Tamaño de la serpiente
TAMANO_CUADRO = 20

# Velocidad inicial
VELOCIDAD = 200

# Direccion inicial
DIRECCION = "derecha"

# Lista que guarda la serpiente
SEGMENTOS = []

# Posición de la comida
COMIDA = (0, 0)

def dibujar_tablero():
  """Dibuja el tablero del juego."""
  turtle.setup(ANCHO, ALTO)
  turtle.penup()
  turtle.goto(-ANCHO/2, -ALTO/2)
  turtle.pendown()
  turtle.setcolor("black")
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(ANCHO)
    turtle.left(90)
  turtle.end_fill()

def dibujar_serpiente():
  """Dibuja la serpiente en el tablero."""
  for i, segmento in enumerate(SEGMENTOS):
    if i == 0:
      turtle.color("red")
    else:
      turtle.color("green")
    turtle.penup()
    turtle.goto(segmento[0], segmento[1])
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(TAMANO_CUADRO/2)
    turtle.end_fill()

def mover_serpiente():
  """Mueve la serpiente en la dirección actual."""
  global DIRECCION

  # Obtener la cabeza de la serpiente
  cabeza_x, cabeza_y = SEGMENTOS[0]

  # Calcular la nueva posición de la cabeza
  if DIRECCION == "derecha":
    cabeza_x += TAMANO_CUADRO
  elif DIRECCION == "izquierda":
    cabeza_x -= TAMANO_CUADRO
  elif DIRECCION == "arriba":
    cabeza_y += TAMANO_CUADRO
  elif DIRECCION == "abajo":
    cabeza_y -= TAMANO_CUADRO

  # Insertar la nueva cabeza al inicio de la lista
  SEGMENTOS.insert(0, (cabeza_x, cabeza_y))

  # Eliminar el último segmento si la serpiente no ha crecido
  if len(SEGMENTOS) > len(SEGMENTOS_INICIALES):
    SEGMENTOS.pop()

def generar_comida():
  """Genera una nueva posición aleatoria para la comida."""
  global COMIDA

  while True:
    x = random.randint(-ANCHO/2 + TAMANO_CUADRO, ANCHO/2 - TAMANO_CUADRO)
    y = random.randint(-ALTO/2 + TAMANO_CUADRO, ALTO/2 - TAMANO_CUADRO)

    # Asegurar que la comida no aparezca dentro de la serpiente
    if not any(segmento == (x, y) for segmento in SEGMENTOS):
      COMIDA = (x, y)
      break

def dibujar_comida():
  """Dibuja la comida en el tablero."""
  turtle.penup()
  turtle.goto(COMIDA[0], COMIDA[1])
  turtle.pendown()
  turtle.color("yellow")
  turtle.begin_fill()
  turtle.circle(TAMANO_CUADRO/2)
  turtle.end_fill()

def detectar_colision():
  """Detecta si la serpiente ha chocado con algo."""
  global JUEGO_ACTIVO

  cabeza_x, cabeza_y = SEGMENTOS[0]

  # Chocar con el borde del tablero
  if cabeza_x < -ANCHO/2 or cabeza_x > ANCHO/2 or cabeza_y < -ALTO/2 or cabeza_y > ALTO/2:
    JUEGO_ACTIVO = False

  # Chocar con la serpiente misma
  if any(segmento == (cabeza_x, cabeza_y) for segmento in SEGMENTOS[1:]):
    JUEGO_ACTIVO = False

def actualizar_pantalla():
  """Actualiza la pantalla con los nuevos dibujos."""
  turtle.clear()
  dibujar_tablero()
  dibujar_serpiente()
  dibujar_comida()


def manejar_teclas():
  """Maneja las teclas presionadas por el usuario."""
  global DIRECCION

  for key in turtle.get_pressed():
    if key == "Up":
      if DIRECCION != "abajo":
        DIRECCION = "arriba"
    elif key == "Down":
      if DIRECCION != "arriba":
        DIRECCION = "abajo"
    elif key == "Right":
      if DIRECCION != "izquierda":
        DIRECCION = "derecha"
    elif key == "Left":
      if DIRECCION != "derecha":
        DIRECCION = "izquierda"

def main():
  """Función principal del juego."""
  global JUEGO_ACTIVO, SEGMENTOS_INICIALES

  # Inicializar variables
  JUEGO_ACTIVO = True
  SEGMENTOS_INICIALES = [(0, 0), (-TAMANO_CUADRO, 0), (-2 * TAMANO_CUADRO, 0)]
  SEGMENTOS = SEGMENTOS_INICIALES[:]

  # Dibujar el tablero y la serpiente inicial
  dibujar_tablero()
  dibujar_serpiente()

  # Generar la comida inicial
  generar_comida()

  # Bucle principal del juego
  while JUEGO_ACTIVO:
    # Actualizar la pantalla
    actualizar_pantalla()

    # Mover la serpiente
    mover_serpiente()

    # Detectar colisiones
    detectar_colision()

    # Generar nueva comida si la serpiente la come
    if SEGMENTOS[0] == COMIDA:
      generar_comida()
      SEGMENTOS.append((0, 0))

    # Controlar la velocidad del juego
    time.sleep(1 / VELOCIDAD)

    # Manejar las teclas presionadas
    manejar_teclas()

  # Mostrar mensaje de fin de juego
  turtle.clear()
  turtle.penup()
  turtle.goto(0, 0)
  turtle.pendown()
  turtle.color("red")
  turtle.write("¡Juego terminado!", align="center", font=("Arial", 24, "normal"))
  turtle.done()

if __name__ == "__main__":
  main()