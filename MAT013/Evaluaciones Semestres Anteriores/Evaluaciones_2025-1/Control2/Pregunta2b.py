import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#! funcion a graficar
def func_f1(x: float):
  return 2*np.sqrt(1-x**2)

def func_f2(x: float):
  return -2*np.sqrt(1-x**2)

def main():
  #! parametros para grafico
  Mostrar_ejes = True
  Ejes_clasicos = True
  Guardar_grafico = True
  Fondo_transparente = True
  Mostrar_grafico = True
  Full_Latex = True

  # tamaaño de fuentes
  tam_fuentes = 16

  if Full_Latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
      "font.size": tam_fuentes,
    })

  # intervalos x e y
  intervalo_x = [-2.5,2.5]
  intervalo_y = [-2.5,2.5]

  # intervalos de las funciones
  intervalo_x_graf = [-0.865,0.865]
  
  # cantidad de puntos en el intervalo
  N=100

  # tamaño de la figura
  # tam_x = 2*(intervalo_x[1]-intervalo_x[0])
  # tam_y = 10*(intervalo_y[1]-intervalo_y[0])
  tam_x = 5
  tam_y = 5

  #! iniciar figura
  _ , ax = plt.subplots(figsize=(tam_x,tam_y))
  ax.set_xlim(*intervalo_x)
  ax.set_ylim(*intervalo_y)
  # ax.set_aspect('equal')

  #* dibujar ejes coordenados
  if Mostrar_ejes & Ejes_clasicos:
    # mover bordes izquierdo e inferior a x = 0 and y = 0, respectivamente
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    # esconder los bordes superior y derecho
    ax.spines[["top", "right"]].set_visible(False)
    # dibujar las flechas de los ejes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  elif not Mostrar_ejes:
    ax.set_axis_off()

  # Graficar la función
  x = np.linspace(intervalo_x_graf[0],intervalo_x_graf[1], N)

  y1 = func_f1(x)
  y2 = np.ones_like(x)
  y3 = -np.ones_like(x)
  y4 = func_f2(x)

  ax.plot(x, y1, '--', color='blue')
  ax.plot(x, y2, '--', color='blue')
  ax.fill_between(x, y1,y2, color='lightblue')
  ax.plot(x, y3, '--', color='blue')
  ax.plot(x, y4, '--', color='blue')
  ax.fill_between(x, y3,y4, color='lightblue')

  #! guardar grafico
  if Guardar_grafico:
    # Verificar si la carpeta imagenes existe, si no, crearla
    carpeta = Path('./imagenes/')
    if not carpeta.exists():
      carpeta.mkdir()

    # Obtener el nombre del archivo actual sin la extension
    Nombre = Path(__file__).stem

    # Nombre del archivo
    archivo = f'{carpeta}/{Nombre}.png'

    # Guardar la figura
    plt.savefig(archivo, dpi=600, transparent=Fondo_transparente)

  #! Mostrar grafico
  if Mostrar_grafico:
    plt.show()

if __name__ == "__main__":
  main()