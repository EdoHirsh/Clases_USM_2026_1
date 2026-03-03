import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#! funcion a graficar sus curvas de nivel
def func_f(x,y):
  return 2*x**2 + y**2
  # return x*y

def main():
  #! parametros para grafico
  Mostrar_ejes = True
  Ejes_clasicos = True
  Guardar_grafico = True
  Fondo_transparente =True
  Mostrar_grafico = True
  Full_Latex = True

  if Full_Latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
    })

  # Definir los intervalos para x e y
  intervalo_x = [-2.5,2.5]
  intervalo_y = [-2.5,2.5]

  # tamaño de la figura
  tam_x = (intervalo_x[1]-intervalo_x[0])/2
  tam_y = (intervalo_y[1]-intervalo_y[0])/2

  # Numero de subdivisiones
  N=500

  # margen para los ejes del grafico
  pbuff=0.2

  # intervalos con margen
  intervalo_x_buff=[intervalo_x[0]-pbuff,intervalo_x[1]+pbuff]
  intervalo_y_buff=[intervalo_y[0]-pbuff,intervalo_y[1]+pbuff]

  # niveles de las curvas de nivel
  Zlevels=[1,2,3,4,5]

  #! iniciar el proceso de graficar
  # X, Y para el grafico 3D
  XPoints = np.linspace(*intervalo_x,N)
  YPoints = np.linspace(*intervalo_y,N)

  # crear mallas para x e y
  xmesh,ymesh=np.meshgrid(XPoints, YPoints)
  zmesh=func_f(xmesh,ymesh)

  # empezar a graficar
  # _ , ax = plt.subplots(figsize=(tam_x,tam_y))
  _ = plt.figure(figsize=(2*tam_x,2*tam_y))
  ax = plt.axes()

  #* dibujar ejes coordenados
  if Mostrar_ejes & Ejes_clasicos:
    # mover bordes izquierdo e inferior a x = 0 and y = 0, respectivamente
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    # esconder los bordes superior y derecho
    ax.spines[["top", "right"]].set_visible(False)
    # dibujar las flechas de los ejes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.set_xlabel(f'$x$',loc='right')
    ax.set_ylabel(f'$y$',loc='top',rotation='horizontal')
  elif not Mostrar_ejes:
    ax.set_axis_off()

  # establecer limites de los ejes
  plt.axis([*intervalo_x_buff,*intervalo_y_buff])

  # Etiquetas de los ejes
  if not Ejes_clasicos:
    plt.xlabel('X')
    plt.ylabel('Y')

  # graficar las curvas de nivel
  contours = plt.contour(xmesh,ymesh,zmesh,cmap='gnuplot',vmin=0,vmax=np.max(zmesh), levels=Zlevels)


  # etiquetas de las curvas de nivel
  # plt.clabel(contours,inline=1,fontsize=10)
  # plt.clabel(contours,inline=1,fontsize=10,fmt='%1.1f')
  # plt.clabel(contours,inline=1,fontsize=10,manual=[(0,1),(0,2),(0,3),(0,4),(0,5)])
  plt.clabel(contours,inline=1,fontsize=10,manual=[(1/2,1/np.sqrt(2)),(np.sqrt(2)/2,1),(np.sqrt(3)/2,np.sqrt(3)/np.sqrt(2)),(1,2/np.sqrt(2)),(np.sqrt(5)/2,np.sqrt(5)/np.sqrt(2))])

  #! Guardar imagen
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

if __name__=='__main__':
  main()