
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("20210904.csv",index_col=0)
dk=df.T
#df.plot.line( )
#plt.show()

dk.iloc[-5:-1,0:100].plot.line()
plt.show()