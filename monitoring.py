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

pd.options.display.float_format = '{:.2f}'.format

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
data_coin_v = pd.read_csv(data_url, encoding='CP949')
#
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_web_org2_valid2.csv'
data_coin_a = pd.read_csv(data_url, encoding='CP949')

data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/cor_coin.csv'
data_coin_cr = pd.read_csv(data_url, encoding='CP949')

data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/chart365_coin.csv'
data_coin_pr = pd.read_csv(data_url, encoding='CP949')

data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/ccf_coin.csv'
data_coin_ccf = pd.read_csv(data_url, encoding='CP949')



## 코스피 ##
# GitHub에서 Raw 형태의 데이터 URL
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/V_kospi_web.csv'
data_kospi_v = pd.read_csv(data_url, encoding='CP949')
#
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_kospi_web_org2_valid2.csv'
data_kospi_a = pd.read_csv(data_url, encoding='CP949')

## 나스닥 ##
# GitHub에서 Raw 형태의 데이터 URL
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/V_nasdaq_web.csv'
data_nasdaq_v = pd.read_csv(data_url, encoding='CP949')
#
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_nasdaq_web_org2_valid2.csv'
data_nasdaq_a = pd.read_csv(data_url, encoding='CP949')











data_coin_v = data_coin_v.rename(columns={'pred_day': '예측일'})
data_coin_v = data_coin_v.rename(columns={'GRP1': '랭킹룰'})
data_coin_v = data_coin_v.rename(columns={'GRP2': '랭킹순위구분'})

data_coin_a = data_coin_a.rename(columns={'pred_day': '예측일'})

data_kospi_v = data_kospi_v.rename(columns={'pred_day': '예측일'})
data_kospi_v = data_kospi_v.rename(columns={'GRP1': '랭킹룰'})
data_kospi_v = data_kospi_v.rename(columns={'GRP2': '랭킹순위구분'})

data_kospi_a = data_kospi_a.rename(columns={'pred_day': '예측일'})

data_nasdaq_v = data_nasdaq_v.rename(columns={'pred_day': '예측일'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'GRP1': '랭킹룰'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'GRP2': '랭킹순위구분'})

data_nasdaq_a = data_nasdaq_a.rename(columns={'pred_day': '예측일'})


data_coin_v['랭킹순위구분'] = data_coin_v['랭킹순위구분'].replace({'A1_5' : 'Top5', 'B6_10' : 'Top6~10', 'C11_15' : 'Top11~15', 'D16_20' : 'Top16~20', 'Z21~all' : '기타' })
data_kospi_v['랭킹순위구분'] = data_kospi_v['랭킹순위구분'].replace({'A1_5' : 'Top5', 'B6_10' : 'Top6~10', 'C11_15' : 'Top11~15', 'D16_20' : 'Top16~20', 'Z21~all' : '기타' })
data_nasdaq_v['랭킹순위구분'] = data_nasdaq_v['랭킹순위구분'].replace({'A1_5' : 'Top5', 'B6_10' : 'Top6~10', 'C11_15' : 'Top11~15', 'D16_20' : 'Top16~20', 'Z21~all' : '기타' })




data_coin_v = data_coin_v.rename(columns={'ophi_A_1up_cnt': '1D_고점상승비중'})
data_coin_v = data_coin_v.rename(columns={'ophi_B_2_4up_cnt': '4D_고점상승비중'})
data_coin_v = data_coin_v.rename(columns={'ophi_C_5_7up_cnt': '7D_고점상승비중'})
data_coin_v = data_coin_v.rename(columns={'ophi_D_8_12up_cnt': '12D_고점상승비중'})
data_coin_v = data_coin_v.rename(columns={'opcl_A_1up_cnt': '1D_종가상승비중'})
data_coin_v = data_coin_v.rename(columns={'opcl_B_2_4up_cnt': '4D_종가상승비중'})
data_coin_v = data_coin_v.rename(columns={'opcl_C_5_7up_cnt': '7D_종가상승비중'})
data_coin_v = data_coin_v.rename(columns={'opcl_D_8_12up_cnt': '12D_종가상승비중'})
data_coin_v = data_coin_v.rename(columns={'oplw_A_1up_cnt': '1D_저점상승비중'})
data_coin_v = data_coin_v.rename(columns={'oplw_B_2_4up_cnt': '4D_저점상승비중'})
data_coin_v = data_coin_v.rename(columns={'oplw_C_5_7up_cnt': '7D_저점상승비중'})
data_coin_v = data_coin_v.rename(columns={'oplw_D_8_12up_cnt': '12D_저점상승비중'})

