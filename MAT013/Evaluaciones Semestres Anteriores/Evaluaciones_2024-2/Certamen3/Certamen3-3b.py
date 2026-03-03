import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def aux(x: float, r: float)-> float:
  R=np.zeros(len(x))
  for i in range(len(x)):
    if r**2 - x[i]**2 >= 0:
      R[i] = np.sqrt(r**2 - x[i]**2)
    else:
      R[i] = 0
  return R

def main():
  # Intervalos de la ventana
  intervalo_x_vent = [-2.25,2.25]
  intervalo_y_vent = [-0.25,2.25]

  # centro y radio del primer circulo
  center1 = (0, 0)
  radius1 = 2

  # centro y radio del segundo circulo
  center2 = (0, 0)
  radius2 = 0

  # numero de puntos
  N = 100

  # Generar los puntos de los circulos
  theta = np.linspace(0, np.pi, N)
  x1 = center1[0] + radius1 * np.cos(theta)
  y1 = center1[1] + radius1 * np.sin(theta)
  x2 = center2[0] + radius2 * np.cos(theta)
  y2 = center2[1] + radius2 * np.sin(theta)

  # Crear los ejes
  _, ax = plt.subplots(figsize=(9,5))
  ax.set_xlim(*intervalo_x_vent)
  ax.set_ylim(*intervalo_y_vent)
  # ax.set_ylim(bottom=intervalo_y_vent[0])
  ax.set_aspect('equal')

  # Preparar los ejes de coordenadas
  ax.spines[["left", "bottom"]].set_position(("data", 0))
  ax.spines[["top", "right"]].set_visible(False)
  ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
  ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  ax.set_yticks([0,1,2])
  # ax.set_yticklabels([])
  ax.set_xticks([-2,-1,0,1,2])
  # ax.set_xticklabels([])


  # Dibujar los circulos
  ax.plot(x1, y1, color='black')
  ax.plot(x2, y2, color='black')

  # Dibujar los segmentos
  ax.plot(np.linspace(-radius1,-radius2,100), np.zeros(100), color='black')
  ax.plot(np.linspace(radius2,radius1,100), np.zeros(100), color='black')


  # Rellenar la region entre los dos circulos
  x = np.linspace(-(center1[0]+radius1),(center1[0]+radius1), N)
  y1_p = np.sqrt(radius1**2 - x**2)
  y2_p = aux(x, radius2)
  # y1_n = -np.sqrt(radius1**2 - x**2)
  # y2_n = -aux(x, radius2)
  # plt.fill_between(x, y1_p, y1_n, where=~(y2_p>y2_n), color='lightblue')
  ax.fill_between(x, y1_p, y2_p, where=None, color='lightblue')
  # ax.fill_between(x, y2_n, y1_n, where=None, color='lightblue')

  # Verifico si la carpeta imagenes existe, si no la creo
  carpeta=Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  # Guardar la imagen
  plt.savefig('./imagenes/Certamen3-3b.png', transparent=True)

  # Mostrar la imagen
  plt.show()

if __name__ == "__main__":
  main()