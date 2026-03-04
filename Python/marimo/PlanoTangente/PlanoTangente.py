# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "matplotlib==3.10.8",
#     "nbformat==5.10.4",
#     "numpy==2.4.2",
#     "sympy==1.14.0",
#     "wigglystuff==0.2.32",
# ]
# ///

import marimo

__generated_with = "0.20.2"
app = marimo.App(
    width="medium",
    app_title="Plano Tangente Interactivo",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def imports():
    import marimo as mo
    import numpy as np
    import sympy as sp
    import matplotlib.pyplot as plt

    from wigglystuff import Slider2D

    return Slider2D, mo, np, plt, sp


@app.cell
def parametros_estilo(plt):
    #! parametros estilo
    Plot_dark_inicial = True
    tam_fuentes = 12

    if Plot_dark_inicial:
        plt.style.use('dark_background')
    else:
        plt.style.use('default')

    plt.rcParams.update({
        "text.usetex": True,
        # "font.family": "Helvetica"
        "font.size": tam_fuentes,
        })  
    return


@app.cell
def funciones(np, plt, sp):
    # función de dos variables para graficar
    def func(x, y):
        return (x**2 + y**2)

    def Superficie(N, X, Y, intervalo_z=None):
        Z = func(X, Y)
        #* Cortar los valores de z si están fuera de intervalo_z
        if intervalo_z is not None:
            Z[Z>intervalo_z[1]]=np.nan
            Z[Z<intervalo_z[0]]=np.nan
        return Z

    def Plano_Tangente(x_0, y_0, N, X, Y, intervalo_z=None, Cortar_Z_fuera_rango=False):
        # version simbolica de la funcion
        x, y = sp.symbols('x y')
        f_sym = (x**2 + y**2)

        f_0 = func(x_0, y_0)
        df_dx = sp.diff(f_sym, x)
        df_dy = sp.diff(f_sym, y)

        gradiente = (df_dx.subs({x: x_0, y: y_0}), df_dy.subs({x: x_0, y: y_0}))

        # Ecuación del plano tangente
        Z_p = f_0 + gradiente[0]*(X - x_0) + gradiente[1]*(Y - y_0)

        if intervalo_z is not None:
            Z_p[Z_p>intervalo_z[1]]=np.nan
            Z_p[Z_p<intervalo_z[0]]=np.nan

        return Z_p

    # función que gráfica la superficie y el plano tangente
    def Grafica_Superficie_Plano_Tangente(x_0=1, y_0=1, rango_x = [-4,4], rango_y = [-4,4], rango_z=None, N=25):
        x_points = np.linspace(*rango_x, N)
        y_points = np.linspace(*rango_y, N)
        X, Y = np.meshgrid(x_points, y_points)

        Z = Superficie(N, X, Y, intervalo_z=rango_z)
        Z_p = Plano_Tangente(x_0, y_0, N, X, Y, intervalo_z=rango_z)

        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')

        ax.set_aspect('equal')
        ax.set_xlim(*rango_x)
        ax.set_ylim(*rango_y)
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_zlabel('$z$')

        # graficar superficie y plano tangente
        f_0 = func(x_0, y_0)
        ax.plot_surface(X, Y, Z, cmap='gnuplot', edgecolor='none', alpha=0.7)
        ax.plot_surface(X, Y, Z_p, color='blue', edgecolor='none', alpha=0.7)
        ax.scatter(x_0, y_0, f_0, color='k', s=50,alpha=0.5)

        return fig

    return (Grafica_Superficie_Plano_Tangente,)


@app.cell
def elementos_interactivos(Slider2D, mo):
    slider_punto = mo.ui.anywidget(Slider2D(width=250,height=250,x_bounds=(-4,4),y_bounds=(-4,4),x=1,y=1))
    slider_N = mo.ui.slider(10,100,1,25,label=f"N",show_value=True)
    Plot_Dark_sel = mo.ui.switch(label="Modo oscuro grafico", value=True)
    return Plot_Dark_sel, slider_N, slider_punto


@app.cell
def creacion_figura(
    Grafica_Superficie_Plano_Tangente,
    Plot_Dark_sel,
    plt,
    slider_N,
    slider_punto,
):
    x_0 = slider_punto.x
    y_0 = slider_punto.y
    N = slider_N.value
    Plot_dark = Plot_Dark_sel.value
    if Plot_dark:
        plt.style.use('dark_background')
    else:
        plt.style.use('default')
    fig = Grafica_Superficie_Plano_Tangente(x_0,y_0,N=N)
    return (fig,)


@app.cell(hide_code=True)
def _(Plot_Dark_sel, fig, mo, slider_N, slider_punto):
    mo.md(rf"""
    # <center>Plano tangente interactivo</center>
    {mo.hstack([mo.vstack([slider_punto,slider_N]),mo.as_html(fig)])}
    <br>
    <center>{Plot_Dark_sel}<center>
    """)
    return


if __name__ == "__main__":
    app.run()