data_coin_v = data_coin_v.rename(columns={'ophi_A_1up_avg': '1D_고점상승평균'})
data_coin_v = data_coin_v.rename(columns={'ophi_B_2_4up_avg': '4D_고점상승평균'})
data_coin_v = data_coin_v.rename(columns={'ophi_C_5_7up_avg': '7D_고점상승평균'})
data_coin_v = data_coin_v.rename(columns={'ophi_D_8_12up_avg': '12D_고점상승평균'})
data_coin_v = data_coin_v.rename(columns={'opcl_A_1up_avg': '1D_종가상승평균'})
data_coin_v = data_coin_v.rename(columns={'opcl_B_2_4up_avg': '4D_종가상승평균'})
data_coin_v = data_coin_v.rename(columns={'opcl_C_5_7up_avg': '7D_종가상승평균'})
data_coin_v = data_coin_v.rename(columns={'opcl_D_8_12up_avg': '12D_종가상승평균'})
data_coin_v = data_coin_v.rename(columns={'oplw_A_1up_avg': '1D_저점상승평균'})
data_coin_v = data_coin_v.rename(columns={'oplw_B_2_4up_avg': '4D_저점상승평균'})
data_coin_v = data_coin_v.rename(columns={'oplw_C_5_7up_avg': '7D_저점상승평균'})
data_coin_v = data_coin_v.rename(columns={'oplw_D_8_12up_avg': '12D_저점상승평균'})

data_coin_a = data_coin_a.rename(columns={'ophi_A_1Day': '1D_고점상승비중'})
data_coin_a = data_coin_a.rename(columns={'ophi_B_2_4Day': '4D_고점상승비중'})
data_coin_a = data_coin_a.rename(columns={'ophi_C_5_7Day': '7D_고점상승비중'})
data_coin_a = data_coin_a.rename(columns={'ophi_D_8_12Day': '12D_고점상승비중'})
data_coin_a = data_coin_a.rename(columns={'opcl_A_1Day': '1D_종가상승비중'})
data_coin_a = data_coin_a.rename(columns={'opcl_B_2_4Day': '4D_종가상승비중'})
data_coin_a = data_coin_a.rename(columns={'opcl_C_5_7Day': '7D_종가상승비중'})
data_coin_a = data_coin_a.rename(columns={'opcl_D_8_12Day': '12D_종가상승비중'})
data_coin_a = data_coin_a.rename(columns={'oplw_A_1Day': '1D_저점상승비중'})
data_coin_a = data_coin_a.rename(columns={'oplw_B_2_4Day': '4D_저점상승비중'})
data_coin_a = data_coin_a.rename(columns={'oplw_C_5_7Day': '7D_저점상승비중'})
data_coin_a = data_coin_a.rename(columns={'oplw_D_8_12Day': '12D_저점상승비중'})




data_kospi_v = data_kospi_v.rename(columns={'ophi_A_1up_cnt': '1D_고점상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'ophi_B_2_4up_cnt': '4D_고점상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'ophi_C_5_7up_cnt': '7D_고점상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'ophi_D_8_12up_cnt': '12D_고점상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'opcl_A_1up_cnt': '1D_종가상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'opcl_B_2_4up_cnt': '4D_종가상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'opcl_C_5_7up_cnt': '7D_종가상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'opcl_D_8_12up_cnt': '12D_종가상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'oplw_A_1up_cnt': '1D_저점상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'oplw_B_2_4up_cnt': '4D_저점상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'oplw_C_5_7up_cnt': '7D_저점상승비중'})
data_kospi_v = data_kospi_v.rename(columns={'oplw_D_8_12up_cnt': '12D_저점상승비중'})

data_kospi_v = data_kospi_v.rename(columns={'ophi_A_1up_avg': '1D_고점상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'ophi_B_2_4up_avg': '4D_고점상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'ophi_C_5_7up_avg': '7D_고점상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'ophi_D_8_12up_avg': '12D_고점상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'opcl_A_1up_avg': '1D_종가상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'opcl_B_2_4up_avg': '4D_종가상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'opcl_C_5_7up_avg': '7D_종가상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'opcl_D_8_12up_avg': '12D_종가상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'oplw_A_1up_avg': '1D_저점상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'oplw_B_2_4up_avg': '4D_저점상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'oplw_C_5_7up_avg': '7D_저점상승평균'})
data_kospi_v = data_kospi_v.rename(columns={'oplw_D_8_12up_avg': '12D_저점상승평균'})


