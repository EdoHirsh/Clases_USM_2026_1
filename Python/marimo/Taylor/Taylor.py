# /// script
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.8",
#     "nbformat==5.10.4",
#     "numpy==2.4.2",
#     "scipy==1.17.1",
# ]
# requires-python = ">=3.11"
# ///

import marimo

__generated_with = "0.19.9"
app = marimo.App(width="full", auto_download=["html", "ipynb"])


@app.cell
def requisitos():
    import marimo as mo
    import numpy as np
    import scipy as scp
    import math
    import matplotlib.pyplot as plt

    #from mpl_toolkits.axisartist.axislines import AxesZero

    return mo, np, plt, scp


@app.cell
def preparacion(plt):
    Texto_Latex = False
    Plot_dark = True

    tam_fuente = 12

    if Plot_dark:
      plt.style.use('dark_background')
    else:
      plt.style.use('default')

    if Texto_Latex:
        plt.rcParams.update({
            "text.usetex": True,
            # "font.family": "Helvetica"
            "font.size": tam_fuente
        })
    return (tam_fuente,)


@app.cell
def funciones(np, plt, scp, tam_fuente):
    def func_f(x) -> float:
        return np.exp(x)

    def Taylor(x: float,n: int) -> float:
        return np.sum([(x**i)/scp.special.factorial(i) for i in range(n+1)])

    def Draw_Taylor(n, intervalo_x=[-10,10], intervalo_y=[-2,2], intervalo_x_graf=[-10.1,10.1], intervalo_y_graf=[-2.1,2.1]):
        Res_EjeX=1000
        N_Max=n
    
        fig = plt.figure(figsize=(20,10))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlim(*intervalo_x_graf)
        ax.set_ylim(*intervalo_y_graf)

        x=np.linspace(*intervalo_x,Res_EjeX)
        y=func_f(x)

        #! Creacion de los ejes 
        # mover bordes izquierdo e inferior a x = 0 and y = 0, respectivamente
        ax.spines[["left", "bottom"]].set_position(("data", 0))
        # esconder los bordes superior y derecho
        ax.spines[["top", "right"]].set_visible(False)
        # dibujar las flechas de los ejes
        ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
        ax.set_xlabel(f'$x$', fontsize=tam_fuente,loc='right')
        ax.set_ylabel(f'$y$', fontsize=tam_fuente,loc='top',rotation='horizontal')

        # Grafico de la función
        ax.plot(x,y,color='blue')

        # Grafico el polinomio de Taylor
        x_T = np.linspace(*intervalo_x,Res_EjeX)
        y_T = np.zeros(Res_EjeX)
        for i in range(Res_EjeX):
            y_T[i]=Taylor(x_T[i],N_Max)
        ax.plot(x_T,y_T,color='red')

        # if Plot_dark:
        #     text_color = 'white'
        # else:
        #     text_color = 'black'
        # ax.text(intervalo_x_graf[0],intervalo_y_graf[1],f'$n = {N_Max}$', fontsize=tam_fuente, color=text_color,horizontalalignment='left',verticalalignment='center')

        return fig

    return (Draw_Taylor,)


@app.cell
def _(mo):
    slider_n = mo.ui.slider(0, 30, 1, 4, label="$n$", show_value=True, full_width=False)
    return (slider_n,)


@app.cell
def _(Draw_Taylor, slider_n):
    n = slider_n.value

    fig = Draw_Taylor(n)
    return (fig,)


@app.cell(hide_code=True)
def _(fig, mo, slider_n):
    mo.md(rf"""
    # <center>Polinomio de Taylor</center>
    {mo.vstack([slider_n, mo.as_html(fig)])}
    """)
    return


if __name__ == "__main__":
    app.run()
