# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.19.9",
#     "matplotlib==3.10.8",
#     "nbformat==5.10.4",
#     "numpy==2.4.2",
#     "openai==2.17.0",
#     "pydantic-ai==1.56.0",
#     "sympy==1.14.0",
#     "wigglystuff==0.2.21",
# ]
# ///

import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def requerimientos():
    import numpy as np
    import sympy as sp
    import matplotlib.pyplot as plt
    import marimo as mo
    import matplotlib as mpl

    from wigglystuff import Slider2D

    return Slider2D, mo, plt


@app.cell
def parametros_de_estilo(plt):
    #! parametros estilo
    Texto_latex = True
    Plot_dark_inicial = True

    tam_fuente = 12

    if Plot_dark_inicial:
      plt.style.use('dark_background')
    else:
      plt.style.use('default')

    #! Configurar texto en LaTeX
    if Texto_latex:
      plt.rcParams.update({
        "text.usetex": True,
        # "font.family": "Helvetica"
        "font.size": tam_fuente,
        })  
    return


@app.cell
def funciones(plt):
    def func_f(x, y):
        return x ** 2 + y ** 2

    def draw_riemann(m, n, intervalo_x=(0, 5), intervalo_y=(0, 5), intervalo_x_graf=(-0.25, 5.25), intervalo_y_graf=(-0.25, 5.25), intervalo_z_graf=(0, 50),alpha=1, beta=1):
        largo_x = intervalo_x[1] - intervalo_x[0]
        largo_y = intervalo_y[1] - intervalo_y[0]

        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(intervalo_x_graf)
        ax.set_ylim(intervalo_y_graf)
        ax.set_zlim(intervalo_z_graf)

        dx = largo_x / m
        dy = largo_y / n

        vol_aprox = 0.0
        zmin = intervalo_z_graf[0]
        zmax = intervalo_z_graf[1]

        for i in range(m):
            for j in range(n):
                x_i = intervalo_x[0] + i * dx
                y_j = intervalo_y[0] + j * dy
                z0 = 0
                dz = func_f(x_i + alpha*dx, y_j + beta*dy)
                color = plt.cm.gnuplot((dz - zmin) / (zmax - zmin) if zmax > zmin else 0)
                ax.bar3d(x_i, y_j, z0, dx, dy, dz, color=color, alpha=0.9, shade=True)
                vol_aprox += dz * dx * dy

        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_zlabel('$z$')
        ax.set_title(f'Suma de Riemann de $f(x,y)=x^2+y^2$ ($m={m}$, $n={n}$)')

        return fig, vol_aprox

    return (draw_riemann,)


@app.cell
def elementos_interactivos(Slider2D, mo):
    slider_m = mo.ui.slider(0, 128, 1, 16, label="$m$", show_value=True)
    slider_n = mo.ui.slider(0, 128, 1, 16, label="$n$", show_value=True)
    slider_punto = mo.ui.anywidget(Slider2D(width=250,height=250,x_bounds=(0,1),y_bounds=(0,1),x=0.5,y=0.5))
    Plot_Dark_sel = mo.ui.switch(label="Modo oscuro grafico", value=True)
    return Plot_Dark_sel, slider_m, slider_n, slider_punto


@app.cell
def ejecucion(
    Plot_Dark_sel,
    draw_riemann,
    plt,
    slider_m,
    slider_n,
    slider_punto,
):
    m = slider_m.value
    n = slider_n.value
    a = slider_punto.x
    b = slider_punto.y
    Plot_dark = Plot_Dark_sel.value
    if Plot_dark:
        plt.style.use('dark_background')
    else:
        plt.style.use('default')

    fig, vol_app = draw_riemann(m,n,alpha=a,beta=b)
    # vol_real = sp.integrate(sp.integrate(func_f(sp.Symbol('x'), sp.Symbol('y')), (sp.Symbol('x'), 0, 5)), (sp.Symbol('y'), 0, 5))
    # volumen real calculado a mano es 1250/3 que es aproximadamente 416.6666666666667
    vol_real = 1250/3


    text_vol_app = f'Volumen aproximado: {vol_app:.2f}'
    text_vol_real = f'Volumen Real: {vol_real:.2f}'
    return fig, text_vol_app, text_vol_real


@app.cell(hide_code=True)
def mostrar(
    Plot_Dark_sel,
    fig,
    mo,
    slider_m,
    slider_n,
    slider_punto,
    text_vol_app,
    text_vol_real,
):
    mo.md(f"""
    # <center>Suma de Riemann 3D</center>
    {mo.hstack([mo.vstack(["Punto muestra:",slider_punto,slider_m,slider_n,text_vol_app,text_vol_real]),mo.as_html(fig)])}
    <br>
    <center>{Plot_Dark_sel}<center>
    """)
    return


@app.cell
def _(plt):
    #plt.rcParams.values()
    #plt.rcParams['font.cursive']
    #mpl.rcParams.values()
    plt.style.available
    return


if __name__ == "__main__":
    app.run()
