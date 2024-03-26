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





hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            #footer {visibility: hidden;}
            GithubIcon {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# st.code("""
# [theme]
# primaryColor="#F39C12"
# backgroundColor="#81F7D8"
# # secondaryBackgroundColor="#AED6F1"
# # textColor="#FFFFFF"
# # font="monospace"
# """)


# if user_name != '':
#   st.write(f'👋 안녕하세요 {user_name}님!')
# else:
#   st.write('👈  **이름**을 입력해 주세요!')

# my_bar = st.progress(0)
# for percent_complete in range(100):
#      time.sleep(0.05)
#      my_bar.progress(percent_complete + 1)

# st.balloons()

# st.title('this is title')
# st.header('this is header')
# st.subheader('this is subheader'


# 현재 날짜 가져오기
today = datetime.today()

# 날짜를 문자열로 변환하여 포매팅
formatted_date = today.strftime("%Y-%m-%d")

# Streamlit Markdown에 날짜 추가
st.title("S I M U L A T I O N , C O I N ")
st.markdown(f'### 1. R E C O M M E N D, 예 측 날 짜: {formatted_date} 00시 기준')
# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title("C H A R T")
# st.sidebar.markdown('비트/알트코인 Link : [All Coin Symbols](https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC)')
# st.sidebar.markdown('코스피200 Link : [All Kospi200 Symbols](https://finance.naver.com/sise/sise_index.nhn?code=KPI200)')
# st.sidebar.markdown('나스닥200 Link : [All Nasdaq200 Symbols](https://kr.investing.com/indices/nq-100-components)')


import streamlit as st
import pandas as pd
 


# text_input = st.sidebar.text_input(" [ 암호를 입력하세요 ] ", 0) 

# st.write(st.secrets["my_secrets"]["secret_code"][0])
# st.write("My secrets:", st.secrets["my_secrets"]["secret_code"])






# GitHub에서 Raw 형태의 데이터 URL
data_url = 'https://raw.githubusercontent.com/whkim16/Coin_predictor/main/C%3A/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_web_Day_v3_BTB.csv'

# 데이터 불러오기
data = pd.read_csv(data_url)

# # Streamlit 앱 내에서 데이터 활용
# st.write(data)
    
# uploaded_file = st.file_uploader(
#     'C:/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_web_Day_v3.csv', accept_multiple_files=False)
# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file, encoding='CP949')
#     # data = data.sort_values(by='RE_RANK', ascending=True)
# else:
#     st.error("File not found. Please check the file path.")
    
    
# try:
#     data = pd.read_csv('https://drive.google.com/file/d/1ZT6Gi3NEMJgbb00P5ZhlF1vP2Xlfcd4u/view?usp=drive_link', encoding='CP949')
#     data = data.sort_values(by='RE_RANK', ascending=True)
#     st.write(data)
# except FileNotFoundError:
#     st.error("File not found. Please check the file path.")
    
#ticker 종목의 시작~종료 날짜 사이의 가격변화를 데이터로 보여줌
# data = pd.read_csv('C:/Users/woohy/Desktop/predict_btc/PT_ALL/rank/coin_rank_DAY_2024021009_v3.csv', encoding='CP949') # , encoding='utf-8' , thousands = ','   .str.replace(',', '').astype('int64')
# data = data.sort_values(by='RE_RANK', ascending=True)
# read.csv( paste0("C:/Users/woohy/Desktop/predict_btc/PT_ALL/rank/coin_rank_DAY_2024021009_v3.csv")

# selected_columns1 = ['pred_day', 'coin', 'RE_RANK', 'RE_RANK_UP', 
#                     'NO_UP_HIGH1', 'NO_UP_CL16', 'NO_UP_HIGH16', 'NO_UP_LOW16', 'NO_UP_HCL16',
#                       'NO_DOWN', 'NO_DOWN_CL16',  'NO_DOWN_LOW16',
#                       'filter1', 'filter2', 'filter3', 'filter4',
#                       'filter5', 'filter6', 'filter7', 'filter8',
#                       'filter9', 'filter10', 'filter11', 'filter12',
#                       'filter13', 'filter14']
data1 = data[data['GRP'] == 'Set1'][['pred_day', 'coin', 'RE_RANK', 'RE_RANK_UP', 
                                     'filter1', 'filter2', 'filter3', 'filter4',
                                     'filter13', 'filter14',
                    'NO_UP_HIGH1', 'NO_UP_CL16', 'NO_UP_HIGH16', 'NO_UP_LOW16', 'NO_UP_HCL16',
                      'NO_DOWN', 'NO_DOWN_CL16',  'NO_DOWN_LOW16',                     
                      'filter5', 'filter6', 'filter7', 'filter8',
                      'filter9', 'filter10', 'filter11', 'filter12'
                      ]].dropna()


# selected_columns3 = ['pred_day', 'coin', 'SEQ', 'date', 'close_up', 'high_up', 'low_up' ]
data3 = data[data['GRP'] == 'Set3'][['pred_day', 'coin', 'SEQ', 'date', 'close_up', 'high_up', 'low_up' ]].dropna()




# ticker = st.sidebar.text_input("Enter a Coin (e. g. BTC)", value = 'BTC')



select_date = st.sidebar.selectbox(
    'Select Date',
    data1['pred_day'].sort_values(ascending=False).unique()
)

data1 = data1.rename(columns={'RE_RANK': '추천순서1'})
data1 = data1.rename(columns={'RE_RANK_UP': '추천순서2'})
data1 = data1.rename(columns={'pred_day': '예측일'})

data1.index = [''] * len(data1)

# new_index = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]
# col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])



col1,col2,col3 = st.columns([1,1,1])
with col1 :
    values01 = st.slider('고점 상승예측모델 필터', 0, 51, (20, 51))
with col2 :
    values02 = st.slider('종가 상승예측모델 필터', 0, 51, (20, 51))
with col3 :
    values03 = st.slider('저점 상승예측모델 필터', 0, 51, (20, 51))


# st.write(data1)


st.markdown(f'###### 👈 [종합 추 천 순 서 1] ')
data1__1 = data1[(data1['예측일'] == select_date) & (data1['filter1'] >= min(values01) ) & (data1['filter1'] <= max(values01) ) &
            (data1['filter3'] >= min(values03) ) & (data1['filter3'] <= max(values03) ) &
            (data1['filter4'] >= min(values02) ) & (data1['filter4'] <= max(values02) ) ].sort_values(by='추천순서1', ascending=True)
# 'c' 컬럼에서 상위 15개 값 출력
data1__1 = data1__1['coin']#.head(15)
new_index = np.arange(1, len(data1__1)+1)
data1__1.index = new_index
st.write(data1__1.to_frame().T )

st.markdown(f'###### 👈 [종합 추 천 순 서 2] ')
data1__2 = data1[(data1['예측일'] == select_date) & (data1['filter1'] >= min(values01) ) & (data1['filter1'] <= max(values01) ) &
            (data1['filter3'] >= min(values03) ) & (data1['filter3'] <= max(values03) ) &
            (data1['filter4'] >= min(values02) ) & (data1['filter4'] <= max(values02) )].sort_values(by='추천순서2', ascending=True)
# 'c' 컬럼에서 상위 15개 값 출력
data1__2 = data1__2['coin']#.head(15)
new_index = np.arange(1, len(data1__2)+1)
data1__2.index = new_index
# st.write(data1__2 )

# 선택한 열 값을 행으로 표시
st.write(data1__2.to_frame().T )

st.markdown(f'###### 👈 [익일 고점상승 예상 순위] ')
data1__3 = data1[(data1['예측일'] == select_date) & (data1['filter1'] >= min(values01) ) & (data1['filter1'] <= max(values01) ) &
            (data1['filter3'] >= min(values03) ) & (data1['filter3'] <= max(values03) ) &
            (data1['filter4'] >= min(values02) ) & (data1['filter4'] <= max(values02) )].sort_values(by='filter1', ascending=False)
# 'c' 컬럼에서 상위 15개 값 출력
data1__3 = data1__3['coin']#.head(15)
new_index = np.arange(1, len(data1__3)+1)
data1__3.index = new_index
st.write(data1__3.to_frame().T )

st.markdown(f'###### 👈 [익일 고점상승 확률높은 순위] ')
data1__4 = data1[(data1['예측일'] == select_date) & (data1['filter1'] >= min(values01) ) & (data1['filter1'] <= max(values01) ) &
            (data1['filter3'] >= min(values03) ) & (data1['filter3'] <= max(values03) ) &
            (data1['filter4'] >= min(values02) ) & (data1['filter4'] <= max(values02) )].sort_values(by='filter13', ascending=False)
# 'c' 컬럼에서 상위 15개 값 출력
data1__4 = data1__4['coin']#.head(15)
new_index = np.arange(1, len(data1__4)+1)
data1__4.index = new_index
st.write(data1__4.to_frame().T )


st.markdown(f'###### 👈 [익일 저점상승 예상 순위] ')
data1__5 = data1[(data1['예측일'] == select_date) & (data1['filter1'] >= min(values01) ) & (data1['filter1'] <= max(values01) ) &
            (data1['filter3'] >= min(values03) ) & (data1['filter3'] <= max(values03) ) &
            (data1['filter4'] >= min(values02) ) & (data1['filter4'] <= max(values02) )].sort_values(by='filter3', ascending=False)
# 'c' 컬럼에서 상위 15개 값 출력
data1__5 = data1__5['coin']#.head(15)
new_index = np.arange(1, len(data1__5)+1)
data1__5.index = new_index
st.write(data1__5.to_frame().T )


st.markdown(f'###### ------------------------------------------------------- ')


# 'NO_DOWN', 'NO_DOWN_CL16',  'NO_DOWN_LOW16',    
st.markdown(f'###### 👈 [익일 하락 예상 순위 - 1] ')
data1__6 = data1[(data1['예측일'] == select_date) ].sort_values(by='NO_DOWN', ascending=False)
# 'c' 컬럼에서 상위 15개 값 출력
data1__6 = data1__6['coin']#.head(15)
new_index = np.arange(1, len(data1__6)+1)
data1__6.index = new_index
st.write(data1__6.to_frame().T )


st.markdown(f'###### 👈 [하락추세 예상 순위 - 2] ')
data1__7 = data1[(data1['예측일'] == select_date) ].sort_values(by='NO_DOWN_CL16', ascending=False)
# 'c' 컬럼에서 상위 15개 값 출력
data1__7 = data1__7['coin']#.head(15)
new_index = np.arange(1, len(data1__7)+1)
data1__7.index = new_index
st.write(data1__7.to_frame().T )


st.markdown(f'###### 👈 [저점하락 예상 순위 - 3] ')
data1__8 = data1[(data1['예측일'] == select_date) ].sort_values(by='NO_DOWN_LOW16', ascending=False)
# 'c' 컬럼에서 상위 15개 값 출력
data1__8 = data1__8['coin']#.head(15)
new_index = np.arange(1, len(data1__8)+1)
data1__8.index = new_index
st.write(data1__8.to_frame().T )



st.markdown(f'###### ------------------------------------------------------- ')
st.markdown(f'###### ------------------------------------------------------- ')


st.markdown(f'##### {formatted_date} 기준, 전체 랭 킹 표 ')
values = st.slider('Select a range of values', 0, len(data1['coin'].unique()), (1, 10))

st.write(data1[(data1['예측일'] == select_date) &  (data1['추천순서1'] >= min(values)) & (data1['추천순서1'] <= max(values)) &
            (data1['filter1'] >= min(values01) ) & (data1['filter1'] <= max(values01) ) &
            (data1['filter3'] >= min(values03) ) & (data1['filter3'] <= max(values03) ) &
            (data1['filter4'] >= min(values02) ) & (data1['filter4'] <= max(values02) ) ] )

st.markdown(f'### 2. C O I N (다중), 예 측 날 짜: {formatted_date} 00시 기준')
# 여러개 선택할 수 있을 때는 multiselect를 이용하실 수 있습니다 
# return : list
select_multi_coin = st.multiselect(   # st.sidebar.multiselect(
    '👈 Select Coin Symbols For #2,3',
    # data1['coin'].sort_values(ascending=True).unique()
    data1[(data1['예측일'] == select_date) ].sort_values(by='추천순서1', ascending=True).coin.unique()
)



# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
data2 = data1[(data1['coin'].isin(select_multi_coin))  & (data1['예측일']==select_date)  ]
data2['추천순서1'] = data2['추천순서1'].astype(int)
data2['추천순서2'] = data2['추천순서2'].astype(int)

# 선택한 종들의 결과표를 나타냅니다.  
# st.header("Multi Select Coin Data Chart")



data2.index = [''] * len(data2)
st.write(data2)


seqs = st.slider('Select a range of Predict', 0, 6, (0, 1))



data3 = data3.rename(columns={'pred_day': '예측일'})
data3 = data3.rename(columns={'close_up': '종가상승확률'})
data3 = data3.rename(columns={'high_up': '고점갱신확률'})
data3 = data3.rename(columns={'low_up': '저점상승확률'})

# 
# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
data3_1 = data3[ (data3['coin'].isin(select_multi_coin))  & (data3['예측일']==select_date)  &  (data3['SEQ'] >= min(seqs)) & (data3['SEQ'] <= max(seqs))]
st.markdown(f'### 3. B U Y or S E L L , 예측날짜:  {formatted_date} 00시 기준')

data3_1.index = [''] * len(data3_1)

st.markdown(f'###### 예 측 일 :  {select_date}, 예 측 건 수 : 1 ~ {max(seqs)} ')

st.write(data3_1[[ 'date','coin', 'SEQ', '종가상승확률','고점갱신확률','저점상승확률']])



# st.sidebar 를 통해 사이드바를 생성하고 내용을 넣을 수 있음.
# st.sidebar.text_input : 사이드바에 텍스트를 입력할 수 있는 요소를 만듦
# st.sidebar.date_input : 사이드바에 날짜를 입력할 수 있는 요소를 만듦

# c("Pred1", "Pred2","Pred6", "Pred7","Pred9", "Pred12","Pred15",
#                                  "Pred18","Pred21", "Pred24","Pred27", "Pred33","Pred34", "Pred37","Pred52")





data4 = data[data['GRP'] == 'Set4' ][['GRP', 'pred_day', 'coin', 'SEQ', 'date', 'variable', 'value_close', 'value_high', 'value_low', 'LOW_VL', 'HIGH_VL', 'CL_VL']]

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_coin = st.selectbox(
    '👈 Select Coin Symbols For #4',
    # data4['coin'].sort_values(ascending=True).unique()
    data1[(data1['예측일'] == select_date) ].sort_values(by='추천순서1', ascending=True).coin.unique()
)

data4 = data4.rename(columns={'pred_day': '예측일'})
# (data4['coin'].isin(select_multi_coin)) |
data4_1 = data4[(  ( (data4['coin'] == select_coin) ) ) & (data4['예측일'] == select_date) ]

data4_2 = data3[ (data3['coin'] == select_coin)  & (data3['예측일'] == select_date)  &  (data3['SEQ'] <= 1) ][['예측일','coin','종가상승확률','고점갱신확률','저점상승확률']]





data4_1CLx = data4_1[data4_1['variable'] == 'Pred1'][['date']]
# data4_1CLx = ['2024-' + text[:5] for text in data4_1CLx.date ] 
data4_1CLx = list(range(1, len(data4_1CLx.date)+1)) 

# data4_1CLx = pd.to_datetime(data4_1CLx)


# ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1CLy.value_close[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
# ax.plot(data4_1CLx[:(len(data4_1CLy0.value_close))], (data4_1CLy0.value_close), linestyle='-', marker='*', color='black', linewidth=2)

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

# st.header("Single Select Coin Data")
st.markdown(f'### 4. C O I N , 예 측 날 짜:  {select_date} 기준')
st.markdown(f'###### {formatted_date} 기준, 6일 전 데이터까지만 조 회 가 능')


# close_up = data4_2['close_up'].values
# high_up = data4_2['high_up'].values
# low_up = data4_2['low_up'].values

# data4_2.close_up, data4_2.high_up, data4_2.low_up
# st.markdown(f'#### {select_coin} , 6 day predict date:  {select_date} {close_up, high_up, low_up}')

data4_2.index = [''] * len(data4_2)
st.write(data4_2)
    
    
    
    

    
    
    
    
    
    
    
    
    
col1,col2 = st.columns([1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

with col1 :
# column 1 에 담을 내용
# Plotting the first set of points
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
    ax.set_title(f'{select_coin} , 6 day predict date:  {select_date} ')  # (f' 예측날짜:  {select_date} 9시 기준')
    # plt.xticks([])  # Disable x-axis ticks
    # plt.yticks([])  # Disable y-axis ticks
    ax.grid(True)
    ax.axvline(x=data4_1CLx[(len(data4_1CLx) - 7)], color='red', linestyle='dashed', linewidth=4)
    
    ax.tick_params(axis='both', which='both', length=1, width=0.5)
    
    ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1CLy.value_close[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
    # ax.plot(data4_1CLx[:(len(data4_1CLy0.value_close))], (data4_1CLy0.value_close), linestyle='-', marker='*', color='black', linewidth=2)
    
    ax.plot(data4_1CLx[:(len(data4_1Hhy0.value_high))], (data4_1Hhy0.value_high), linestyle='--', marker='*', color='black', linewidth=1)
    ax.plot(data4_1CLx[:(len(data4_1Lwy0.value_low))], (data4_1Lwy0.value_low), linestyle='--', marker='*', color='black', linewidth=1)


    # plt.show()
    st.pyplot(fig)



with col2 :
  # column 2 에 담을 내용
    fig, ax = plt.subplots()
    ax.plot(data4_1CLx, data4_1CLy['value_close'], linestyle='-', marker='None', color='white', linewidth=1)
    ax.set_ylim(np.min(data4_1CLy['value_close'])*0.92, np.max(data4_1CLy['value_close'])*1.08)
    
    
    # # Plotting additional points
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_2CLy.value_close)), linestyle='-', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_12CLy.value_close)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_13CLy.value_close)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_15CLy.value_close)), linestyle='--', marker='None', color='red', linewidth=1)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_3CLy.value_close)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_4CLy.value_close)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_5CLy.value_close)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_6CLy.value_close)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_7CLy.value_close)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_8CLy.value_close)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_9CLy.value_close)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_10CLy.value_close)), linestyle='--', marker='None', color='green', linewidth=1)
    
    date_format = mdates.DateFormatter('%Y-%m-%d')  # 날짜 형식 지정
    ax.xaxis.set_major_locator(mdates.DayLocator())  # 일 단위로 눈금 표시
    ax.xaxis.set_major_formatter(date_format)
    
    # # x축 라벨을 세로로 변환
    ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='right')
    ax.set_xlabel("date")
    ax.set_ylabel("close")
    ax.set_title(f'{select_coin} , close 6 day predict date :  {select_date} ')  # (f' 예측날짜:  {select_date} 9시 기준')
    # plt.xticks([])  # Disable x-axis ticks
    # plt.yticks([])  # Disable y-axis ticks
    ax.grid(True)
    ax.axvline(x=data4_1CLx[(len(data4_1CLx) - 7)], color='red', linestyle='dashed', linewidth=4)
    
    ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1CLy.value_close[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
    ax.plot(data4_1CLx[:(len(data4_1CLy0.value_close))], (data4_1CLy0.value_close), linestyle='-', marker='*', color='black', linewidth=2)




    # plt.show()
    st.pyplot(fig)

col3,col4 = st.columns([1,1])


with col3 :
  # column 1 에 담을 내용
    fig, ax = plt.subplots()
    ax.plot(data4_1CLx, data4_1Hhy['value_high'], linestyle='-', marker='None', color='white', linewidth=1)
    ax.set_ylim(np.min(data4_1Hhy['value_high'])*0.92, np.max(data4_1Hhy['value_high'])*1.08)
    
    
    # # Plotting additional points
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_2Hhy.value_high)), linestyle='-', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_12Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_13Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_15Hhy.value_high)), linestyle='--', marker='None', color='red', linewidth=1)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_3Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_4Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_5Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_6Hhy.value_high)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_7Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_8Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_9Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Hhy.value_high[:(len(data4_1CLx) - 6)], data4_10Hhy.value_high)), linestyle='--', marker='None', color='green', linewidth=1)
    
    date_format = mdates.DateFormatter('%Y-%m-%d')  # 날짜 형식 지정
    ax.xaxis.set_major_locator(mdates.DayLocator())  # 일 단위로 눈금 표시
    ax.xaxis.set_major_formatter(date_format)
    
    # # x축 라벨을 세로로 변환
    ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='right')
    ax.set_xlabel("date")
    ax.set_ylabel("high")
    ax.set_title(f'{select_coin} , high 6 day predict date:  {select_date} ')  # (f' 예측날짜:  {select_date} 9시 기준')
    # plt.xticks([])  # Disable x-axis ticks
    # plt.yticks([])  # Disable y-axis ticks
    ax.grid(True)
    ax.axvline(x=data4_1CLx[(len(data4_1CLx) - 7)], color='red', linestyle='dashed', linewidth=4)
    
    ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1Hhy.value_high[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
    ax.plot(data4_1CLx[:(len(data4_1Hhy0.value_high))], (data4_1Hhy0.value_high), linestyle='-', marker='*', color='black', linewidth=2)
    # plt.show()
    st.pyplot(fig)
    


with col4 :
    fig, ax = plt.subplots() 
    ax.plot(data4_1CLx, data4_1Lwy['value_low'], linestyle='-', marker='o', color='white', linewidth=1)
    ax.set_ylim(np.min(data4_1Lwy['value_low'])*0.92, np.max(data4_1Lwy['value_low'])*1.08)
    
     
    # # Plotting additional points
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_2Lwy.value_low)), linestyle='-', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_12Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_13Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_15Lwy.value_low)), linestyle='--', marker='None', color='red', linewidth=1)
    
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_3Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_4Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_5Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_6Lwy.value_low)), linestyle='--', marker='None', color='blue', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_7Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_8Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_9Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    ax.plot(data4_1CLx, np.concatenate((data4_1Lwy.value_low[:(len(data4_1CLx) - 6)], data4_10Lwy.value_low)), linestyle='--', marker='None', color='green', linewidth=1)
    
    date_format = mdates.DateFormatter('%Y-%m-%d')  # 날짜 형식 지정
    ax.xaxis.set_major_locator(mdates.DayLocator())  # 일 단위로 눈금 표시
    ax.xaxis.set_major_formatter(date_format)
    
    # # x축 라벨을 세로로 변환
    ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='right')
    ax.set_xlabel("date")
    ax.set_ylabel("low")
    ax.set_title(f'{select_coin} , low 6 day predict date:  {select_date} ')  # (f' 예측날짜:  {select_date} 9시 기준')
    # plt.xticks([])  # Disable x-axis ticks
    # plt.yticks([])  # Disable y-axis ticks
    ax.grid(True)
    ax.axvline(x=data4_1CLx[(len(data4_1CLx) - 7)], color='red', linestyle='dashed', linewidth=4)
    
    ax.plot(data4_1CLx[:(len(data4_1CLx) - 6)], (data4_1Lwy.value_low[:(len(data4_1CLx) - 6)]), linestyle='-', marker='*', color='black', linewidth=2)
    ax.plot(data4_1CLx[:(len(data4_1Lwy0.value_low))], (data4_1Lwy0.value_low), linestyle='-', marker='*', color='black', linewidth=2)
    # plt.show()
    st.pyplot(fig)


    
# with 구문 말고 다르게 사용 가능 
# col1.subheader(' i am column1  subheader !! ')
# col2.checkbox('this is checkbox2 in col2 ') 
# col3.checkbox('this is checkbox2 in col2 ') 
#=>위에 with col2: 안의 내용과 같은 기능을합니다


st.markdown(f'#### 참고. 투자코인 , 예측날짜:  {formatted_date} 9시 기준')

select_multi_coin2 = ['ETH','LSK','EOS','QTUM','BTT','LINK','GMT',
                      'SEI','ETC','MBL','NEO','EGLD','IMX','SC','SSX',
                     '코웨이','현대미포조선']
data3_2 = data3[ (data3['coin'].isin(select_multi_coin2))  & (data3['예측일']==select_date)  &  (data3['SEQ'] >= min(seqs)) & (data3['SEQ'] <= max(seqs))]
data3_2 = data3_2.sort_values(by='고점갱신확률', ascending=True)
data3_2.index = [''] * len(data3_2)

st.write(data3_2[[ 'date','coin', 'SEQ',  '종가상승확률','고점갱신확률','저점상승확률']])
