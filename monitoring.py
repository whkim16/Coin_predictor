# streamlit run app.py
# cd C:\Users\woohy\Desktop\streamlit_fd\
# streamlit run dashboard.py

# git add -A
# git commit -m 'commit message'
# git push origin dashborad


import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
import matplotlib.dates as mdates
import numpy as np



# st.title('this is title')
# st.header('this is header')
# st.subheader('this is subheader'


# 현재 날짜 가져오기
today = datetime.today()

# 날짜를 문자열로 변환하여 포매팅
formatted_date = today.strftime("%Y-%m-%d")

# Streamlit Markdown에 날짜 추가
st.title("코인예측 시뮬레이션 모니터링")
# st.markdown(f'### 1. 코인 추천랭킹, 예측날짜: {formatted_date} 9시 기준')


# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title("Coin Chart")
st.sidebar.markdown('비트/알트코인 Link : [All Coin Symbols](https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC)')
st.sidebar.markdown('코스피200 Link : [All Kospi200 Symbols](https://finance.naver.com/sise/sise_index.nhn?code=KPI200)')
st.sidebar.markdown('나스닥200 Link : [All Nasdaq200 Symbols](https://kr.investing.com/indices/nq-100-components)')


# 예측된 코인 갯수
# 예측 코인의 익일 평균 상승값, (종가 고가 저가)
# 

st.markdown(f'### 1. 예측일자 {0}, 추천순위1 에 따른 모니터링')


st.markdown(f'##### 1.1 예측일자 {0}, 추천순위1 에 따른 익일 고점랭킹')

st.markdown(f'##### 1.2 예측일자 {0}, 추천순위1 에 따른 익일 종가랭킹')

st.markdown(f'##### 1.3 예측일자 {0}, 추천순위1 에 따른 N일 고점랭킹')

st.markdown(f'##### 1.4  예측일자 {0}, 추천순위1 에 따른 N일 종가랭킹')



st.markdown(f'### 2. 코예측일자 {0}, 익일 고점랭킹의 주요변수 평균값')

st.markdown(f'##### 2.1 코예측일자 {0}, 익일 종가랭킹의 주요변수 평균값')
