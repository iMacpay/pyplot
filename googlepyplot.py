
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json




df = pd.read_csv("C:\\Users\\Administrator\\PycharmProjects\\pythonProject1\\gitpyplot\\fastapi\\20210904.csv", index_col=0)
dk=df.T
#df.plot.line( )
#plt.show()
js=df.to_json(orient="index", force_ascii=False)
json1=json.loads(js)
dk.iloc[-5:-1,30:100].plot()
plt.show()