data_kospi_a = data_kospi_a.rename(columns={'ophi_A_1Day': '1D_고점상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'ophi_B_2_4Day': '4D_고점상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'ophi_C_5_7Day': '7D_고점상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'ophi_D_8_12Day': '12D_고점상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'opcl_A_1Day': '1D_종가상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'opcl_B_2_4Day': '4D_종가상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'opcl_C_5_7Day': '7D_종가상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'opcl_D_8_12Day': '12D_종가상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'oplw_A_1Day': '1D_저점상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'oplw_B_2_4Day': '4D_저점상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'oplw_C_5_7Day': '7D_저점상승비중'})
data_kospi_a = data_kospi_a.rename(columns={'oplw_D_8_12Day': '12D_저점상승비중'})





data_nasdaq_v = data_nasdaq_v.rename(columns={'ophi_A_1up_cnt': '1D_고점상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'ophi_B_2_4up_cnt': '4D_고점상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'ophi_C_5_7up_cnt': '7D_고점상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'ophi_D_8_12up_cnt': '12D_고점상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'opcl_A_1up_cnt': '1D_종가상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'opcl_B_2_4up_cnt': '4D_종가상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'opcl_C_5_7up_cnt': '7D_종가상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'opcl_D_8_12up_cnt': '12D_종가상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'oplw_A_1up_cnt': '1D_저점상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'oplw_B_2_4up_cnt': '4D_저점상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'oplw_C_5_7up_cnt': '7D_저점상승비중'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'oplw_D_8_12up_cnt': '12D_저점상승비중'})

data_nasdaq_v = data_nasdaq_v.rename(columns={'ophi_A_1up_avg': '1D_고점상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'ophi_B_2_4up_avg': '4D_고점상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'ophi_C_5_7up_avg': '7D_고점상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'ophi_D_8_12up_avg': '12D_고점상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'opcl_A_1up_avg': '1D_종가상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'opcl_B_2_4up_avg': '4D_종가상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'opcl_C_5_7up_avg': '7D_종가상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'opcl_D_8_12up_avg': '12D_종가상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'oplw_A_1up_avg': '1D_저점상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'oplw_B_2_4up_avg': '4D_저점상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'oplw_C_5_7up_avg': '7D_저점상승평균'})
data_nasdaq_v = data_nasdaq_v.rename(columns={'oplw_D_8_12up_avg': '12D_저점상승평균'})


data_nasdaq_a = data_nasdaq_a.rename(columns={'ophi_A_1Day': '1D_고점상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'ophi_B_2_4Day': '4D_고점상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'ophi_C_5_7Day': '7D_고점상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'ophi_D_8_12Day': '12D_고점상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'opcl_A_1Day': '1D_종가상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'opcl_B_2_4Day': '4D_종가상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'opcl_C_5_7Day': '7D_종가상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'opcl_D_8_12Day': '12D_종가상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'oplw_A_1Day': '1D_저점상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'oplw_B_2_4Day': '4D_저점상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'oplw_C_5_7Day': '7D_저점상승비중'})
data_nasdaq_a = data_nasdaq_a.rename(columns={'oplw_D_8_12Day': '12D_저점상승비중'})







st.markdown(f'## [  코인  ] ')

# select_date = st.sidebar.selectbox(
#     '예측일 선택',
#     data_coin_v['pred_day'].sort_values(ascending=True).unique()
# )
select_date = st.selectbox(
    '예측일 선택',
    data_coin_v['예측일'].sort_values(ascending=True).unique()
)
rule_rank = st.selectbox(
    '랭킹룰 선택',
    ['RE_RANK','RE_RANK_UP','NO_UP_HIGH16','NO_UP_HIGH1']
    # data_coin_v['GRP1'].sort_values(ascending=False).unique()
)

st.markdown(f'#### 1. 코인 랭킹룰별 상승률 검증, 검증날짜: {formatted_date} 기준')

st.markdown(f'###### 👈 1.1 예측 후 날짜경과별 <시가 대비 고점상승> 비중 및 평균값,  예측날짜: {select_date} 기준, 랭킹룰 : {rule_rank}')
col1,col2 = st.columns([1,1])
with col1 :
    st.write(data_coin_v[(data_coin_v['예측일'] == select_date) & (data_coin_v['랭킹룰']  == rule_rank) ][[
        '랭킹순위구분','1D_고점상승비중','4D_고점상승비중','7D_고점상승비중','12D_고점상승비중']].T )
