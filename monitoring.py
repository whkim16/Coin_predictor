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
st.title("코인,코스피,나스닥 예측 시뮬레이션 검증 모니터링")


# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title("Coin Chart")
st.sidebar.markdown('비트/알트코인 Link : [All Coin Symbols](https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC)')
st.sidebar.markdown('코스피200 Link : [All Kospi200 Symbols](https://finance.naver.com/sise/sise_index.nhn?code=KPI200)')
st.sidebar.markdown('나스닥200 Link : [All Nasdaq200 Symbols](https://kr.investing.com/indices/nq-100-components)')


# 예측된 코인 갯수
# 예측 코인의 익일 평균 상승값, (종가 고가 저가)



import streamlit as st
import pandas as pd


## 코인 ##
# GitHub에서 Raw 형태의 데이터 URL
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/V_coin_web.csv'
data_coin_v = pd.read_csv(data_url)
#
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_web_org2_valid2.csv'
data_coin_a = pd.read_csv(data_url)

## 코스피 ##
# GitHub에서 Raw 형태의 데이터 URL
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/V_kospi_web.csv'
data_kospi_v = pd.read_csv(data_url)
#
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_kospi_web_org2_valid2.csv'
data_kospi_a = pd.read_csv(data_url)



select_date = st.selectbox(
    '예측일 선택',
    data_coin_v['pred_day'].sort_values(ascending=True).unique()
)
rule_rank = st.selectbox(
    '랭킹룰 선택',
    data_coin_v['GRP1'].sort_values(ascending=False).unique()
)

data_coin_v = data_coin_v.rename(columns={'pred_day': '예측일'})
data_coin_v = data_coin_v.rename(columns={'GRP1': '랭킹룰'})

data_coin_a = data_coin_a.rename(columns={'pred_day': '예측일'})

data_kospi_v = data_kospi_v.rename(columns={'pred_day': '예측일'})
data_kospi_v = data_kospi_v.rename(columns={'GRP1': '랭킹룰'})

# data_kospi_a = data_kospi_a.rename(columns={'pred_day': '예측일'})


st.markdown(f'## [▶ 코인 ◀] ')

st.markdown(f'#### 1. 코인 랭킹룰별 상승률 검증, 검증날짜: {formatted_date} 기준')
st.write(data_coin_v[(data_coin_v['예측일'] == select_date) & (data_coin_v['랭킹룰']  == rule_rank) ])

st.markdown(f'#### 2. 코인별 상승률 검증, 검증날짜: {formatted_date} 기준')
st.write(data_coin_a[(data_coin_a['예측일'] == select_date) ])



st.markdown(f'## [▶ KOSPI 200 ◀] ')

st.markdown(f'#### 1. KOSPI 200 랭킹룰 별 상승률 검증, 검증날짜: {formatted_date} 기준')
st.write(data_kospi_v[(data_kospi_v['예측일'] == select_date) & (data_kospi_v['랭킹룰']  == rule_rank) ])

st.markdown(f'#### 2. KOSPI 200 별 상승률 검증, 검증날짜: {formatted_date} 기준')
st.write(data_kospi_a[(data_kospi_a['예측일'] == select_date) ])



st.table(data_coin_v[(data_coin_v['예측일'] == select_date) & (data_coin_v['랭킹룰']  == rule_rank) ].T )

st.table(data_kospi_v[(data_kospi_v['예측일'] == select_date) & (data_kospi_v['랭킹룰']  == rule_rank) ].T )







st.markdown(f'### 1. 예측일자 {0}, 추천순위1 에 따른 모니터링')


st.markdown(f'##### 1.1 예측일자 {0}, 추천순위1 에 따른 익일 고점랭킹')

st.markdown(f'##### 1.2 예측일자 {0}, 추천순위1 에 따른 익일 종가랭킹')

st.markdown(f'##### 1.3 예측일자 {0}, 추천순위1 에 따른 N일 고점랭킹')

st.markdown(f'##### 1.4  예측일자 {0}, 추천순위1 에 따른 N일 종가랭킹')



st.markdown(f'### 2. 코예측일자 {0}, 익일 고점랭킹의 주요변수 평균값')

st.markdown(f'##### 2.1 코예측일자 {0}, 익일 종가랭킹의 주요변수 평균값')






