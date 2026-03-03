import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

def func_f(x: float):
  return 4-(x-3)**2/2+1

def func_g(x):
  return np.cos(4*x/(np.pi))/2+1

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

  #* intervalos del grafico
  intervalo_x_graf = [-0.5,5.5]
  intervalo_y_graf = [-0.5,5.5]

  #* intervalo del dominio
  intervalo_x = [1,5]

  #! Crear los ejes
  _ , ax = plt.subplots(figsize=(5,5))
  ax.set_xlim(*intervalo_x_graf)
  ax.set_ylim(*intervalo_y_graf)
  ax.set_aspect('equal')
  ax.set_xticks([1,5],['$a$', '$b$'], fontsize=tam_fuentes)
  ax.set_yticks([])

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
  x = np.linspace(intervalo_x[0],intervalo_x[1], 100)
  y1 = func_f(x)
  y2 = func_g(x)
  ax.plot(x, y1, color='black')
  ax.plot(x, y2, color='black')
  ax.fill_between(x, y1, y2, color='lightblue')

  #* etiquetas de las funciones
  ax.text(3, 0.25, f'$\psi_1(x)$', fontsize=tam_fuentes, color='black')
  ax.text(3, 5.25, f'$\psi_2(x)$', fontsize=tam_fuentes, color='black')

  #* Limites del intervalo
  ax.plot([intervalo_x[0],intervalo_x[0]],[np.min([func_f(intervalo_x[0]),func_g(intervalo_x[0])]),np.max([func_f(intervalo_x[0]),func_g(intervalo_x[0])])],color='black',linestyle='-')
  ax.plot([intervalo_x[0],intervalo_x[0]],[0,np.min([func_f(intervalo_x[0]),func_g(intervalo_x[0])])],color='black',linestyle='--')
  ax.plot([intervalo_x[1],intervalo_x[1]],[np.min([func_f(intervalo_x[1]),func_g(intervalo_x[1])]),np.max([func_f(intervalo_x[1]),func_g(intervalo_x[1])])],color='black',linestyle='-')
  ax.plot([intervalo_x[1],intervalo_x[1]],[0,np.min([func_f(intervalo_x[1]),func_g(intervalo_x[1])])],color='black',linestyle='--')


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