with col2 :
    st.write(data_coin_v[(data_coin_v['예측일'] == select_date) & (data_coin_v['랭킹룰']  == rule_rank) ][[
        '랭킹순위구분', '1D_고점상승평균','4D_고점상승평균','7D_고점상승평균','12D_고점상승평균']].T )

st.markdown(f'###### 👈 1.2 예측 후 날짜경과별 <시가 대비 종가상승> 비중 및 평균값,  예측날짜: {select_date} 기준, 랭킹룰 : {rule_rank}')
col3,col4 = st.columns([1,1])
with col3 :
    st.write(data_coin_v[(data_coin_v['예측일'] == select_date) & (data_coin_v['랭킹룰']  == rule_rank) ][[
        '랭킹순위구분','1D_종가상승비중','4D_종가상승비중','7D_종가상승비중','12D_종가상승비중']].T )
with col4 :
    st.write(data_coin_v[(data_coin_v['예측일'] == select_date) & (data_coin_v['랭킹룰']  == rule_rank) ][[
        '랭킹순위구분','1D_종가상승평균','4D_종가상승평균','7D_종가상승평균','12D_종가상승평균']].T )
    
st.markdown(f'###### 👈 1.3 예측 후 날짜경과별 <시가 대비 저점상승> 비중 및 평균값,  예측날짜: {select_date} 기준, 랭킹룰 : {rule_rank}')
col5,col6 = st.columns([1,1])
with col5 :
    st.write(data_coin_v[(data_coin_v['예측일'] == select_date) & (data_coin_v['랭킹룰']  == rule_rank) ][[
        '랭킹순위구분','1D_저점상승비중','4D_저점상승비중','7D_저점상승비중','12D_저점상승비중']].T )
with col6 :
    st.write(data_coin_v[(data_coin_v['예측일'] == select_date) & (data_coin_v['랭킹룰']  == rule_rank) ][[
        '랭킹순위구분','1D_저점상승평균','4D_저점상승평균','7D_저점상승평균','12D_저점상승평균']].T )
    




# st.write(data_coin_v[(data_coin_v['예측일'] == select_date) & (data_coin_v['랭킹룰']  == rule_rank) ])

st.markdown(f'#### 👋 1.4 코인별 상승률 검증, 검증날짜: {formatted_date} 기준')
st.write(data_coin_a[(data_coin_a['예측일'] == select_date) ])

st.markdown(f'#### 👋 1.5 코인별 상승률 검증, 검증날짜: {formatted_date} 기준')
select_coin2 = st.selectbox(
    '코인 선택',
    ['all'] + list(data_coin_a['coin'].sort_values(ascending=True).unique())   # ['a', 'b']
)
select_date2 = st.selectbox(
    '예측일 선택',
    data_coin_a['예측일'].sort_values(ascending=False).unique()
)
rule_rank2 = st.selectbox(
    '랭킹룰 선택',
    ['RE_RANK','RE_RANK_UP','NO_UP_HIGH1','NO_UP_CL16', 'NO_UP_HIGH16', 'NO_UP_LOW16','NO_UP_HCL16','NO_DOWN', 'NO_DOWN_CL16',
    'filter1','filter2','filter3', 'filter4']
)
real_uprate2 = st.selectbox(
    '실제상승률지표 선택',
    ['1D_고점상승비중','4D_고점상승비중','7D_고점상승비중','12D_고점상승비중',
     '1D_종가상승비중','4D_종가상승비중','7D_종가상승비중','12D_종가상승비중',
     '1D_저점상승비중','4D_저점상승비중','7D_저점상승비중','12D_저점상승비중']
)
st.markdown(f'###### 👋 1.5.1 코인별 랭킹패턴 및 상승률 비교,  예측날짜: {select_date2} 기준, 랭킹룰 : {rule_rank2}')
data_coin_a2 = pd.DataFrame(data_coin_a)
data_coin_a_pv2 = pd.pivot_table(data_coin_a2, values = rule_rank2, index = 'coin', columns = '예측일' , aggfunc = 'first').reset_index() 
data_coin_a3 = data_coin_a[ (data_coin_a['예측일'] == select_date2)][['coin', real_uprate2]]

data_coin_a_pv2 = pd.merge(data_coin_a_pv2, data_coin_a3, left_on='coin', right_on='coin', how='left')
# 순위 부여하기
# data_coin_a_pv2['rank'] = data_coin_a_pv2.iloc[:, -1].rank()
data_coin_a_pv2 = data_coin_a_pv2.sort_values(by=real_uprate2, ascending = False)


if select_coin2 == 'all':
      st.write(data_coin_a_pv2)
