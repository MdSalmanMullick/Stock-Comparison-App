import streamlit as st
import pandas as pd
import pandas_datareader as data
st.title('Stock Predictor')
tickers = st.text_input('Enter your ticker', 'TSLA')
start = st.date_input('Start', value = pd.to_datetime('2001-01-01'))
end = st.date_input('End', value = pd.to_datetime('2021-12-31'))
if len(tickers) > 0:
    dataframe = data.DataReader(tickers, 'yahoo', start, end)['Close']
    st.line_chart(dataframe)
