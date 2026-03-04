import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path

#! Ejecutar con: streamlit run Series_Criterio_Integral.py

def func_f(x: float):
  return 1/x

def Draw_Criterio(n ,N, PuntosSubintervalos, intervalo_x_vent = [-0.5,10.5], intervalo_y_vent = [-0.075,1.075], intervalo_x_graf = [0,10.5], Mostrar_ejes = True, Ejes_clasicos = True, SumaSuperior = True, SumaInferior = True, mostrar_funcion = True):
  #! iniciar figura
  fig , ax = plt.subplots(figsize=(20,10))
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

  #* Graficar la función
  x = np.linspace(intervalo_x_graf[0],intervalo_x_graf[1], N)
  y = func_f(x)
  if mostrar_funcion:
    ax.plot(x, y, color='blue')

  #* Graficar los rectangulos izquierda
  if SumaSuperior:
    for i in range(n-1):
      ax.plot([PuntosSubintervalos[i],PuntosSubintervalos[i+1],PuntosSubintervalos[i+1],PuntosSubintervalos[i],PuntosSubintervalos[i]],[0,0,func_f(PuntosSubintervalos[i]),func_f(PuntosSubintervalos[i]),0],color='blue')
      ax.fill_between([PuntosSubintervalos[i],PuntosSubintervalos[i+1]],[func_f(PuntosSubintervalos[i]),func_f(PuntosSubintervalos[i])],color='lightblue')

  #* Graficar los rectangulos derecha
  if SumaInferior:
    for i in range(n-1):
      ax.plot([PuntosSubintervalos[i],PuntosSubintervalos[i+1],PuntosSubintervalos[i+1],PuntosSubintervalos[i],PuntosSubintervalos[i]],[0,0,func_f(PuntosSubintervalos[i+1]),func_f(PuntosSubintervalos[i+1]),0],color='brown')
      ax.fill_between([PuntosSubintervalos[i],PuntosSubintervalos[i+1]],[func_f(PuntosSubintervalos[i+1]),func_f(PuntosSubintervalos[i+1])],color='orange')

  return fig


def main():
  #! parametros para grafico
  Full_Latex = True
  Plot_dark = True
  Mostrar_ejes = True
  Ejes_clasicos = True
  Fondo_transparente = False
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

  # cantidad de puntos en el intervalo
  N=100

  if Full_Latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
      "font.size": Tam_fuentes
    })

  #! Configuración de la página de Streamlit
  st.set_page_config(page_title="Criterio de la integral", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')#, menu_items={'Get Help': 'https://www.extremelycoolapp.com/help','Report a bug': "https://www.extremelycoolapp.com/bug",'About': "# This is a header. This is an *extremely* cool app!"})

  #! Titulo
  st.title('Visualización criterio de la integral')

  #! Checkboxes para opciones de visualización
  mostrar_funcion = st.sidebar.checkbox('Mostrar función', value=True)
  SumaSuperior = st.sidebar.checkbox('Mostrar suma superior', value=True)
  SumaInferior = st.sidebar.checkbox('Mostrar suma inferior', value=True)
  Plot_dark = st.sidebar.checkbox('Tema oscuro en el gráfico', value=Plot_dark)
  # Plot_dark = st.toggle(label='gráfico modo oscuro', value=True, key='toggle_dark_mode')
  if Plot_dark:
    plt.style.use('dark_background')
  else:
    plt.style.use('default')

  #! Generar gráfico con spinner
  with st.spinner('Generando gráfico...'):
    fig = Draw_Criterio(n ,N, PuntosSubintervalos, intervalo_x_vent, intervalo_y_vent,intervalo_x_graf, Mostrar_ejes, Ejes_clasicos, SumaSuperior, SumaInferior, mostrar_funcion)
    st.pyplot(fig)

if __name__ == "__main__":
  main()