import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#! Ejecutar con: streamlit run Sucesiones_Representacion_1D.py

#* Etiqueta de la sucesión en formato LaTeX para mostrar en el gráfico
latex_tag_funcion=r'$a_n = (-1)^n\left(0.1+\dfrac{1}{n}\right)$'

#* Función que define la sucesión a representar
@np.vectorize
def func_a(x: int):
    return ((-1)**x)*(0.1+1/x)

#* Función para dibujar la sucesión
def Draw_Sucesion_1D(n , intervalo_x = [0,1], intervalo_y = [-1,1],solo_ultimo = False, Plot_dark = True, ocultar_etiquetas = False, tam_fuentes = 12):
    indices_suc= np.arange(1,n+1)
    if solo_ultimo:
        sucesion = func_a(n)
    else:
        sucesion = func_a(indices_suc)

    #! iniciar figura
    fig , ax = plt.subplots(figsize=(10,1))

    aux1=min(intervalo_x[0], np.min(sucesion))
    aux2=max(intervalo_x[1], np.max(sucesion))
    dif = aux2-aux1
    ax.set_xlim(aux1-0.05*dif,aux2+0.05*dif)
    ax.set_ylim(*intervalo_y)

    #* dibujar ejes coordenados
    ax.spines[["bottom"]].set_position(("data", 0))
    ax.spines[["left", "top", "right"]].set_visible(False)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color = 'white' if Plot_dark else 'black')

    #* Graficar la función
    ax.scatter(sucesion,np.zeros_like(sucesion) , color='cyan' if Plot_dark else 'blue', s=30)

    #* etiquetas de los puntos
    if not ocultar_etiquetas:
        if solo_ultimo:
            ax.text(sucesion, 0.25 , f'$a_{{{n}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
        else:
            for i in range(n):
                ax.text(sucesion[i], 0.25 , f'$a_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')

    #* etiquetas de los valores en los ejes
    etiquetas_x = np.arange(aux1, aux2+0.1*(aux2-aux1), 0.1*(aux2-aux1))
    ax.set_xticks(etiquetas_x)
    ax.set_yticks([])

    #* tamaño de fuentes en los ejes
    ax.tick_params(axis='both', which='major', labelsize=tam_fuentes)

    return fig ,ax

def main():
    #! parametros para grafico
    Full_Latex = True
    Plot_dark = True

    tam_fuentes=12

    #* intervalos x e y
    intervalo_x = [-1.5, 1.5]

    #* cantidad numero de elementos de la sucesion
    n=3

    if Full_Latex:
        plt.rcParams.update({
        "text.usetex": True,
        "font.size": tam_fuentes
        })

    #! Configuración de la página de Streamlit
    st.set_page_config(page_title="Visualización 1D de una sucesión", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')#, menu_items={'Get Help': 'https://www.extremelycoolapp.com/help','Report a bug': "https://www.extremelycoolapp.com/bug",'About': "# This is a header. This is an *extremely* cool app!"})

    #! Titulo
    st.title('Visualización 1D de una sucesión')

    #! Checkboxes para opciones de visualización
    n = st.sidebar.number_input('indique el valor de $n$', min_value=1, value=n, step=1)
    ocultar_etiquetas = st.sidebar.toggle('Ocultar etiquetas sucesión', value=False)
    solo_ultimo = st.sidebar.toggle('Mostrar solo el término actual', value=False)
    Plot_dark = st.sidebar.toggle(label='Gráfico modo oscuro', value=True, key='toggle_dark_mode')
    if Plot_dark:
        plt.style.use('dark_background')
        if Full_Latex:
            plt.rcParams.update({
                "text.usetex": True,
                "font.size": tam_fuentes
            })
    else:
        plt.style.use('default')
        if Full_Latex:
            plt.rcParams.update({
                "text.usetex": True,
                "font.size": tam_fuentes
            })

    #! Generar gráfico con spinner
    with st.spinner('Generando gráfico...'):
        fig , _ = Draw_Sucesion_1D(n , intervalo_x, solo_ultimo=solo_ultimo, Plot_dark=Plot_dark, ocultar_etiquetas=ocultar_etiquetas, tam_fuentes=tam_fuentes)
        st.pyplot(fig)
        st.markdown(f'Gráfico sucesión: {latex_tag_funcion}')

if __name__ == "__main__":
    main()