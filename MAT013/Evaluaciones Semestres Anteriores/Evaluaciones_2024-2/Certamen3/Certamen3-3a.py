import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def f(x: float)-> float:
  return 2*x

def g(x: float)-> float:
  return x**2

def main():
  intervalo_x_vent = [-0.25,2.25]
  intervalo_y_vent = [-0.25,4.25]
  intervalo_x_graf = [0,2]
  # intervalo_y_graf = [0,10.5]

  # Crear los ejes
  _, ax = plt.subplots(figsize=(10,6))
  ax.set_xlim(*intervalo_x_vent)
  ax.set_ylim(*intervalo_y_vent)
  # ax.set_ylim(bottom=intervalo_y_vent[0])
  ax.set_aspect('equal')

  # Preparar los ejes de coordenadas
  ax.spines[["left", "bottom"]].set_position(("data", 0))
  ax.spines[["top", "right"]].set_visible(False)
  ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
  ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  ax.set_yticks([0,1,2,3,4])
  # ax.set_yticklabels([])
  ax.set_xticks([0,1,2])
  # ax.set_xticklabels([])

  # ocultar los ejes
  # ax.set_axis_off()
  
  # Graficar
  x = np.linspace(*intervalo_x_graf, 100)
  y1 = f(x)
  y2 = g(x)
  ax.plot(x, y1, color='black')
  ax.plot(x, y2, color='black')
  ax.fill_between(x, y1, y2, color='lightblue')

  # Limites del intervalo
  ax.plot([intervalo_x_graf[0],intervalo_x_graf[0]],[np.min([f(intervalo_x_graf[0]),g(intervalo_x_graf[0])]),np.max([f(intervalo_x_graf[0]),g(intervalo_x_graf[0])])],color='black',linestyle='-')
  ax.plot([intervalo_x_graf[1],intervalo_x_graf[1]],[np.min([f(intervalo_x_graf[1]),g(intervalo_x_graf[1])]),np.max([f(intervalo_x_graf[1]),g(intervalo_x_graf[1])])],color='black',linestyle='-')

  # Verifico si la carpeta imagenes existe, si no la creo
  carpeta=Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()
  
  # Guardar la imagen
  plt.savefig(f'./imagenes/Certamen3-3a.png',transparent=True)

  # Mostrar la imagen
  plt.show()


if __name__ == "__main__":
  main()