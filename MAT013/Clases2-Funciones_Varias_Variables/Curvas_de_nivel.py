import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

def func_f(x,y):
  return np.sqrt(x**2+y**2)
  # return x*y

def main():
  # parametros de la figura
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

  # Definir los intervalos para x e y
  intervalo_x = [-5,5]
  intervalo_y = [-5,5]

  # proporcion de la figura
  prop=(intervalo_x[1]-intervalo_x[0])/(intervalo_y[1]-intervalo_y[0])

  # Numero de subdivisiones
  N=1000

  # margen para los ejes del grafico
  pbuff=0.2

  # intervalos con margen
  intervalo_x_buff=[intervalo_x[0]-pbuff,intervalo_x[1]+pbuff]
  intervalo_y_buff=[intervalo_y[0]-pbuff,intervalo_y[1]+pbuff]


  # niveles de las curvas de nivel
  Zlevels=[1,2,3,4,5]

  # X, Y para el grafico 3D
  XPoints = np.linspace(*intervalo_x,N)
  YPoints = np.linspace(*intervalo_y,N)

  # crear mallas para x e y
  xmesh,ymesh=np.meshgrid(XPoints, YPoints)
  zmesh=func_f(xmesh,ymesh)

  # empezar a graficar
  _ = plt.figure(figsize=(5*prop,5))

  # establecer limites de los ejes
  plt.axis([*intervalo_x_buff,*intervalo_y_buff])

  # Etiquetas de los ejes
  plt.xlabel('$x$')
  plt.ylabel('$y$')

  # graficar las curvas de nivel
  contours = plt.contour(xmesh,ymesh,zmesh,cmap='gnuplot',vmin=0,vmax=5, levels=Zlevels)


  # etiquetas de las curvas de nivel
  # plt.clabel(contours,inline=1,fontsize=10)
  # plt.clabel(contours,inline=1,fontsize=10,fmt='%1.1f')
  # plt.clabel(contours,inline=1,fontsize=10,manual=[(0,1),(0,2),(0,3),(0,4),(0,5)])
  plt.clabel(contours,inline=1,fontsize=10,manual=[(1/np.sqrt(2),1/np.sqrt(2)),(2/np.sqrt(2),2/np.sqrt(2)),(3/np.sqrt(2),3/np.sqrt(2)),(4/np.sqrt(2),4/np.sqrt(2)),(5/np.sqrt(2),5/np.sqrt(2))])

  # Verificar si la carpeta imagenes existe, si no, crearla
  carpeta = Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  # Obtener el nombre del archivo actual sin la extension
  Nombre = Path(__file__).stem

  # Nombre del archivo
  archivo = f'{carpeta}/{Nombre}.png'

  # Guardar la figura
  plt.savefig(archivo, dpi=600, transparent=True)

  # Mostrar la figura
  plt.show()

if __name__=='__main__':
  main()