import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.special as special

from matplotlib.animation import FuncAnimation
from mpl_toolkits.axisartist.axislines import AxesZero
from pathlib import Path

def func_f(x) -> float:
  return np.exp(x)

def Taylor(x: float,n: int) -> float:
  return np.sum([(x**i)/special.factorial(i) for i in range(n+1)])

def main():
  #! parametros para grafico
  Full_Latex = True
  Guardar_grafico = False
  Fondo_transparente = False
  Mostrar_grafico = True
  Animado = False
  Tam_fuentes=16

  # Parametros de la animación
  N_base = 0
  N_Max = 20
  N_add = N_Max-N_base

  Res_EjeX=1000


  # Multiplicador para suaavizar la animación
  Mult = 10

  intervalo_x_fig=[-10.1,10.1]
  intervalo_y_fig=[-2.1,2.1]
  intervalo_x_graf=intervalo_x_fig

  # Definir la función
  x=np.linspace(*intervalo_x_graf,Res_EjeX)
  y=func_f(x)

  # tamaño de la figura
  tam_x = 12
  tam_y = 6

  if Full_Latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
      "font.size": Tam_fuentes
    })

  #! iniciar figura
  fig = plt.figure(figsize=(tam_x,tam_y))
  ax = fig.add_subplot(axes_class=AxesZero)
  ax.set_xlim(*intervalo_x_fig)
  ax.set_ylim(*intervalo_y_fig)
  # ax.set_aspect('equal')

  if Animado:
    # Animación del ajuste
    def update(frame):
      # Limpio el grafico
      ax.clear()

      # Redeclaro los ejes
      ax.set_xlim(*intervalo_x_fig)
      ax.set_ylim(*intervalo_y_fig)

      for direction in ["xzero", "yzero"]:
        # adds arrows at the ends of each axis
        ax.axis[direction].set_axisline_style("-|>")
        # adds X and Y-axis from the origin
        ax.axis[direction].set_visible(True)

      for direction in ["left", "right", "bottom", "top"]:
        # hides borders
        ax.axis[direction].set_visible(False)

      # Grafico de la función
      ax.plot(x,y,color='black')

      # Grafico el polinomio de Taylor
      n=int(np.floor(frame/Mult))
      x_T=np.linspace(*intervalo_x_graf,Res_EjeX)
      y_T=np.zeros(Res_EjeX)
      for i in range(Res_EjeX):
          y_T[i]=Taylor(x_T[i],n)
      ax.plot(x_T,y_T,color='red')

      ax.text(intervalo_x_fig[0],intervalo_y_fig[1],f'$n = {n}$', fontsize=Tam_fuentes, color='black',horizontalalignment='left',verticalalignment='center')

    ani=FuncAnimation(fig, update, frames=np.linspace(N_base*Mult,N_base*Mult+N_add*Mult,Mult*N_add), blit=False, repeat=False)
  else:
    # Redeclaro los ejes
    ax.set_xlim(*intervalo_x_fig)
    ax.set_ylim(*intervalo_y_fig)

    for direction in ["xzero", "yzero"]:
      # adds arrows at the ends of each axis
      ax.axis[direction].set_axisline_style("-|>")
      # adds X and Y-axis from the origin
      ax.axis[direction].set_visible(True)

    for direction in ["left", "right", "bottom", "top"]:
      # hides borders
      ax.axis[direction].set_visible(False)

    # Grafico de la función
    ax.plot(x,y,color='black')

    # Grafico el polinomio de Taylor
    x_T=np.linspace(*intervalo_x_graf,Res_EjeX)
    y_T=np.zeros(Res_EjeX)
    for i in range(Res_EjeX):
        y_T[i]=Taylor(x_T[i],N_Max)
    ax.plot(x_T,y_T,color='red')

    ax.text(intervalo_x_fig[0],intervalo_y_fig[1],f'$n = {N_Max}$', fontsize=Tam_fuentes, color='black',horizontalalignment='left',verticalalignment='center')

  #! Guardar grafico
  if Guardar_grafico:
    if Animado:
      # Verifico si existe la carpeta videos, si no la creo
      carpeta=Path('./videos/')
      if not carpeta.exists():
        carpeta.mkdir()

      # Obtener el nombre del archivo actual sin la extension
      Nombre = Path(__file__).stem

      # Creo el nombre del archivo
      archivo=f'{carpeta}/{Nombre}_{2*N_base}_{N_Max}.mp4'

      # Guardar la animación
      Writer = animation.writers['ffmpeg']
      writer = Writer(fps=30, bitrate=1800)
      ani.save(archivo, writer=writer)
    else:
      # Verifico si existe la carpeta imagenes, si no la creo
      carpeta=Path('./imagenes/')
      if not carpeta.exists():
        carpeta.mkdir()

      # Obtener el nombre del archivo actual sin la extension
      Nombre = Path(__file__).stem

      # Creo el nombre del archivo
      archivo=f'{carpeta}/{Nombre}_n{N_Max}.png'

      # Guardar la imagen
      plt.savefig(archivo,transparent=Fondo_transparente)

  #! Mostrar grafico
  if Mostrar_grafico:
    plt.show()


if __name__ == "__main__":
  main()