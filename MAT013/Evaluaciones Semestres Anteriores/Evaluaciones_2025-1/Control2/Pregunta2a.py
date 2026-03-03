import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#! funcion a graficar
def func_f1(x: float):
  return np.sqrt(100-4*x**2)/5

def func_f2(x: float):
  return -np.sqrt(100-4*x**2)/5

def func_f3(x: float):
  return 1-x

def main():
  #! parametros para grafico
  Mostrar_ejes = True
  Ejes_clasicos = True
  Guardar_grafico = True
  Fondo_transparente =True
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
  intervalo_x = [-5.5,5.5]
  intervalo_y = [-3.5,3.5]

  # intervalos de las funciones
  intervalo_x1 = [-5,-0.96]
  intervalo_x2 = [-0.96,2.69]

  # cantidad de puntos en el intervalo
  N=100

  # tamaño de la figura
  # tam_x = 2*(intervalo_x[1]-intervalo_x[0])
  # tam_y = 10*(intervalo_y[1]-intervalo_y[0])
  tam_x = 11
  tam_y = 7

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
  x1 = np.linspace(intervalo_x1[0],intervalo_x1[1], N)
  x2 = np.linspace(intervalo_x2[0],intervalo_x2[1], N)

  y11 = func_f1(x1)
  y12 = func_f2(x1)
  y22 = func_f2(x2)
  y23 = func_f3(x2) 

  ax.plot(x1, y11, color='blue')
  ax.plot(x1, y12, color='blue')
  ax.fill_between(x1, y11,y12, color='lightblue')
  ax.plot(x2, y22, color='blue')
  ax.plot(x2, y23, color='blue')
  ax.fill_between(x2, y22,y23, color='lightblue')

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