else:
    st.write(data_coin_a_pv2[ (data_coin_a_pv2['coin']  == select_coin2) ])


st.markdown(f'#### 👋 1.6 코인별 상관관계 비교, 검증날짜: {formatted_date} 기준')
select_coin2_1 = st.selectbox(
    '▷ 1. 상관계수 비교 -- 기준코인 선택',
    ['all'] + list(data_coin_cr['기준코인'].sort_values(ascending=True).unique())  
)
select_coin2_2 = st.selectbox(
    '▷ 2. 상관계수 비교 -- 비교 대상코인 선택',
    ['all'] + list(data_coin_cr['대상코인'].sort_values(ascending=True).unique())  
)

# 
if  (select_coin2_2 == 'all'):  # (select_coin2_1 == 'all') |
    col1,col2 = st.columns([1,1])
    with col1 :
    st.write(data_coin_cr) 
    with col2 :
    st.write(data_coin_ccf) 
else:
    col1,col2 = st.columns([1,1])
    with col1 : 
    st.write(data_coin_cr[ (data_coin_cr['기준코인']  == select_coin2_1) & (data_coin_cr['대상코인']  == select_coin2_2) ])
    with col2 :
    st.write(data_coin_ccf[ (data_coin_ccf['기준코인']  == select_coin2_1) & (data_coin_ccf['대상코인']  == select_coin2_2) ])
  
select_coin2_3 = st.selectbox(
    '▷ 3. 크로스 비교 지표 선택 (고점/종가/저점) ',
    ['high','close','low']
)

if  (select_coin2_2 == 'all'):  # (select_coin2_1 == 'all') |
    st.write(data_coin_pr.sort_values(by='date', ascending = False)) 
else:
    # st.write(data_coin_cr[ (data_coin_cr['기준코인']  == select_coin2_1) & (data_coin_cr['대상코인']  == select_coin2_2) ])
    data_pr1 = data_coin_pr[ (data_coin_pr['coin']  == select_coin2_1 ) & ( data_coin_pr['구성요소'] == select_coin2_3) ]
    data_pr2 = data_coin_pr[ (data_coin_pr['coin']  == select_coin2_2 ) & ( data_coin_pr['구성요소'] == select_coin2_3) ]

    data_pr3 = pd.merge(data_pr1, data_pr2, on = 'date', how = 'inner')
    data_pr3 = data_pr3.dropna()
   

    data_pr1 = data_pr3[['date','coin_x','가격_x']]
    data_pr2 = data_pr3[['date','coin_y','가격_y']]

    data_pr1['date'] = pd.to_datetime(data_pr1['date'])
    data_pr2['date'] = pd.to_datetime(data_pr2['date'])

    # col1,col2 = st.columns([1,2])
    # with col1 :
    #    st.write(data_pr3.sort_values(by='date', ascending = False)[['date','구성요소_x','coin_x','가격_x','coin_y','가격_y']]) 
    # with col2 :
    # # Streamlit 앱 구성
    # st.title('Crossed Line Charts')
    # # Line Chart 1
    # st.line_chart(data_pr1.set_index('date'))
    # # Line Chart 2
    # st.line_chart(data_pr2.set_index('date'))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # 교차로 그리기
    fig, ax1 = plt.subplots()
    color1 = 'black'
    ax1.set_ylabel(select_coin2_1, color=color1)
    ax1.plot(data_pr1['date'], data_pr1['가격_x'], label = select_coin2_1, color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)
  
    # 두 번째 축 생성
    ax2 = ax1.twinx()
    
    color2 = 'tab:red'
    ax2.set_ylabel(select_coin2_2, color=color2)
    ax2.plot(data_pr2['date'], data_pr2['가격_y'], label = select_coin2_2 , color=color2 )
    ax2.tick_params(axis='y', labelcolor=color2)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='lower left')
    ax1.grid(True)
    # matplotlib 피규어를 Streamlit에 플로팅
    st.pyplot(fig)







st.markdown(f'##### ------------------------------------------------------------------------------------------------------  ')
st.markdown(f'##### ------------------------------------------------------------------------------------------------------  ')




st.markdown(f'## [  KOSPI 200  ] ')

