"""Modulo que exibe um grafico de uma linha exponencial com margem de erro

    Baseado de  https://tonysyu.github.io/plotting-error-bars.html
"""

from numpy import isscalar
import matplotlib.pyplot as plt

def plot_erro(x, y, y_erro, cor='green', alpha_fill=0.3, ax=None):
    """
     x: vetor-like que representa o eixo x
     y: vetor-like que representa o eixo y
     y_erro: vetor-like ou float scalar 0-1 que representa o erro da linha
     alpha_fill: transparencia do contorno de erro
     ax: instancia de eixos na figura
    """
    ax = ax if ax is not None else plt.gca()

    if isscalar(y_erro) or len(y_erro) == len(y):
        ymin = y - y_erro
        ymax = y + y_erro
    elif len(y_erro) == 2:
        ymin, ymax = y_erro
    
    ax.plot(x, y, color=cor)
    ax.fill_between(x, ymax, ymin, color=cor, alpha=alpha_fill)
