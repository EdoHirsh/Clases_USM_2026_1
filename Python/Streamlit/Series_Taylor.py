import numpy as np
import scipy as scp
import sympy as syp
import matplotlib.pyplot as plt
import streamlit as st

#! Ejecutar con: streamlit run Series_Taylor.py

#* función creada por copilot web para invertir el orden de los terminos de un polinomio y generar su etiqueta en LaTeX, detectando fracciones e incluyendo x dentro de la fracción
def polinomio_latex_ascendente(expr, var='x', usar_dfrac=True, incluir_x_en_frac=True):
    x = syp.symbols(var)
    p = syp.Poly(expr, x)
    coeficientes = p.all_coeffs()[::-1]  # orden ascendente
    
    partes = []
    for i, c in enumerate(coeficientes):
        if c == 0:
            continue
        
        #* Detectar fracciones
        if isinstance(c, syp.Rational):
            num, den = c.as_numer_denom()
            if den == 1:  # entero
                coef_str = str(num)
            else:
                frac_cmd = "dfrac" if usar_dfrac else "frac"
                if incluir_x_en_frac and i > 0:
                    # x dentro de la fracción
                    if i == 1:
                        # Evitar 1x → solo x
                        if num == 1:
                            coef_str = f"\\{frac_cmd}{{{var}}}{{{den}}}"
                        elif num == -1:
                            coef_str = f"-\\{frac_cmd}{{{var}}}{{{den}}}"
                        else:
                            coef_str = f"\\{frac_cmd}{{{num}{var}}}{{{den}}}"
                    else:
                        if num == 1:
                            coef_str = f"\\{frac_cmd}{{{var}^{{{i}}}}}{{{den}}}"
                        elif num == -1:
                            coef_str = f"-\\{frac_cmd}{{{var}^{{{i}}}}}{{{den}}}"
                        else:
                            coef_str = f"\\{frac_cmd}{{{num}{var}^{{{i}}}}}{{{den}}}"
                else:
                    # x fuera de la fracción
                    coef_str = f"\\{frac_cmd}{{{num}}}{{{den}}}"
        else:
            coef_str = str(c)
        
        #* Construcción de términos
        if i == 0:
            partes.append(f"{coef_str}")
        elif i == 1:
            if coef_str == "1":
                partes.append(f"{var}")
            elif coef_str == "-1":
                partes.append(f"-{var}")
            else:
                if incluir_x_en_frac and isinstance(c, syp.Rational) and c.q != 1:
                    partes.append(coef_str)  # ya incluye x
                else:
                    partes.append(f"{coef_str}{var}")
        else:
            if coef_str == "1":
                partes.append(f"{var}^{{{i}}}")
            elif coef_str == "-1":
                partes.append(f"-{var}^{{{i}}}")
            else:
                if incluir_x_en_frac and isinstance(c, syp.Rational) and c.q != 1:
                    partes.append(coef_str)  # ya incluye x^i
                else:
                    partes.append(f"{coef_str}{var}^{{{i}}}")
    
    return " + ".join(partes).replace("+ -", "- ")

#* función a aproximar
def func_f(x) -> float:
    return np.exp(x)

#* polinomio de Taylor de la función func_f en x=0
@np.vectorize
def Taylor(x: float,n: int) -> float:
    return np.sum([(x**i)/scp.special.factorial(i) for i in range(n+1)])

#* Función para dibujar la función y su polinomio de Taylor
def Draw_Taylor(n, funcion = func_f, polinomio = Taylor, intervalo_x=[-10,10], intervalo_y=[-2,2], Plot_dark=False, tam_fuentes=12):
    if polinomio == Taylor:
        polinomio = lambda x: Taylor(x,n)
    Res_EjeX=1000

    dx = intervalo_x[1]-intervalo_x[0]
    dy = intervalo_y[1]-intervalo_y[0]
    intervalo_x_graf = [intervalo_x[0]-0.05*dx,intervalo_x[1]+0.05*dx]
    intervalo_y_graf = [intervalo_y[0]-0.05*dy,intervalo_y[1]+0.05*dy]

    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(*intervalo_x_graf)
    ax.set_ylim(*intervalo_y_graf)

    x=np.linspace(*intervalo_x_graf,Res_EjeX)
    y=funcion(x)

    #* dibujar ejes coordenados
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color = 'white' if Plot_dark else 'black')
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color = 'white' if Plot_dark else 'black')
    ax.set_xlabel(f'$x$', fontsize=tam_fuentes,loc='right')
    ax.set_ylabel(f'$y$', fontsize=tam_fuentes,loc='top',rotation='horizontal')

    #* Grafico de la función
    ax.plot(x,y,color='cyan' if Plot_dark else 'blue')

    #* Grafico el polinomio de Taylor
    x_T = np.linspace(*intervalo_x_graf,Res_EjeX)
    y_T = polinomio(x_T)
    ax.plot(x_T,y_T,color='magenta' if Plot_dark else 'red')

    ax.text(intervalo_x_graf[0],intervalo_y_graf[1],f'$n = {n}$', fontsize=tam_fuentes, color= 'white' if Plot_dark else 'black',horizontalalignment='left',verticalalignment='center')

    return fig , ax

