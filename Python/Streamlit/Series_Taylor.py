import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path

#! Ejecutar con: streamlit run Series_Taylor.py

tam_fuentes=12

def func_f(x) -> float:
  return np.exp(x)

def Taylor(x: float,n: int) -> float:
  return np.sum([(x**i)/scp.special.factorial(i) for i in range(n+1)])

def Draw_Taylor(n, intervalo_x=[-10,10], intervalo_y=[-2,2], intervalo_x_graf=[-10.1,10.1], intervalo_y_graf=[-2.1,2.1], Plot_dark=False):
  Res_EjeX=1000
  N_Max=n

  fig = plt.figure(figsize=(20,10))
  ax = fig.add_subplot(1, 1, 1)
  ax.set_xlim(*intervalo_x_graf)
  ax.set_ylim(*intervalo_y_graf)

  x=np.linspace(*intervalo_x,Res_EjeX)
  y=func_f(x)

  #* dibujar ejes coordenados
  ax.spines[["left", "bottom"]].set_position(("data", 0))
  ax.spines[["top", "right"]].set_visible(False)
  ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color = 'white' if Plot_dark else 'black')
  ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color = 'white' if Plot_dark else 'black')
  ax.set_xlabel(f'$x$', fontsize=tam_fuentes,loc='right')
  ax.set_ylabel(f'$y$', fontsize=tam_fuentes,loc='top',rotation='horizontal')

  # Grafico de la función
  ax.plot(x,y,color='blue')

  # Grafico el polinomio de Taylor
  x_T = np.linspace(*intervalo_x,Res_EjeX)
  y_T = np.zeros(Res_EjeX)
  for i in range(Res_EjeX):
      y_T[i]=Taylor(x_T[i],N_Max)
  ax.plot(x_T,y_T,color='red')

  ax.text(intervalo_x_graf[0],intervalo_y_graf[1],f'$n = {N_Max}$', fontsize=tam_fuentes, color= 'white' if Plot_dark else 'black',horizontalalignment='left',verticalalignment='center')

  return fig

def main():
  #! parametros para grafico
  Full_Latex = True
  Plot_dark = False
  Fondo_transparente = False

  # intervalos x e y
  intervalo_x = [0,6]
  intervalo_y = [0,1]

  # cantidad numero de elementos de la sucesion
  n=6

  if Full_Latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
      "font.size": tam_fuentes
    })

  #! Configuración de la página de Streamlit
  st.set_page_config(page_title="Serie de Taylor de la función $e^x$", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')#, menu_items={'Get Help': 'https://www.extremelycoolapp.com/help','Report a bug': "https://www.extremelycoolapp.com/bug",'About': "# This is a header. This is an *extremely* cool app!"})

  #! Titulo
  st.title('Serie de Taylor de la función $e^x$')

  #! Checkboxes para opciones de visualización
  # n = st.sidebar.slider('indique el valor de $n$', 1, 100, 6, 1)
  n = st.sidebar.number_input('indique el valor de $n$', min_value=0, value=n, step=1)
  Plot_dark = st.sidebar.toggle(label='Gráfico modo oscuro', value=Plot_dark)
  if Plot_dark:
    plt.style.use('dark_background')
    if Full_Latex:
      plt.rcParams.update({
        "text.usetex": True,
        # "font.family": "Helvetica"
        "font.size": tam_fuentes
      })
  else:
    plt.style.use('default')
    if Full_Latex:
      plt.rcParams.update({
        "text.usetex": True,
        # "font.family": "Helvetica"
        "font.size": tam_fuentes
      })

  #! Generar gráfico con spinner
  with st.spinner('Generando gráfico...'):
    fig = Draw_Taylor(n, Plot_dark=Plot_dark)
    st.pyplot(fig)

if __name__ == "__main__":
  main()