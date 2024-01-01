import streamlit as st
import yfinance as yf
import pandas as pd


st.write("""
# Simple stock Price APP
""")
st.subheader(" Below shown are the stock closing price and volume of google! ")


tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d',start='2015-5-31',end='2023-5-31')

st.write("CLOSING PRICES")
st.line_chart(tickerDf.Close)


st.write("VOLUME GOOGLE STOCKS")
st.line_chart(tickerDf.Volume)

df=pd.DataFrame(tickerDf)
st.write("DATA GOOGLE STOCKS", df)
