from argparse import ArgumentParser
import yfinance as yf
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns

%matplotlib inline

# def get_graphs(ticker): 

#     st.write(f"""
#     # Aplicativo simples de preço de ação {ticker}

#     """)

#     tickerSymbol = ticker
#     tickerData = yf.Ticker(tickerSymbol)
#     tickerDf = tickerData.history(period="Id",start='2010-5-31', end="2020-5-31")

#     st.line_chart(tickerDf.Close)
#     st.line_chart(tickerDf.Volume)


# if __name__=="__main__":
#     parser = ArgumentParser(description="simple_sp")
#     parser.add_argument("string", metavar="N", type=str,
#     help="Insert Ticker")
#     args = parser.parse_args()    
    
#     ticker = args.string
#     get_graphs(ticker)
    
st.write(f"""
# Aplicativo simples de preço de ação GOOGL

""")

tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="Id",start='2010-5-31', end="2020-5-31")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
