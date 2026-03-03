import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from pathlib import Path

# Definir la función de dos variables
def func_f(x, y):
  return x**2 + y**2

def main():
  #! parametros para grafico
  Texto_Latex = False
  Guardar_Video = False
  Mostrar_Video = True

  # tamaaño de fuentes
  tam_fuentes = 14

  # configurar el texto en LaTeX
  if Texto_Latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
      "font.size": tam_fuentes,
    })

  #* numero de subdivisiones
  N = 20

  #* intervalos del grafico
  intervalo_x_graf = (-0.25, 5.25)
  intervalo_y_graf = (-0.25, 5.25)

  #* intervalos del dominio
  intervalo_x = (0, 5)
  intervalo_y = (0, 5)

  #* largo de los intervalos
  largo_x = intervalo_x[1] - intervalo_x[0]
  largo_y = intervalo_y[1] - intervalo_y[0]

  #! Crear la figura y el eje 3D
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  # Configurar la figura
  ax.set_xlim(intervalo_x_graf)
  ax.set_ylim(intervalo_y_graf)

  #* definir la función de actualización para la animación
  def update(n):
    ax.clear()
    dx = largo_x / n
    dy = largo_y / n
    x = np.linspace(*intervalo_x, n+1)
    y = np.linspace(*intervalo_y, n+1)
    X, Y = np.meshgrid(x, y)
    Z = func_f(X, Y)
    
    vol_aprox = 0  # Inicializar el área aproximada

    for i in range(n):
      for j in range(n):
        x0 = i * dx
        y0 = j * dy
        z0 = 0
        dz = func_f(x0 + dx, y0 + dy)  # Altura de la barra por punto final
        col = plt.cm.gnuplot((dz-np.min(Z)) / (np.max(Z)-np.min(Z)))  # Usar un mapa de colores para la altura
        ax.bar3d(x0, y0, z0, dx, dy, dz, color=col, alpha=1, shade=True)  # Agregar sombreado
        vol_aprox += dz * dx * dy  # Sumar el volumen de cada barra a la área aproximada

    # Configurar etiquetas y título
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    ax.set_title(f'Suma de Riemann de la función $f(x,y)=x^2+y^2$ ($m=n={n}$)')

    # Limpiar el texto anterior y mostrar el área aproximada debajo del gráfico
    if hasattr(update, 'text'):
      update.text.remove()
    update.text = plt.figtext(0.5, 0.01, f'Volumen aproximado: ${vol_aprox:.2f}$', ha='center', fontsize=12)

  #! Crear la animación
  ani = FuncAnimation(fig, update, frames=range(2, N+1), repeat=False)

  #! Guardar video
  carpeta = Path('./videos/')
  if Guardar_Video:
    # Verificar si la carpeta videos existe, si no, crearla
    carpeta = Path('./videos/')
    if not carpeta.exists():
      carpeta.mkdir()

    # Obtener el nombre del archivo actual sin la extension
    Nombre = Path(__file__).stem

    # Nombre del archivo
    archivo = f'{carpeta}/{Nombre}.mp4'

    # Guardar la figura
    ani.save(archivo, writer='ffmpeg')

  #! Mostrar la animacion
  if Mostrar_Video:
    plt.show()

if __name__ == "__main__":
  main()