# select_date = st.sidebar.selectbox(
#     '예측일 선택',
#     data_kospi_v['pred_day'].sort_values(ascending=True).unique()
# )
select_date200 = st.selectbox(
    '예측일 선택',
    data_kospi_v['예측일'].sort_values(ascending=True).unique()
)
rule_rank200 = st.selectbox(
    '랭킹룰 선택',
    ['RE_RANK','RE_RANK_UP','NO_UP_HIGH16','NO_UP_HIGH1', ' ']
    # data_coin_v['GRP1'].sort_values(ascending=False).unique()
)
st.markdown(f'#### 2. KOSPI 200 랭킹룰 별 상승률 검증, 검증날짜: {formatted_date} 기준')
# st.write(data_kospi_v[(data_kospi_v['예측일'] == select_date200) & (data_kospi_v['랭킹룰']  == rule_rank200) ])

st.markdown(f'###### 👈 2.1 예측 후 날짜경과별 <시가 대비 고점상승> 비중 및 평균값,  예측날짜: {select_date200} 기준, 랭킹룰 : {rule_rank}')
col1,col2 = st.columns([1,1])
with col1 :
    st.write(data_kospi_v[(data_kospi_v['예측일'] == select_date200) & (data_kospi_v['랭킹룰']  == rule_rank200) ][[
        '랭킹순위구분','1D_고점상승비중','4D_고점상승비중','7D_고점상승비중','12D_고점상승비중']].T )
with col2 :
    st.write(data_kospi_v[(data_kospi_v['예측일'] == select_date200) & (data_kospi_v['랭킹룰']  == rule_rank200) ][[
        '랭킹순위구분', '1D_고점상승평균','4D_고점상승평균','7D_고점상승평균','12D_고점상승평균']].T )

st.markdown(f'###### 👈 2.2 예측 후 날짜경과별 <시가 대비 종가상승> 비중 및 평균값,  예측날짜: {select_date200} 기준, 랭킹룰 : {rule_rank200}')
col3,col4 = st.columns([1,1])
with col3 :
    st.write(data_kospi_v[(data_kospi_v['예측일'] == select_date200) & (data_kospi_v['랭킹룰']  == rule_rank200) ][[
        '랭킹순위구분','1D_종가상승비중','4D_종가상승비중','7D_종가상승비중','12D_종가상승비중']].T )
with col4 :
    st.write(data_kospi_v[(data_kospi_v['예측일'] == select_date200) & (data_kospi_v['랭킹룰']  == rule_rank200) ][[
        '랭킹순위구분','1D_종가상승평균','4D_종가상승평균','7D_종가상승평균','12D_종가상승평균']].T )
    
st.markdown(f'###### 👈 2.3 예측 후 날짜경과별 <시가 대비 저점상승> 비중 및 평균값,  예측날짜: {select_date200} 기준, 랭킹룰 : {rule_rank200}')
col5,col6 = st.columns([1,1])
with col5 :
    st.write(data_kospi_v[(data_kospi_v['예측일'] == select_date200) & (data_kospi_v['랭킹룰']  == rule_rank200) ][[
        '랭킹순위구분','1D_저점상승비중','4D_저점상승비중','7D_저점상승비중','12D_저점상승비중']].T )
with col6 :
    st.write(data_kospi_v[(data_kospi_v['예측일'] == select_date200) & (data_kospi_v['랭킹룰']  == rule_rank200) ][[
        '랭킹순위구분','1D_저점상승평균','4D_저점상승평균','7D_저점상승평균','12D_저점상승평균']].T )




# st.markdown(f'#### 2. KOSPI 200 별 상승률 검증, 검증날짜: {formatted_date} 기준')
# st.write(data_kospi_a[(data_kospi_a['예측일'] == select_date) ])



# st.write(data_coin_v[(data_coin_v['예측일'] == select_date200) & (data_coin_v['랭킹룰']  == rule_rank200) ])

st.markdown(f'#### 👋 2.4 KOSPI 200 별 상승률 검증, 검증날짜: {formatted_date} 기준')
st.write(data_kospi_a[(data_kospi_a['예측일'] == select_date200) ])

