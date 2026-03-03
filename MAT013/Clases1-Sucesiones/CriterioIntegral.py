import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

def func_f(x: float):
  return 1/x

def main():
  #! parametros para grafico
  Full_Latex = True
  Mostrar_ejes = True
  Ejes_clasicos = True
  Guardar_grafico = False
  Fondo_transparente = False
  Mostrar_grafico = True
  SumaSuperior = True
  SumaInferior = True
  Tam_fuentes=16

  # intervalos x e y
  intervalo_x_vent = [-0.5,10.5]
  intervalo_y_vent = [-0.075,1.075]
  intervalo_x_graf = [0,10.5]
  # intervalo_y_graf = [0,10.5]

  # cantidad numero de elementos de la sucesion
  n=10

  # puntos en el dominio para la sucesion
  PuntosSubintervalos=np.arange(1,n+1,1)
  print(PuntosSubintervalos)

  # cantidad de puntos en el intervalo
  N=100

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
  _ , ax = plt.subplots(figsize=(tam_x,tam_y))
  ax.set_xlim(*intervalo_x_vent)
  ax.set_ylim(*intervalo_y_vent)
  # ax.set_aspect('equal')

  # Elegir las etiquetas de los ejes
  ax.set_yticks([])
  ax.set_yticklabels([])
  ax.set_xticks(PuntosSubintervalos)
  ax.set_xticklabels(PuntosSubintervalos)

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
  y = func_f(x)
  ax.plot(x, y, color='black')
  # ax.text(intervalo_x[0],1.1*intervalo_y[1],f'  n = {n}', fontsize=12, color='black',horizontalalignment='left',verticalalignment='center')

  # Graficar los rectangulos izquierda
  if SumaSuperior:
    for i in range(n-1):
      ax.plot([PuntosSubintervalos[i],PuntosSubintervalos[i+1],PuntosSubintervalos[i+1],PuntosSubintervalos[i],PuntosSubintervalos[i]],[0,0,func_f(PuntosSubintervalos[i]),func_f(PuntosSubintervalos[i]),0],color='blue')
      ax.fill_between([PuntosSubintervalos[i],PuntosSubintervalos[i+1]],[func_f(PuntosSubintervalos[i]),func_f(PuntosSubintervalos[i])],color='lightblue')

  # Graficar los rectangulos derecha
  if SumaInferior:
    for i in range(n-1):
      ax.plot([PuntosSubintervalos[i],PuntosSubintervalos[i+1],PuntosSubintervalos[i+1],PuntosSubintervalos[i],PuntosSubintervalos[i]],[0,0,func_f(PuntosSubintervalos[i+1]),func_f(PuntosSubintervalos[i+1]),0],color='brown')
      ax.fill_between([PuntosSubintervalos[i],PuntosSubintervalos[i+1]],[func_f(PuntosSubintervalos[i+1]),func_f(PuntosSubintervalos[i+1])],color='orange')

  # ax.plot([intervalo_x[0],intervalo_x[0]],[0,f(intervalo_x[0])],color='black',linestyle='--')
  # ax.plot([intervalo_x[1],intervalo_x[1]],[0,f(intervalo_x[1])],color='black',linestyle='--')

  #! guardar grafico
  if Guardar_grafico:
    # Verificar si la carpeta imagenes existe, si no, crearla
    carpeta = Path('./imagenes/')
    if not carpeta.exists():
      carpeta.mkdir()

    # Obtener el nombre del archivo actual sin la extension
    Nombre = Path(__file__).stem
    lado=('_Sup' if SumaSuperior else '')+('_Inf' if SumaInferior else '')

    # Nombre del archivo
    archivo = f'{carpeta}/{Nombre}{lado}.png'

    # Guardar la figura
    plt.savefig(archivo, dpi=600, transparent=Fondo_transparente)

  #! Mostrar grafico
  if Mostrar_grafico:
    plt.show()

if __name__ == "__main__":
  main()