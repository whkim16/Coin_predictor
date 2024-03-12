import sys

import plotly.graph_objects as go
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

import pandas as pd
import numpy as np
import time
import pyupbit


# 현재 날짜 가져오기
today = datetime.today()

# 날짜를 문자열로 변환하여 포매팅
formatted_date = today.strftime("%Y-%m-%d")

# Streamlit Markdown에 날짜 추가
st.title("코인 데시보드")
st.markdown(f'### 1. 코인 가격 날짜: {formatted_date} 9시 기준')

# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title("Coin Chart")
st.sidebar.markdown('비트/알트코인 Link : [All Coin Symbols](https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC)')
st.sidebar.markdown('코스피200 Link : [All Kospi200 Symbols](https://finance.naver.com/sise/sise_index.nhn?code=KPI200)')
st.sidebar.markdown('나스닥200 Link : [All Nasdaq200 Symbols](https://kr.investing.com/indices/nq-100-components)')

@st.cache(hash_funcs={type: lambda x: None})
### 전체 코인 목록 
# st.write(pyupbit.get_tickers())
### 원화/달라/btc 매장별로 가능한 코인 목록
# st.write(pyupbit.get_tickers(fiat="KRW"))

COIN_LIST = pyupbit.get_tickers(fiat="KRW")

select_coin = st.selectbox(
    'Coinlist',
    COIN_LIST
)
coin1 = 'KRW-BTC'
coin2 = 'KRW-VET'
coin3 = 'KRW-DOGE'
coin4 = 'KRW-ELF'
coin5 = select_coin


st.markdown(f'###### 👈 코인 : {coin1} 가격변동 ')
df1 = pyupbit.get_ohlcv(coin1, count=4, interval = "day")
st.write(df1[['open','close']].T) 
st.markdown(f'###### 👈 코인 : {coin2} 가격변동 ')
df2 = pyupbit.get_ohlcv(coin2, count=4, interval = "day")
st.write(df2[['open','close']].T) 
st.markdown(f'###### 👈 코인 : {coin3} 가격변동 ')
df3 = pyupbit.get_ohlcv(coin3, count=4, interval = "day")
st.write(df3[['open','close']].T) 
st.markdown(f'###### 👈 코인 : {coin4} 가격변동 ')
df4 = pyupbit.get_ohlcv(coin4, count=4, interval = "day")
st.write(df4[['open','close']].T) 


st.markdown(f'###### 👈 코인선택 : {coin5} 가격변동 ')
df5 = pyupbit.get_ohlcv(coin5, count=4, interval = "day")
st.write(df5[['open','close']].T) 