st.markdown(f'#### 👋 2.5 KOSPI 200 별 상승률 검증, 검증날짜: {formatted_date} 기준')
select_coin3 = st.selectbox(
    '코스피종목 선택',
    ['all'] + list(data_kospi_a['coin'].sort_values(ascending=True).unique())   # ['a', 'b']
)
select_date3 = st.selectbox(
    '코스피 예측일 선택',
    data_kospi_a['예측일'].sort_values(ascending=False).unique()
)
rule_rank3 = st.selectbox(
    '코스피 랭킹룰 선택',
    ['RE_RANK','RE_RANK_UP','NO_UP_HIGH1','NO_UP_CL16', 'NO_UP_HIGH16', 'NO_UP_LOW16','NO_UP_HCL16','NO_DOWN', 'NO_DOWN_CL16', 'filter1','filter2','filter3', 'filter4', 'filter13']
)
real_uprate3 = st.selectbox(
    '코스피 실제상승률지표 선택',
    ['1D_고점상승비중','4D_고점상승비중','7D_고점상승비중','12D_고점상승비중', '1D_종가상승비중','4D_종가상승비중','7D_종가상승비중','12D_종가상승비중', '1D_저점상승비중','4D_저점상승비중','7D_저점상승비중','12D_저점상승비중', ' ']
)
st.markdown(f'###### 👋 1.5.1 코인별 랭킹패턴 및 상승률 비교,  예측날짜: {select_date3} 기준, 랭킹룰 : {rule_rank3}')
data_kospi_a2 = pd.DataFrame(data_kospi_a)
data_kospi_a_pv2 = pd.pivot_table(data_kospi_a2, values = rule_rank3, index = 'coin', columns = '예측일' , aggfunc = 'first').reset_index() 
data_kospi_a3 = data_kospi_a[ (data_kospi_a['예측일'] == select_date3)][['coin', real_uprate3]]

data_kospi_a_pv2 = pd.merge(data_kospi_a_pv2, data_kospi_a3, left_on='coin', right_on='coin', how='left')
# 순위 부여하기
# data_kospi_a_pv2['rank'] = data_kospi_a_pv2.iloc[:, -1].rank()
data_kospi_a_pv2 = data_kospi_a_pv2.sort_values(by=real_uprate3, ascending = False)

if select_coin3 == 'all':
    st.write(data_kospi_a_pv2)
else:
    st.write(data_kospi_a_pv2[ (data_kospi_a_pv2['coin']  == select_coin3) ])






st.markdown(f'##### ------------------------------------------------------------------------------------------------------  ')
st.markdown(f'##### ------------------------------------------------------------------------------------------------------  ')
st.markdown(f'##### ------------------------------------------------------------------------------------------------------  ')




st.markdown(f'## [  NASDAQ 200  ] ')
# select_date = st.sidebar.selectbox(
#     '예측일 선택',
#     data_nasdaq_v['pred_day'].sort_values(ascending=True).unique()
# )
select_date300 = st.selectbox(
    '예측일 선택',
    data_nasdaq_v['예측일'].sort_values(ascending=True).unique()
)
rule_rank300 = st.selectbox(
    '랭킹룰 선택',
    ['RE_RANK','RE_RANK_UP','NO_UP_HIGH16','NO_UP_HIGH1', ' ' , '  ']
    # data_nasdaq_v['GRP1'].sort_values(ascending=False).unique()
)
st.markdown(f'#### 3. NASDAQ 200 랭킹룰 별 상승률 검증, 검증날짜: {formatted_date} 기준')
# st.write(data_nasdaq_v[(data_nasdaq_v['예측일'] == select_date300) & (data_nasdaq_v['랭킹룰']  == rule_rank300) ])

st.markdown(f'###### 👈 3.1 예측 후 날짜경과별 <시가 대비 고점상승> 비중 및 평균값,  예측날짜: {select_date300} 기준, 랭킹룰 : {rule_rank300}')
col1,col2 = st.columns([1,1])
with col1 :
    st.write(data_nasdaq_v[(data_nasdaq_v['예측일'] == select_date300) & (data_nasdaq_v['랭킹룰']  == rule_rank300) ][[
        '랭킹순위구분','1D_고점상승비중','4D_고점상승비중','7D_고점상승비중','12D_고점상승비중']].T )
with col2 :
    st.write(data_nasdaq_v[(data_nasdaq_v['예측일'] == select_date300) & (data_nasdaq_v['랭킹룰']  == rule_rank300) ][[
        '랭킹순위구분', '1D_고점상승평균','4D_고점상승평균','7D_고점상승평균','12D_고점상승평균']].T )

st.markdown(f'###### 👈 3.2 예측 후 날짜경과별 <시가 대비 종가상승> 비중 및 평균값,  예측날짜: {select_date300} 기준, 랭킹룰 : {rule_rank300}')
col3,col4 = st.columns([1,1])
with col3 :
    st.write(data_nasdaq_v[(data_nasdaq_v['예측일'] == select_date300) & (data_nasdaq_v['랭킹룰']  == rule_rank300) ][[
        '랭킹순위구분','1D_종가상승비중','4D_종가상승비중','7D_종가상승비중','12D_종가상승비중']].T )
