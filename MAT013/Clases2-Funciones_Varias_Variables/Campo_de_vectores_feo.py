import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#* Definir las funciones de campo vectorial
# X= -x/(x^2+y^2)
# Y= -y/(x^2+y^2)
# es un caso malo que justifica normalizar y usar colores
def X_func(x,y):
  r=-x/(x**2+y**2)
  return r

def Y_func(x,y):
  r=-y/(x**2+y**2)
  return r

def main():
  x_lim = [-5,5]
  y_lim = [-5,5]
  N=20
  p_x=(x_lim[1]-x_lim[0])/N
  p_y=(y_lim[1]-y_lim[0])/N

  # rangos x e y
  x = np.arange(*x_lim,p_x)
  y = np.arange(*y_lim,p_y)
  
  # # mostrar los valores de x e y
  # print(f'x={x}')
  # print(f'y={y}')

  # Meshgrid plano
  X,Y = np.meshgrid(x,y)
  
  # grids de coordenadas de los vectores
  Ex = X_func(X,Y)
  Ey = Y_func(X,Y)

  # Plot vector field
  fig=plt.figure()
  plt.quiver(x, y, Ex, Ey, color='b')
  plt.axis([*x_lim,*y_lim])
  plt.xlabel('x')
  plt.ylabel('y')
  # plt.grid()

  # Mostar la figura
  plt.show()

  # Guardar la figura
  carpeta=Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  archivo = f'{carpeta}/Campo_de_Vectores_feo.png'

  fig.savefig(archivo, dpi=300, transparent=True)

if __name__=='__main__':
  main()