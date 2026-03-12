import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#* función que define la sucesión a_n
def func_a(x: int):
    return (-1)**(x+1)*(1/x)

#* Función que calcula la suma de los primeros n términos de la sucesión a_n
@np.vectorize
def sum_a(x: int):
    ind = np.arange(1,x+1)
    suc =func_a(ind)
    return np.sum(suc)

#* Grafica la sucesión s_n y sus términos a_n
def Draw_Alternante(n , intervalo_x = [-0.05,1.05], intervalo_y = [-0.125,0.125],solo_ultimo = False, Plot_dark = True, ocultar_etiquetas = False, tam_fuentes = 12):
    indices_suc= np.arange(1,n+1)

    #! iniciar figura
    fig , ax = plt.subplots(figsize=(12,1))
    aux1=min(0.5,intervalo_x[0])
    aux2=max(1,intervalo_x[1])
    dif = aux2-aux1
    ax.set_xlim(aux1-0.05*dif,aux2+0.05*dif)
    ax.set_ylim(*intervalo_y)

    #* dibujar ejes coordenados
    ax.spines[["bottom"]].set_position(("data", 0))
    ax.spines[["left", "top", "right"]].set_visible(False)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color = 'white' if Plot_dark else 'black')

    #* Graficar la función
    if solo_ultimo:
        sucesion = sum_a(n)
    else:
        sucesion = sum_a(indices_suc)

    ax.scatter(sucesion,np.zeros_like(sucesion) , color='cyan' if Plot_dark else 'blue', s=30)

    #* etiquetas de los puntos
    if not ocultar_etiquetas:
        if solo_ultimo:
            ax.text(sucesion, 0.025 , f'$s_{{{n}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
        else:
            ax.plot([sucesion[-2],sucesion[-1]], [0.08, 0.08], color='cyan' if Plot_dark else 'blue')
            ax.text((sucesion[-2]+sucesion[-1])/2, 0.09 , rf'$b_{{{n}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
            for i in range(n):
                ax.text(sucesion[i], 0.025 , f'$s_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')

    #* etiquetas de los valores en los ejes
    # etiquetas_x = np.arange(aux1, aux2+0.1*(aux2-aux1), 0.1*(aux2-aux1))
    # ax.set_xticks(etiquetas_x)
    ax.set_xticks([])
    ax.set_yticks([])

    #* tamaño de fuentes en los ejes
    ax.tick_params(axis='both', which='major', labelsize=tam_fuentes)

    return ax, fig

def main():
    #! parametros para grafico
    Full_Latex = True
    Guardar_grafico = True
    Fondo_transparente = True
    Mostrar_grafico = True
    Dark_mode = False

    #* tamaaño de fuentes
    tam_fuentes = 16

    #* cantidad de puntos en la sucesion
    n=6

    #* intervalos x e y
    intervalo_x = [0.5,1]

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

    #! Generar gráfico
    _ , fig = Draw_Alternante(n, intervalo_x, Plot_dark=Dark_mode, tam_fuentes=tam_fuentes)

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
        fig.savefig(archivo, dpi=600, transparent=Fondo_transparente)

    #! Mostrar grafico
    if Mostrar_grafico:
        plt.show()

if __name__ == "__main__":
    main()