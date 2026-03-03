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
  a, b = 1, 9   # Intervalo en x
  c, d = 1, 7   # Intervalo en y
  m, n = 6, 6   # Divisiones en x y y

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
  ax.set_xticks(np.append(np.arange(a, b, dx), b))
  ax.set_yticks(np.append(np.arange(c, d, dy), d))
  ax.set_xticklabels(['$x_0$', '$x_1$', '$x_2$', '$x_{i-1}$', '$x_{i}$', '$x_{m-1}$', '$x_m$'])
  ax.set_yticklabels(['$y_0$', '$y_1$', '$y_2$', '$y_{j-1}$', '$y_{j}$', '$y_{n-1}$', '$y_n$'])
  # ax.set_xticklabels([str(i) for i in range(x_lim[0], x_lim[1]+1)])
  # ax.set_yticklabels([str(i) for i in range(y_lim[0], y_lim[1]+1)])
  # ax.set_title(f'Dominio de suma de Riemann bidimensional\n({m} divisiones en x, {n} en y)')
  ax.set_aspect('equal')
  # plt.grid(True, which='both', linestyle='--', alpha=0.3)

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
      if i == m-2 or j == n-2 or i==2 or j==2:
        rect = Rectangle((x0, y0), dx, dy, edgecolor='k', facecolor='none', lw=1, linestyle=':')
        if i == m-2 and j == n-2:
          ax.text(x0 + dx/2, y0 + dy/2, ' ', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif i == m-2 and j == 2:
          ax.text(x0 + dx/2, y0 + dy/2, ' ', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif i == 2 and j == n-2:
          ax.text(x0 + dx/2, y0 + dy/2, ' ', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif j == 2 and i == 2:
          ax.text(x0 + dx/2, y0 + dy/2, ' ', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif i == m-2:
          ax.text(x0 + dx/2, y0 + dy/2, '$\cdots$', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif i == 2:
          ax.text(x0 + dx/2, y0 + dy/2, '$\cdots$', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif j == n-2:
          ax.text(x0 + dx/2, y0 + dy/2, '$\\vdots$', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif j == 2:
          ax.text(x0 + dx/2, y0 + dy/2, '$\\vdots$', ha='center', va='center', fontsize=tam_fuentes*0.8)
      else:
        rect = Rectangle((x0, y0), dx, dy, edgecolor='k', facecolor='none', lw=1)
        cx = x0 + dx/2
        cy = y0 + dy/2
        if i == m-1 and j == n-1:
          ax.text(cx, cy, '$R_{mn}$', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif i == m-3 and j == n-3:
          ax.text(cx, cy, '$R_{ij}$', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif i == m-1 and j == n-3:
          ax.text(cx, cy, '$R_{m j}$', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif i == m-3 and j == n-1:
          ax.text(cx, cy, '$R_{i n}$', ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif i == m-3:
          ax.text(cx, cy, '$R_{i%d}$' % (j+1), ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif j == n-3:
          ax.text(cx, cy, '$R_{%dj}$' % (i+1), ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif i == m-1:
          ax.text(cx, cy, '$R_{m%d}$' % (j+1), ha='center', va='center', fontsize=tam_fuentes*0.8)
        elif j == n-1:
          ax.text(cx, cy, '$R_{%dn}$' % (i+1), ha='center', va='center', fontsize=tam_fuentes*0.8)
        else:
          ax.text(cx, cy, '$R_{%d%d}$' % (i+1, j+1), ha='center', va='center', fontsize=tam_fuentes*0.8)
      ax.add_patch(rect)
  #* puntos suspensivos en los ejes
  ax.text(a+2.5*dx-0.1, -0.3, '$\cdots$', ha='center', va='center', fontsize=tam_fuentes*0.8)
  ax.text(a+4.5*dx-0.1, -0.3, '$\cdots$', ha='center', va='center', fontsize=tam_fuentes*0.8)
  ax.text(-0.3, c+2.5*dy-0.1, '$\\vdots$', ha='center', va='center', fontsize=tam_fuentes*0.8)
  ax.text(-0.3, c+4.5*dy-0.1, '$\\vdots$', ha='center', va='center', fontsize=tam_fuentes*0.8)

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