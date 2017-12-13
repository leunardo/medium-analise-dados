# imports
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit
from plot_erro import plot_erro

data = pd.read_csv('./src/GlobalLandTemperaturesByCountry.csv')
brasil = data.where(data.Country == 'Brazil')

print(brasil.sample(10))
