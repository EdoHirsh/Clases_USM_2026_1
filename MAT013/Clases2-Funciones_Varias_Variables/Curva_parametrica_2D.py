import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

# funcion auxiliar para graficar en coordenadas polares
def rho(t):
  return np.cos(3*t)

def f(t):
  return rho(t)*np.cos(t)

def g(t):
  return rho(t)*np.sin(t)

def main():
  # Limites de la gráfica
  intervalo_x = [-1,1]
  intervalo_y = [-1,1]

  # Rango del parámetro
  a=0
  b=2*np.pi

  # Número de puntos
  N=1000

  # Crear el vector de parámetros t
  t = np.linspace(a, b, N)

  # Crear el vector de coordenadas X y Y
  X = f(t)
  Y = g(t)

  # Prepaparar la figura
  fig , ax = plt.subplots()

  ax.set_xlim(intervalo_x[0],intervalo_x[1])
  ax.set_ylim(intervalo_y[0],intervalo_y[1])
  ax.set_aspect('equal')

  # Preparar los ejes de coordenadas
  # ax.spines[["left", "bottom"]].set_position(("data", 0))
  # ax.spines[["top", "right"]].set_visible(False)
  # ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
  # ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  ax.set_xticks([-1,0,1])
  ax.set_yticks([-1,0,1])
  ax.grid(True)


  # Dibujar la curva paramétrica
  ax.plot(X, Y)

  # Guardar la figura
  carpeta = Path('./imagenes/')
  if not carpeta.exists():
    Path(carpeta).mkdir()

  archivo = f'{carpeta}/Curva_parametrica_2D.png'

  fig.savefig(archivo, dpi=300, transparent=True)

  # Mostrar la figura
  plt.show()

if __name__ == '__main__':
  main()