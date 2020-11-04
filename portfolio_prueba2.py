import yfinance as yf
import pandas as pd
import numpy as np

df=yf.download("KO",auto_adjust=True,start="2017-01-01")
cruces=[(5,20),(20,100)]
df["logDR"]=np.log(df.Close/df.Close.shift())*100
for i in range(len(cruces)):
    df["Cruce_"+str(i)]=df.Close.rolling(cruces[i][0]).mean()/df.Close.rolling(cruces[i][1]).mean()
    df["Estado_" + str(i)] = np.where( df["Cruce_"+str(i)].shift() > 1.02 , "Comprado", np.where(df["Cruce_"+str(i)].shift()<0.98,"Vendido","Neutral" ))
    df["Estrategia_"+str(i)]=np.where(df["Estado_"+str(i)]=="Comprado",df.logDR,np.where(df["Estado_"+str(i)]=="Vendido",-df.logDR,0))
    
df=df.dropna().round(4)
df