with col4 :
    st.write(data_nasdaq_v[(data_nasdaq_v['예측일'] == select_date300) & (data_nasdaq_v['랭킹룰']  == rule_rank300) ][[
        '랭킹순위구분','1D_종가상승평균','4D_종가상승평균','7D_종가상승평균','12D_종가상승평균']].T )
    
st.markdown(f'###### 👈 3.3 예측 후 날짜경과별 <시가 대비 저점상승> 비중 및 평균값,  예측날짜: {select_date300} 기준, 랭킹룰 : {rule_rank300}')
col5,col6 = st.columns([1,1])
with col5 :
    st.write(data_nasdaq_v[(data_nasdaq_v['예측일'] == select_date300) & (data_nasdaq_v['랭킹룰']  == rule_rank300) ][[
        '랭킹순위구분','1D_저점상승비중','4D_저점상승비중','7D_저점상승비중','12D_저점상승비중']].T )
with col6 :
    st.write(data_nasdaq_v[(data_nasdaq_v['예측일'] == select_date300) & (data_nasdaq_v['랭킹룰']  == rule_rank300) ][[
        '랭킹순위구분','1D_저점상승평균','4D_저점상승평균','7D_저점상승평균','12D_저점상승평균']].T )


# st.markdown(f'#### 2. NASDAQ 200 별 상승률 검증, 검증날짜: {formatted_date} 기준')
# st.write(data_nasdaq_a[(data_nasdaq_a['예측일'] == select_date300) ])

st.markdown(f'#### 👋 3.4 NASDAQ 200 별 상승률 검증, 검증날짜: {formatted_date} 기준')
st.write(data_nasdaq_a[(data_nasdaq_a['예측일'] == select_date300) ])

st.markdown(f'#### 👋 3.5 NASDAQ 200 별 상승률 검증, 검증날짜: {formatted_date} 기준')
select_coin4 = st.selectbox(
    '나스닥종목 선택',
    ['all'] + list(data_nasdaq_a['coin'].sort_values(ascending=True).unique())   # ['a', 'b']
)
select_date4 = st.selectbox(
    '나스닥 예측일 선택',
    data_nasdaq_a['예측일'].sort_values(ascending=False).unique()
)
rule_rank4 = st.selectbox(
    '나스닥 랭킹룰 선택',
    ['RE_RANK','RE_RANK_UP','NO_UP_HIGH1','NO_UP_CL16', 'NO_UP_HIGH16', 'NO_UP_LOW16','NO_UP_HCL16','NO_DOWN', 'NO_DOWN_CL16', 'filter1','filter2','filter3', 'filter4', 'filter13', ' ']
)
real_uprate4 = st.selectbox(
    '나스닥 실제상승률지표 선택',
    ['1D_고점상승비중','4D_고점상승비중','7D_고점상승비중','12D_고점상승비중', '1D_종가상승비중','4D_종가상승비중','7D_종가상승비중','12D_종가상승비중', '1D_저점상승비중','4D_저점상승비중','7D_저점상승비중','12D_저점상승비중', ' ', ' ']
)
st.markdown(f'###### 👋 1.5.1 나스닥 종목 별 랭킹패턴 및 상승률 비교,  예측날짜: {select_date4} 기준, 랭킹룰 : {rule_rank4}')
data_nasdaq_a2 = pd.DataFrame(data_nasdaq_a)
data_nasdaq_a_pv2 = pd.pivot_table(data_nasdaq_a2, values = rule_rank4, index = 'coin', columns = '예측일' , aggfunc = 'first').reset_index() 
data_nasdaq_a3 = data_nasdaq_a[ (data_nasdaq_a['예측일'] == select_date4)][['coin', real_uprate4]]

data_nasdaq_a_pv2 = pd.merge(data_nasdaq_a_pv2, data_nasdaq_a3, left_on='coin', right_on='coin', how='left')
# 순위 부여하기
# data_nasdaq_a_pv2['rank'] = data_nasdaq_a_pv2.iloc[:, -1].rank()
data_nasdaq_a_pv2 = data_nasdaq_a_pv2.sort_values(by=real_uprate4, ascending = False)

if select_coin4 == 'all':
    st.write(data_nasdaq_a_pv2)
else:
    st.write(data_nasdaq_a_pv2[ (data_nasdaq_a_pv2['coin']  == select_coin4) ])






st.markdown(f'##### ------------------------------------------------------------------------------------------------------  ')
st.markdown(f'##### ------------------------------------------------------------------------------------------------------  ')
st.markdown(f'##### ------------------------------------------------------------------------------------------------------  ')





