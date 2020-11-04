import yfinance as yf
import pandas as pd
import numpy as np

pd.options.display.max_columns = 12

df = yf.download('AAPL', auto_adjust=True, start='2017-01-01')

fast, slow = 10, 50
df['Cruce'] = df.Close.rolling(fast).mean() / df.Close.rolling(slow).mean() 
df['Estado'] = np.where(df.Cruce.shift() > 1.02 , 'Comprado', np.where(df.Cruce.shift() < 0.98, 'Vendido', 'Neutral'))
df['logDR'] = np.log(df.Close/df.Close.shift()) * 100
df['Estrategia'] = np.where(df.Estado=='Comprado', df.logDR , np.where( df.Estado=='Vendido' , -df.logDR  , 0 ) )
df = df.dropna().round(4)
df
