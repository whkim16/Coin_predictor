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
import time
 



## 보이기 
# hide_streamlit_style = """
#             <style>
#             MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             GithubIcon {visibility: hidden;}
#             #header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# 숨기기 
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            #footer {visibility: hidden;}
            GithubIcon {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# 현재 날짜 가져오기
today = datetime.today()
# 날짜를 문자열로 변환하여 포매팅
formatted_date = today.strftime("%Y-%m-%d")


st.title("비트코인 일(Day)예측 대시보드")
st.markdown(f'#### [비트코인, {formatted_date} 👈 예측결과 ] ')

st.markdown(f'##### ※ 💡 주의 사항  ')
st.markdown(f'######  - 본 서비스는 정보제공 목적으로만 서비스를 제공하며 이용자에게 투자권유, 매매권유 및 제안 등을 일체 하지 않습니다.')
st.markdown(f'######    따라서 투자/매매 등 모든 책임은 투자자(이용자) 본인에게 있으며 본 서비스 제공자는 아무 관련(책임)이 없습니다.')

st.markdown(f'######  - 과거 데이터를 기반으로 일별(Day) 상승/하락 확률을 예측하는 모형이며 예측결과가 100% 정확성을 보장하지 않습니다.')
st.markdown(f'######  - 외부충격(예, 질병 코로나, 전쟁이슈 등)이 반영되지 않는 기술적 분석에 초점이 맞춰져 있는 예측모형입니다.')

st.markdown(f'######   (코인거래소 Upbit 기준 오전 9시 기준 예측 수행결과)')



st.sidebar.title("Coin Chart")
st.sidebar.markdown('비트/알트코인 Link : [All Coin Symbols](https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC)')
st.sidebar.markdown('코스피200 Link : [All Kospi200 Symbols](https://finance.naver.com/sise/sise_index.nhn?code=KPI200)')
st.sidebar.markdown('나스닥200 Link : [All Nasdaq200 Symbols](https://kr.investing.com/indices/nq-100-components)')









# GitHub에서 Raw 형태의 데이터 URL
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_web_Day_v3.csv'
# 데이터 불러오기
data = pd.read_csv(data_url, encoding='CP949')

data1 = data[data['GRP'] == 'Set1'][['pred_day', 'coin', 'RE_RANK', 'RE_RANK_UP', 
                                     'filter1', 'filter2', 'filter3', 'filter4',
                                     'filter13', 'filter14',
                    'NO_UP_HIGH1', 'NO_UP_CL16', 'NO_UP_HIGH16', 'NO_UP_LOW16', 'NO_UP_HCL16',
                      'NO_DOWN', 'NO_DOWN_CL16',  'NO_DOWN_LOW16',                     
                      'filter5', 'filter6', 'filter7', 'filter8',
                      'filter9', 'filter10', 'filter11', 'filter12'
                      ]].dropna()
data3 = data[data['GRP'] == 'Set3'][['pred_day', 'coin', 'SEQ', 'date', 'close_up', 'high_up', 'low_up' ]].dropna()
data9 = data[data['GRP'] == 'Set9'][['pred_day', 'coin', 'MSG8', 'MSG9' ]]


st.markdown(f'######     ')
st.markdown(f'###### 👈 아래 필터 사용법 : 예측수행일은 모델이 결과를 도출한 날짜를 의미함    ')
st.markdown(f'######       (예를들어, 05-05 Day 상승/하락이 궁금하다면 05-04 Day 를 선택하면 됨)   ')
st.markdown(f'######     ')
select_date = st.selectbox(
    '👈 예측수행일 선택하세요 ',
    data3['pred_day'].sort_values(ascending=False).unique()
)

st.markdown(f'######     ')

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_coin = st.selectbox(
    '👈 Coin Symbol 선택하세요 ',
    # data4['coin'].sort_values(ascending=True).unique()
    ['BTC'] + list(data1[(data1['pred_day'] == select_date) ].sort_values(by='RE_RANK', ascending=True).coin.unique())
)
st.markdown(f'######     ')

data1 = data1.rename(columns={'RE_RANK': '추천순서1'})
data1 = data1.rename(columns={'RE_RANK_UP': '추천순서2'})
data1 = data1.rename(columns={'pred_day': '예측일'})
data1.index = [''] * len(data1)

data3 = data3.rename(columns={'pred_day': '예측일'})
data3 = data3.rename(columns={'close_up': '종가상승확률'})
data3 = data3.rename(columns={'high_up': '고점갱신확률'})
data3 = data3.rename(columns={'low_up': '저점상승확률'})

data9 = data9.rename(columns={'pred_day': '예측일'})

# 💻 🧠 👋 👈
st.markdown(f'#### 💻 비트코인 예측일 :  {select_date} 👈 9시 기준, 예측결과 ')

st.markdown(f'###### 👈 [상승확률 높은 코인 1] ')
data1__1 = data1[(data1['예측일'] == select_date) & (data1['filter1'] >= 45 ) & 
                 (data1['filter3'] >= 45 ) & (data1['filter4'] >= 45 ) ].sort_values(by='추천순서1', ascending=True)
# 'c' 컬럼에서 상위 15개 값 출력
data1__1 = data1__1['coin']#.head(15)
new_index = np.arange(1, len(data1__1)+1)
data1__1.index = new_index
st.write(data1__1.to_frame().T )

st.markdown(f'###### 👈 [상승확률 높은 코인 2] ')
data1__1 = data1[(data1['예측일'] == select_date) & (data1['filter1'] >= 40 ) & 
                 (data1['filter3'] >= 40 ) & (data1['filter4'] >= 40 ) ].sort_values(by='추천순서1', ascending=True)
# 'c' 컬럼에서 상위 15개 값 출력
data1__1 = data1__1['coin']#.head(15)
new_index = np.arange(1, len(data1__1)+1)
data1__1.index = new_index
st.write(data1__1.to_frame().T )




data3_1 = data3[ (data3['coin'] == select_coin)  & (data3['예측일']==select_date)  &  (data3['SEQ'] == 1)]
data9_1 = data9[ (data9['coin'] == select_coin)  & (data9['예측일']==select_date) ]


a = data3_1['종가상승확률'].unique()
b = data3_1['고점갱신확률'].unique()
c = data3_1['저점상승확률'].unique()
d = data9_1['MSG8'].unique()
e = data9_1['MSG9'].unique()

st.markdown(f'##### 👋 익일 종가 상승확률 : {a}  ')
st.markdown(f'###### ▷. 익일 종가 {d} ')
st.markdown(f'##### 👋 익일 고점 상승확률 : {b}  ')
st.markdown(f'##### 👋 익일 저점 상승확률 : {c}  ')



st.markdown(f'###### ▷. {e} ')

st.markdown(f'######    ※ 💡 확률 수치 참고  ')
# st.markdown(f'######    - 상승확률 100 ~ 77% 인 경우 상승가능성 매우 높음  ')
# st.markdown(f'######    - 상승확률 76 ~ 59% 인 경우 상승가능성 높음  ')
# st.markdown(f'######    - 상승확률 58 ~ 40% 인 경우 중립(전날 종가 유사)  ')
# st.markdown(f'######    - 상승확률 39 ~ 21% 인 경우 하락가능성 높음  ')
# st.markdown(f'######    - 상승확률 20 ~ 0% 이상인 경우 하락가능성 매우 높음  ')

st.markdown(f'######    - 100 ~ 77% (상승가능성 매우 높음)  ')
st.markdown(f'######    - 76 ~ 59% (상승가능성 높음)  ')
st.markdown(f'######    - 58 ~ 40% (중립(전날 종가 유사))  ')
st.markdown(f'######    - 39 ~ 21% (하락가능성 높음)  ')
st.markdown(f'######    - 20 ~ 0% (하락가능성 매우 높음)  ')


data4 = data[data['GRP'] == 'Set4' ][['GRP', 'pred_day', 'coin', 'SEQ', 'date', 'variable', 'value_close', 'value_high', 'value_low', 'LOW_VL', 'HIGH_VL', 'CL_VL']]

data4 = data4.rename(columns={'pred_day': '예측일'})
data4_1 = data4[(  ( (data4['coin'] == select_coin) ) ) & (data4['예측일'] == select_date) ]
data4_2 = data3[ (data3['coin'] == select_coin)  & (data3['예측일'] == select_date)  &  (data3['SEQ'] <= 1) ][['예측일','coin','종가상승확률','고점갱신확률','저점상승확률']]





data4_1CLx = data4_1[data4_1['variable'] == 'Pred1'][['date']]
data4_1CLx = list(range(1, len(data4_1CLx.date)+1)) 

data4_1CLy0 = data4_1[data4_1['variable'] == 'Pred0'][['value_close']]

data4_1CLy = data4_1[data4_1['variable'] == 'Pred1'][['value_close']]

data4_2CLy = data4_1[data4_1['variable'] == 'Pred2'][['value_close']]
data4_3CLy = data4_1[data4_1['variable'] == 'Pred6'][['value_close']]
data4_4CLy = data4_1[data4_1['variable'] == 'Pred7'][['value_close']]
data4_5CLy = data4_1[data4_1['variable'] == 'Pred9'][['value_close']]
data4_6CLy = data4_1[data4_1['variable'] == 'Pred12'][['value_close']]
data4_7CLy = data4_1[data4_1['variable'] == 'Pred15'][['value_close']]
data4_8CLy = data4_1[data4_1['variable'] == 'Pred18'][['value_close']]
data4_9CLy = data4_1[data4_1['variable'] == 'Pred21'][['value_close']]
data4_10CLy = data4_1[data4_1['variable'] == 'Pred24'][['value_close']]
data4_11CLy = data4_1[data4_1['variable'] == 'Pred27'][['value_close']]
data4_12CLy = data4_1[data4_1['variable'] == 'Pred33'][['value_close']] #
data4_13CLy = data4_1[data4_1['variable'] == 'Pred34'][['value_close']] #
data4_14CLy = data4_1[data4_1['variable'] == 'Pred37'][['value_close']]
data4_15CLy = data4_1[data4_1['variable'] == 'Pred52'][['value_close']] # 

data4_1Hhy0 = data4_1[data4_1['variable'] == 'Pred0'][['value_high']]

data4_1Hhy = data4_1[data4_1['variable'] == 'Pred1'][['value_high']]
data4_2Hhy = data4_1[data4_1['variable'] == 'Pred2'][['value_high']]
data4_3Hhy = data4_1[data4_1['variable'] == 'Pred6'][['value_high']]
data4_4Hhy = data4_1[data4_1['variable'] == 'Pred7'][['value_high']]
data4_5Hhy = data4_1[data4_1['variable'] == 'Pred9'][['value_high']]
data4_6Hhy = data4_1[data4_1['variable'] == 'Pred12'][['value_high']]
data4_7Hhy = data4_1[data4_1['variable'] == 'Pred15'][['value_high']]
data4_8Hhy = data4_1[data4_1['variable'] == 'Pred18'][['value_high']]
data4_9Hhy = data4_1[data4_1['variable'] == 'Pred21'][['value_high']]
data4_10Hhy = data4_1[data4_1['variable'] == 'Pred24'][['value_high']]
data4_11Hhy = data4_1[data4_1['variable'] == 'Pred27'][['value_high']]
data4_12Hhy = data4_1[data4_1['variable'] == 'Pred33'][['value_high']] #
data4_13Hhy = data4_1[data4_1['variable'] == 'Pred34'][['value_high']] #
data4_14Hhy = data4_1[data4_1['variable'] == 'Pred37'][['value_high']]
data4_15Hhy = data4_1[data4_1['variable'] == 'Pred52'][['value_high']] # 

data4_1Lwy0 = data4_1[data4_1['variable'] == 'Pred0'][['value_low']]

data4_1Lwy = data4_1[data4_1['variable'] == 'Pred1'][['value_low']]
data4_2Lwy = data4_1[data4_1['variable'] == 'Pred2'][['value_low']]
data4_3Lwy = data4_1[data4_1['variable'] == 'Pred6'][['value_low']]
data4_4Lwy = data4_1[data4_1['variable'] == 'Pred7'][['value_low']]
data4_5Lwy = data4_1[data4_1['variable'] == 'Pred9'][['value_low']]
data4_6Lwy = data4_1[data4_1['variable'] == 'Pred12'][['value_low']]
data4_7Lwy = data4_1[data4_1['variable'] == 'Pred15'][['value_low']]
data4_8Lwy = data4_1[data4_1['variable'] == 'Pred18'][['value_low']]
data4_9Lwy = data4_1[data4_1['variable'] == 'Pred21'][['value_low']]
data4_10Lwy = data4_1[data4_1['variable'] == 'Pred24'][['value_low']]
data4_11Lwy = data4_1[data4_1['variable'] == 'Pred27'][['value_low']]
data4_12Lwy = data4_1[data4_1['variable'] == 'Pred33'][['value_low']] #
data4_13Lwy = data4_1[data4_1['variable'] == 'Pred34'][['value_low']] #
data4_14Lwy = data4_1[data4_1['variable'] == 'Pred37'][['value_low']]
data4_15Lwy = data4_1[data4_1['variable'] == 'Pred52'][['value_low']] # 



st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown(f'######     ')
st.markdown(f'#### 🧠 예측 시각화 차트 (D-4 조회가능)')
st.markdown(f'######     ')


data4_2.index = [''] * len(data4_2)
st.write(data4_2)
    
    
    
st.markdown(f'#####    ※ 💡 시각화 차트 해석  ')
st.markdown(f'######   👈 시각화는 참고용으로 보시고 위 상승/하락 확률을 메인으로 정보파악 필요! ')
st.markdown(f'######  - 빨간 수직선 : 예측결과 도출한 날을 의미  ')
st.markdown(f'######  - 빨간 수직선 좌측 : 실제 비트코인 차트결과  ')
st.markdown(f'######  - 빨간 수직선 우측 : 6일치 비트코인 예측결과  ')
st.markdown(f'######  - 실선 : 종가 예측결과 (여러패턴 가능성 시각화)  ')
st.markdown(f'######  - 점선 : 고점/저점 예측결과 (여러패턴 가능성 시각화)  ')
st.markdown(f'######     ')
   
    
    
    
    
    
    
    
    

fig, ax = plt.subplots()
ax.plot(data4_1CLx, data4_1CLy['value_close'], linestyle='-', marker='None', color='white', linewidth=1)
ax.set_ylim(np.min(data4_1CLy['value_close']), np.max(data4_1CLy['value_close']))
ax.set_ylim(np.min(data4_1CLy['value_close'])*0.92, np.max(data4_1CLy['value_close'])*1.08)
ax.set_facecolor('#e0ffff')

# # Plotting additional points
ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_2CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1.5)
ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_12CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1.5)
ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_13CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1.5)
ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_15CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1.5)

ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_3CLy.value_close)), linestyle='-', marker='None', color='blue', linewidth=1.5)
ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_4CLy.value_close)), linestyle='-', marker='None', color='blue', linewidth=1.5)
ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_5CLy.value_close)), linestyle='-', marker='None', color='blue', linewidth=1.5)
ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_6CLy.value_close)), linestyle='-', marker='None', color='blue', linewidth=1.5)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_7CLy.value_close)), linestyle='-', marker='None', color='green', linewidth=1.5)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_8CLy.value_close)), linestyle='-', marker='None', color='green', linewidth=1.5)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_9CLy.value_close)), linestyle='-', marker='None', color='green', linewidth=1.5)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_10CLy.value_close)), linestyle='-', marker='None', color='green', linewidth=1.5)


ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_2Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_12Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_13Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_15Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)

ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_3Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_4Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_5Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_6Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_7Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_8Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_9Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_10Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)

ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_2Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_12Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_13Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_15Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)

ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_3Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_4Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_5Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_6Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_7Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_8Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_9Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
# ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_10Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)

