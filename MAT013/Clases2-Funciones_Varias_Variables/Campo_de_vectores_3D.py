import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#funncion coordenada x del campo vectorial
def fx(x,y,z):
  return x

#funncion coordenada y del campo vectorial
def fy(x,y,z):
  return y

#funncion coordenada z del campo vectorial
def fz(x,y,z):
  return z

def main():
  # limites de los ejes x,y,z
  x_lim = [-2,2]
  y_lim = [-2,2]
  z_lim = [-2,2]

  # numero de puntos en los ejes x,y,z
  n_x = 5
  n_y = 5
  n_z = 5


  # coordenadas de los puntos del campo vectorial
  x = np.linspace(*x_lim,n_x)
  y = np.linspace(*y_lim,n_y)
  z = np.linspace(*z_lim,n_z)

  # mesh de coordenadas de los puntos del campo vectorial
  X,Y,Z=np.meshgrid(x,y,z)

  #coordenadas de los vectores del campo vectorial
  U = fx(X,Y,Z)
  V = fy(X,Y,Z)
  W = fz(X,Y,Z)

  # grafico campo vectorial 3D
  fig , ax = plt.subplots(subplot_kw={'projection':'3d'})

  ax.quiver(X,Y,Z,U,V,W,cmap='gnuplot',length=0.5,normalize=True)#,cmap='gnuplot',vmin=np.min(np.sqrt(U**2+V**2+W**2)),vmax=np.max(np.sqrt(U**2+V**2+W**2)))
  ax.set_zticks([-2,-1,0,1,2])

  # guardar imagen
  carpeta = Path('./imagenes/')
  if not carpeta.exists():
    Path(carpeta).mkdir()
  
  archivo = f'{carpeta}/Campo_de_vectores_3D.png'
  fig.savefig(archivo, dpi=300, transparent=True)

  # mostrar grafico
  plt.show()

if __name__ == "__main__":
  main()