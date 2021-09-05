import asyncio
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import *
from datetime import datetime
import time
import sys
import os
dir_path=os.path.dirname(os.path.realpath(__file__))
parent_dir_path= os.path.abspath(os.path.join(dir_path,os.pardir))
sys.path.insert(0,parent_dir_path)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

app = FastAPI()

def caculate():
    df = pd.read_csv("20210904.csv", index_col=0)
    js=df.to_json(orient="index",force_ascii=False)
    respjson = json.loads(js)
  #  dk=df.T
    #df.plot.line( )
    #plt.show()
   # dk.iloc[-5:-1,30:100].plot()
    return respjson

@app.head("/")
def home():
    return ""


@app.get("/getdata")
def home():
    alljsondate=caculate()
    return alljsondate


@app.get("/reset")
async def reset():
    global counter, proxies
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app='run:app', host="127.0.0.1", port=8000, log_level="info")
