import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle
from pathlib import Path

def main():
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

  # Parámetros de la región y divisiones
  a, b = 0, 6   # Intervalo en x
  c, d = 0, 4   # Intervalo en y
  m, n = 3, 2   # Divisiones en x y y

  dx = (b - a) / m
  dy = (d - c) / n

  #Parametros zona a graficar
  x_lim = (a-1.25, b+1)
  y_lim = (c-1.25, d+1)
  escala_figura = 0.6

  #! Crear los ejes
  _ , ax = plt.subplots(figsize=(*np.diff(x_lim)*escala_figura, *np.diff(y_lim)*escala_figura))
  ax.set_xlim(*x_lim)
  ax.set_ylim(*y_lim)
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  # append en vez de b+dx para evitar errores de redondeo
  ax.set_xticks(np.append(np.arange(a, b, dx), b)) 
  ax.set_yticks(np.append(np.arange(c, d, dy), d))
  ax.set_aspect('equal')
  plt.grid(True, which='both', linestyle='--', alpha=0.7)

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

  #! Graficar
  #* Dibujar los rectángulos de la suma de Riemann
  for i in range(m):
    for j in range(n):
      x0 = a + i * dx
      y0 = c + j * dy
      rect = Rectangle((x0, y0), dx, dy, edgecolor='k', facecolor='none', lw=1)
      ax.add_patch(rect)

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