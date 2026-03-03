import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

# funcion auxiliar para graficar en coordenadas polares
def rho(t):
  return np.sqrt(9-(t-3)**2)

def f(t):
  return rho(t)*np.cos(10*np.pi*t/6)

def g(t):
  return rho(t)*np.sin(10*np.pi*t/6)

def h(t):
  return t

def main():
  # Limites de la gráfica
  intervalo_x = [-3,3]
  intervalo_y = [-3,3]
  intervalo_z = [0,6]

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
  Z = h(t)

  # Prepaparar la figura
  fig , ax = plt.subplots(subplot_kw={'projection':'3d'})

  ax.set_xlim(intervalo_x[0],intervalo_x[1])
  ax.set_ylim(intervalo_y[0],intervalo_y[1])
  ax.set_zlim(intervalo_z[0],intervalo_z[1])
  # ax.set_aspect('equal')

  # Preparar los ejes de coordenadas
  # ax.set_xticks([-1,0,1])
  # ax.set_yticks([-1,0,1])
  ax.grid(True)


  # Dibujar la curva paramétrica
  ax.plot(X, Y, Z)

  # Guardar la figura
  carpeta = Path('./imagenes/')
  if not carpeta.exists():
    Path(carpeta).mkdir()

  archivo = f'{carpeta}/Curva_parametrica_3D.png'

  fig.savefig(archivo, dpi=300, transparent=True)

  # Mostrar la figura
  plt.show()

if __name__ == '__main__':
  main()