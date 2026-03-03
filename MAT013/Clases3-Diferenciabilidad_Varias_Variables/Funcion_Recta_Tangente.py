import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#! definicion de la funcion y su derivada
def func(x: float) -> float:
  return x**2

def der_func(x: float) -> float:
  return 2*x

def main() -> None:
  #! parametros para grafico
  Mostrar_ejes = True
  Ejes_clasicos = True
  Guardar_grafico = True
  Fondo_transparente = True
  Mostrar_grafico = True
  Texto_latex = True

  # tamaaño de fuentes
  tam_fuentes = 14

  # configurar el texto en LaTeX
  if Texto_latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
      "font.size": tam_fuentes,
    })

  #* intervalos del grafico
  intervalo_x = [-0.5,2.5]
  intervalo_y = [-0.5,2.5]

  x_0: float = 0.5

  #! Crear los ejes
  _ , ax = plt.subplots(figsize=(5,5))
  ax.set_xlim(*intervalo_x)
  ax.set_ylim(*intervalo_y)
  ax.set_aspect('equal')
  ax.set_xticks([0.5,1,1.5,2])
  ax.set_yticks([0.5,1,1.5,2])

  #* dibujar ejes coordenados
  if Mostrar_ejes & Ejes_clasicos:
    # mover bordes izquierdo e inferior a x = 0 and y = 0, respectivamente
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    # esconder los bordes superior y derecho
    ax.spines[["top", "right"]].set_visible(False)
    # dibujar las flechas de los ejes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.set_xlabel(f'$x$', fontsize=tam_fuentes,loc='right')
    ax.set_ylabel(f'$y$', fontsize=tam_fuentes,loc='top',rotation='horizontal')
  elif not Ejes_clasicos:
    ax.set_xlabel(f'$x$', fontsize=tam_fuentes)
    ax.set_ylabel(f'$y$', fontsize=tam_fuentes)
  elif not Mostrar_ejes:
    ax.set_axis_off()

  #! Graficar la función
  x = np.linspace(intervalo_x[0],intervalo_x[1], 100)
  y = func(x)
  ax.plot(x, y, color='black')

  # Graficar la recta tangente
  y_recta = der_func(x_0)*(x-x_0)+func(x_0)
  ax.plot(x, y_recta, color='red')

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