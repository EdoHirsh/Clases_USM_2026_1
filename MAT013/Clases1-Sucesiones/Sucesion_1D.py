import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#! funcion a graficar
def func_f(x: float):
  # return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2)
  return 1/x

def main():
  #! parametros para grafico
  Full_Latex = True
  Mostrar_ejes = True
  Ejes_clasicos = True
  Malla_de_fondo = False
  Guardar_grafico = False
  Fondo_transparente = False
  Mostrar_grafico = True

  # tamaaño de fuentes
  tam_fuentes = 16
  # cantidad de puntos en la sucesion
  n=6

  # intervalos x e y
  intervalo_x = [-0.05,1.05]
  intervalo_y = [-0.125,0.125]

  # numeros de 1 a n
  indices_suc= np.arange(1,n+1)

  if Full_Latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
    })

  # tamaño de la figura
  # tam_x = 2*(intervalo_x[1]-intervalo_x[0])
  # tam_y = 10*(intervalo_y[1]-intervalo_y[0])
  tam_x = 12
  tam_y = 1

  #! iniciar figura
  _ , ax = plt.subplots(figsize=(tam_x,tam_y))
  ax.set_xlim(*intervalo_x)
  ax.set_ylim(*intervalo_y)
  # ax.set_aspect('equal')

  #* dibujar ejes coordenados
  if Mostrar_ejes & Ejes_clasicos:
    # mover bordes izquierdo e inferior a x = 0 and y = 0, respectivamente
    ax.spines[["bottom"]].set_position(("data", 0))
    # esconder los bordes superior y derecho
    ax.spines[["left", "top", "right"]].set_visible(False)
    # dibujar las flechas de los ejes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    # ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  elif not Mostrar_ejes:
    ax.set_axis_off()

  # Graficar la función
  sucesion = 1/indices_suc
  ax.scatter(sucesion,np.zeros_like(sucesion) , color='black', s=30)

  # etiquetas de los puntos
  for i in range(n):
    ax.text(sucesion[i], 0.025 , f'$a_{i+1}$', fontsize=tam_fuentes, ha='center', va='bottom')
  # puntos suspensivos al final
  ax.text(0.1, 0.02 , '$\ldots$', fontsize=tam_fuentes, ha='center', va='bottom')

  # etiquetas de los valores en los ejes
  ax.set_xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
  ax.set_yticks([])

  # tamaño de fuentes en los ejes
  ax.tick_params(axis='both', which='major', labelsize=12)

  # dibujar mallado
  if Malla_de_fondo:
    ax.grid(True, which='both', linestyle='--', lw=0.5)

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