date_format = mdates.DateFormatter('%Y-%m-%d')  # 날짜 형식 지정
ax.xaxis.set_major_locator(mdates.DayLocator())  # 일 단위로 눈금 표시
ax.xaxis.set_major_formatter(date_format)

# # x축 라벨을 세로로 변환
ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='right')
ax.set_xlabel("date")
ax.set_ylabel("low ~ high range")
ax.set_title(f' BTC Coin , 6 day predict date:  {select_date} ')  # (f' 예측날짜:  {select_date} 9시 기준')
# plt.xticks([])  # Disable x-axis ticks
# plt.yticks([])  # Disable y-axis ticks
ax.grid(True)
ax.axvline(x=data4_1CLx[(len(data4_1CLx) - 7)], color='red', linestyle='dashed', linewidth=4)

ax.tick_params(axis='both', which='both', length=1, width=0.5)

ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1CLy.value_close[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
ax.plot(data4_1CLx[:(len(data4_1CLy0.value_close))], (data4_1CLy0.value_close), linestyle='-', marker='*', color='black', linewidth=2)

ax.plot(data4_1CLx[:(len(data4_1Hhy0.value_high))], (data4_1Hhy0.value_high), linestyle='--', marker='*', color='black', linewidth=1)
ax.plot(data4_1CLx[:(len(data4_1Lwy0.value_low))], (data4_1Lwy0.value_low), linestyle='--', marker='*', color='black', linewidth=1)


# plt.show()
st.pyplot(fig)
