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


### 전체 코인 목록 
# st.write(pyupbit.get_tickers())
### 원화/달라/btc 매장별로 가능한 코인 목록
# st.write(pyupbit.get_tickers(fiat="KRW"))

COIN_LIST = pyupbit.get_tickers(fiat="KRW")


df = pyupbit.get_ohlcv(COIN_LIST[1], count=100, interval = "day")
st.write(df)







