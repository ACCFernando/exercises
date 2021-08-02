from argparse import ArgumentParser
import yfinance as yf
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns

# %matplotlib inline

def get_graphs(ticker): 

    print(f"Imprimindo gráficos de {ticker}")

    tickerSymbol = ticker
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="Id",start='2010-5-31', end="2020-5-31")
    
    plt.figure(figsize=(8, 6), dpi=80)
    plt.subplot(2,1,1)  
    sns.lineplot(x=tickerDf.Close.index,y=tickerDf.Close)
    plt.subplot(2,1,2)
    sns.lineplot(x=tickerDf.Volume.index,y=tickerDf.Volume)
    # plt.savefig("graphs.jpg")
    plt.show()


if __name__=="__main__":
    parser = ArgumentParser(description="simple_sp")
    parser.add_argument("string", metavar="N", type=str,
    help="Insert Ticker")
    args = parser.parse_args()    
    
    ticker = args.string
    get_graphs(ticker)
    