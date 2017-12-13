# imports
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit
from plot_erro import plot_erro

data = pd.read_csv('./src/GlobalLandTemperaturesByCountry.csv')
brasil = data.where(data.Country == 'Brazil')

brasil = brasil.dropna() # removemos os registros vazios

brasil.dt = [d.split('-')[0] for d in brasil.dt] # formata a data de yyyy-mm-dd para yyyy
brasil_groupby_ano = brasil.groupby('dt') # agrupa os valores por data


# preparar exibicao

x = [int(dt[0]) for dt in brasil_groupby_ano.dt] # converte o ano de string para int
y = brasil_groupby_ano.AverageTemperature.mean() # calcula media das temperaturas em cada ano
sigma = brasil_groupby_ano.AverageTemperatureUncertainty.mean() # media do erro no ano

plt.scatter(x, y) # adiciona os pontos no grafico
plt.title('Temperatura media do Brasil desde 1800')

# efetua a exponenciacao do numero pelo
# logaritmo natural + parametros de otimizacao
def exponenciar(x, a, b, c):
    return a * np.exp(-b * x) + c

# ajuste de curvas dada a nossa funcao e os eixos
popt, _ = curve_fit(exponenciar, x, y, p0=(1, 1e-6, 1), maxfev=4000, sigma=sigma)

xx = np.linspace(1800, 2020) # cria numeros iguais distribuidos de 1800 ate 2020
yy = exponenciar(xx, *popt) # yy = f(xx), adequados aos params de otimizacao

# essa funcao exibe uma linha com um sombreado em volta, representando a margem de erro
plot_erro(xx, yy, .05)

plt.show()
