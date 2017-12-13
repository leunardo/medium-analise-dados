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

plt.scatter(x, y)
plt.title('Temperatura media do Brasil desde 1800')
plt.show()
