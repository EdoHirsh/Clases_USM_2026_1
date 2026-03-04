import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#! definicion función que define la sucesión
def func_a(x: float):
  return 1-1/x

def func_b(x: float):
  return 1+np.sin(x)/x

def func_c(x: float):
  return 1+1/x

def main():
  #! parametros para grafico
  Full_Latex = True
  Mostrar_ejes = True
  Ejes_clasicos = True
  Malla_de_fondo = False
  Guardar_grafico = False
  Fondo_transparente = True
  Mostrar_grafico = True
  Dark_mode = True

  #* tamaaño de fuentes
  tam_fuentes = 16

  #* cantidad de puntos en la sucesion
  n=10

  #* intervalos x e y
  intervalo_x = [-0.5,10.5]
  intervalo_y = [-0.125,2.125]

  #* numeros de 1 a n
  indices_suc= np.arange(1,n+1)

  #* Activar el modo oscuro
  if Dark_mode:
    plt.style.use('dark_background')
  else:
    plt.style.use('default')

  #* Activar el uso de LaTeX en las etiquetas
  if Full_Latex:
    plt.rcParams.update({
      "text.usetex": True,
      "font.size": tam_fuentes
    })

  #! iniciar figura
  _ , ax = plt.subplots(figsize=(10,5))
  ax.set_xlim(*intervalo_x)
  ax.set_ylim(*intervalo_y)

  #* dibujar ejes coordenados
  if Mostrar_ejes & Ejes_clasicos:
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color = 'white' if Dark_mode else 'black')
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color = 'white' if Dark_mode else 'black')
  elif not Mostrar_ejes:
    ax.set_axis_off()

  #! Graficar las sucesiones
  sucesion_a = func_a(indices_suc)
  sucesion_b = func_b(indices_suc)
  sucesion_c = func_c(indices_suc)
  ax.scatter(indices_suc, sucesion_a, color='white' if Dark_mode else 'black', s=10)
  ax.scatter(indices_suc, sucesion_b, color='white' if Dark_mode else 'black', s=10)
  ax.scatter(indices_suc, sucesion_c, color='white' if Dark_mode else 'black', s=10)
  #* grafico de las versiones continuas de las sucesiones
  x_continuo = np.linspace(1, 10, 1000)
  ax.plot(x_continuo, func_a(x_continuo), color='cyan' if Dark_mode else 'blue',linestyle=':')
  ax.plot(x_continuo, func_b(x_continuo), color='magenta' if Dark_mode else 'red', linestyle=':')
  ax.plot(x_continuo, func_c(x_continuo), color='darkturquoise' if Dark_mode else 'lightblue', linestyle=':')
  

  #* etiquetas de los puntos
  for i in range(n):
    ax.text(indices_suc[i]+0.05, sucesion_a[i]+0.02, f'$a_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
    ax.text(indices_suc[i]+0.05, sucesion_b[i]+0.02, f'$b_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
    ax.text(indices_suc[i]+0.05, sucesion_c[i]+0.02, f'$c_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
  #* puntos suspensivos al final
  ax.text(indices_suc[-1]+0.3, sucesion_a[-1]-0.01, '$\ldots$', fontsize=tam_fuentes, ha='center', va='bottom')

  #* etiquetas de los valores en los ejes
  ax.set_xticks(indices_suc)
  ax.set_yticks(np.arange(0,2.2,0.2))

  #* tamaño de fuentes en los ejes
  ax.tick_params(axis='both', which='major', labelsize=tam_fuentes)

  #* dibujar mallado
  if Malla_de_fondo:
    ax.grid(True, which='both', linestyle='--', lw=0.5)

  #! guardar grafico
  if Guardar_grafico:
    #* Verificar si la carpeta imagenes existe, si no, crearla
    carpeta = Path('./imagenes/')
    if not carpeta.exists():
      carpeta.mkdir()

    #* Obtener el nombre del archivo actual sin la extension
    Nombre = Path(__file__).stem

    #* Nombre del archivo
    archivo = f'{carpeta}/{Nombre}.png'

    #* Guardar la figura
    plt.savefig(archivo, dpi=600, transparent=Fondo_transparente)

  #! Mostrar grafico
  if Mostrar_grafico:
    plt.show()

if __name__ == "__main__":
  main()