def main():
    #! parametros para grafico
    Full_Latex = True
    Plot_dark = False

    tam_fuentes=12

    #* función simbolica para calcular el polinomio de Taylor con sympy
    x = syp.symbols('x')
    f_sym = syp.cos(x)

    #* transformar la funcion simbolica  y el polinomio de Taylor a funciones numericas para graficar
    f_num = syp.lambdify(x, f_sym, modules=['numpy'])

    #* grado del polinomio de Taylor
    n=6

    #* intervalos x e y
    intervalo_x = [-10,10]
    intervalo_y = [-2,2]

    if Full_Latex:
        plt.rcParams.update({
            "text.usetex": True,
            "font.size": tam_fuentes
        })

    #! Configuración de la página de Streamlit
    st.set_page_config(page_title=rf"Serie de Taylor de la función f(x)", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')#, menu_items={'Get Help': 'https://www.extremelycoolapp.com/help','Report a bug': "https://www.extremelycoolapp.com/bug",'About': "# This is a header. This is an *extremely* cool app!"})

    #! Titulo
    st.title(r'Serie de Taylor de la función $f(x)$')

    #! Checkboxes para opciones de visualización
    # func_select = st.sidebar.selectbox('Selecciona la función a aproximar', ('e^x', 'cos(x)', 'sen(x)', 'ln(1+x)'))#, format_func=lambda x: f'${x}$')
    # if func_select == 'e^x':
    #     f_sym = syp.exp(x)
    #     f_num = syp.lambdify(x, f_sym, modules=['numpy'])
    # elif func_select == 'cos(x)':
    #     f_sym = syp.cos(x)
    #     f_num = syp.lambdify(x, f_sym, modules=['numpy'])
    # elif func_select == 'sen(x)':
    #     f_sym = syp.sin(x)
    #     f_num = syp.lambdify(x, f_sym, modules=['numpy'])
    # elif func_select == 'ln(1+x)':
    #     f_sym = syp.log(1+x)
    #     f_num = syp.lambdify(x, f_sym, modules=['numpy'])
    func_select = st.sidebar.text_input('Indique la función (en términos de x)', value='cos(x)')
    try:
        f_sym = syp.sympify(func_select)
        f_num = syp.lambdify(x, f_sym, modules=['numpy'])
        n = st.sidebar.number_input('indique el valor de $n$', min_value=0, value=n, step=1)
        Plot_dark = st.sidebar.toggle(label='Gráfico modo oscuro', value=Plot_dark)
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

        #* calcular el polinomio de Taylor con sympy y su versión numérica para graficar
        Taylor_sym = f_sym.series(x, 0, n+1).removeO()
        if Taylor_sym.is_constant(x):
            Taylor_num = np.vectorize(syp.lambdify(x, Taylor_sym, modules=['numpy']))
        else:
            Taylor_num = syp.lambdify(x, Taylor_sym, modules=['numpy'])

        #! Generar gráfico con spinner
        with st.spinner('Generando gráfico...'):
            fig , _ = Draw_Taylor(n, funcion=f_num, polinomio=Taylor_num, intervalo_x=intervalo_x, intervalo_y=intervalo_y, Plot_dark=Plot_dark, tam_fuentes=tam_fuentes)
            st.pyplot(fig)
            st.latex(f'f(x) = {syp.latex(f_sym)}')
            # st.latex(f'T_{{{n}}}(x) = {syp.latex(Taylor_sym)}')
            st.latex(f'T_{{{n}}}(x) = {polinomio_latex_ascendente(Taylor_sym)}')
    except:
        st.error('La función ingresada no es válida. Por favor, ingrese una función en términos de x, por ejemplo: cos(x), exp(x), sin(x), log(1+x), etc.')
        return


if __name__ == "__main__":
    main()