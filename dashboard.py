
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
from datetime import datetime


# st.title('this is title')
# st.header('this is header')
# st.subheader('this is subheader'


# 현재 날짜 가져오기
today = datetime.today()

# 날짜를 문자열로 변환하여 포매팅
formatted_date = today.strftime("%Y-%m-%d")

# Streamlit Markdown에 날짜 추가
st.title("코인예측 시뮬레이션 데시보드")
st.markdown(f'### 1. 코인 추천랭킹, 예측날짜: {formatted_date} 9시 기준')
# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title("Coin Chart")
st.sidebar.markdown('비트/알트코인 Link : [All Coin Symbols](https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC)')
st.sidebar.markdown('코스피200 Link : [All Kospi200 Symbols](https://finance.naver.com/sise/sise_index.nhn?code=KPI200)')
st.sidebar.markdown('나스닥200 Link : [All Nasdaq200 Symbols](https://kr.investing.com/indices/nq-100-components)')






uploaded_file = st.file_uploader(
    'C:/Users/woohy/Desktop/predict_btc/PT_ALL/final_data/web/final_web_Day_v3.csv', accept_multiple_files=False)
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding='CP949')
    # data = data.sort_values(by='RE_RANK', ascending=True)
else:
    st.error("File not found. Please check the file path.")
    
    
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
                    'NO_UP_HIGH1', 'NO_UP_CL16', 'NO_UP_HIGH16', 'NO_UP_LOW16', 'NO_UP_HCL16',
                      'NO_DOWN', 'NO_DOWN_CL16',  'NO_DOWN_LOW16',
                      'filter1', 'filter2', 'filter3', 'filter4',
                      'filter5', 'filter6', 'filter7', 'filter8',
                      'filter9', 'filter10', 'filter11', 'filter12',
                      'filter13', 'filter14']].dropna()


# selected_columns3 = ['pred_day', 'coin', 'SEQ', 'date', 'close_up', 'high_up', 'low_up' ]
data3 = data[data['GRP'] == 'Set3'][['pred_day', 'coin', 'SEQ', 'date', 'close_up', 'high_up', 'low_up' ]].dropna()




# ticker = st.sidebar.text_input("Enter a Coin (e. g. BTC)", value = 'BTC')



select_date = st.sidebar.selectbox(
    'Select Date',
    data1['pred_day'].sort_values(ascending=False).unique()
)
values = st.slider('Select a range of values', 0, len(data1['coin'].unique()), (1, 15))

data1 = data1.rename(columns={'RE_RANK': '추천순서1'})
data1 = data1.rename(columns={'RE_RANK_UP': '추천순서2'})
data1 = data1.rename(columns={'pred_day': '예측일'})

st.write(data1[(data1['예측일'] == select_date) &  (data1['추천순서1'] >= min(values)) & (data1['추천순서1'] <= max(values)) ] )

# 여러개 선택할 수 있을 때는 multiselect를 이용하실 수 있습니다 
# return : list
select_multi_coin = st.sidebar.multiselect(
    'Select Coin Symbols For #2',
    data1['coin'].sort_values(ascending=True).unique()
)


# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
data2 = data1[(data1['coin'].isin(select_multi_coin))  & (data1['예측일']==select_date)  ]
data2['추천순서1'] = data2['추천순서1'].astype(int)
data2['추천순서2'] = data2['추천순서2'].astype(int)

# 선택한 종들의 결과표를 나타냅니다.  
# st.header("Multi Select Coin Data Chart")
st.markdown(f'### 2. 코인 주요변수(다중), 예측날짜: {formatted_date} 9시 기준')
st.table(data2)


seqs = st.slider('Select a range of Predict', 0, 6, (0, 1))

# # select_species 변수에 사용자가 선택한 값이 지정됩니다
# select_coin = st.sidebar.selectbox(
#     'Select Coin Symbols For #3',
#     data3['coin'].sort_values(ascending=True).unique()
# )
data3 = data3.rename(columns={'pred_day': '예측일'})

# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
data3_1 = data3[(data3['coin'].isin(select_multi_coin))  & (data3['예측일']==select_date)  &  (data3['SEQ'] >= min(seqs)) & (data3['SEQ'] <= max(seqs))]
st.markdown(f'### 3. 매수매도결정 , 예측날짜:  {formatted_date} 9시 기준')
st.table(data3_1)



# st.sidebar 를 통해 사이드바를 생성하고 내용을 넣을 수 있음.
# st.sidebar.text_input : 사이드바에 텍스트를 입력할 수 있는 요소를 만듦
# st.sidebar.date_input : 사이드바에 날짜를 입력할 수 있는 요소를 만듦



data4 = data[data['GRP'] == 'Set4' ][['GRP', 'pred_day', 'coin', 'SEQ', 'date', 'variable', 'value_close', 'value_high', 'value_low', 'LOW_VL', 'HIGH_VL', 'CL_VL']]
# c("Pred1", "Pred2","Pred6", "Pred7","Pred9", "Pred12","Pred15",
#                                  "Pred18","Pred21", "Pred24","Pred27", "Pred33","Pred34", "Pred37","Pred52")
data4.head(5)

data4_1 = data4[(data4['coin'] == '1INCH') & (data4['pred_day'] == '02-10 Day') ]
data4_1.head(5)

data4_1CLx = data4_1[data4_1['variable'] == 'Pred1'][['date']]
data4_1CLx = ['2024-' + text[:5] for text in data4_1CLx.date ] 
data4_1CLx = pd.to_datetime(data4_1CLx)

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

data4_1CLy = data4_1[data4_1['variable'] == 'Pred1'][['value_high']]

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
st.markdown(f'### 4. 코인차트 , 예측날짜:  {formatted_date} 9시 기준')

# 라인 차트 그리기
# st.pyplot(plot_line_chart(data3, f'{select_coin} Coin Price', 'Date', 'Close Price (Won)'))

# Plotting the first set of points
plt.plot(data4_1CLx, data4_1CLy['value_close'], linestyle='--', marker='o', color='white', linewidth=1)
plt.ylim(np.min(data4_1CLy['value_close'])*0.98, np.max(data4_1CLy['value_close'])*1.02)
# plt.xlim(1, len( data4_1CLy))
# x축 라벨을 세로로 변환
plt.xticks(rotation='vertical')
plt.xlabel("날짜")
plt.ylabel("종가")
plt.title('종가 예측결과')
# plt.xticks([])  # Disable x-axis ticks
# plt.yticks([])  # Disable y-axis ticks
plt.grid(True)
plt.axvline(x=data4_1CLx[23], color='red', linestyle='dashed', linewidth=4)

# Plotting additional points
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_2CLy.value_close)), linestyle='-', marker='o', color='red', linewidth=3)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_12CLy.value_close)), linestyle='--', marker='o', color='red', linewidth=3)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_13CLy.value_close)), linestyle='--', marker='o', color='red', linewidth=3)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_15CLy.value_close)), linestyle='--', marker='o', color='red', linewidth=3)

plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_3CLy.value_close)), linestyle='--', marker='o', color='blue', linewidth=2)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_4CLy.value_close)), linestyle='--', marker='o', color='blue', linewidth=2)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_5CLy.value_close)), linestyle='--', marker='o', color='blue', linewidth=2)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_6CLy.value_close)), linestyle='--', marker='o', color='blue', linewidth=2)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_7CLy.value_close)), linestyle='--', marker='o', color='green', linewidth=2)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_8CLy.value_close)), linestyle='--', marker='o', color='green', linewidth=2)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_9CLy.value_close)), linestyle='--', marker='o', color='green', linewidth=2)
plt.plot(data4_1CLx, np.concatenate((data4_1CLy.value_close[:(len(data4_1CLx) - 6)], data4_10CLy.value_close)), linestyle='--', marker='o', color='green', linewidth=2)


plt.plot(data4_1CLx[:24], (data4_1CLy.value_close[:(len(data4_1CLx) - 6)]), linestyle='-', marker='o', color='black', linewidth=3)
plt.show()














col1,col2,col3 = st.columns([1,2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

with col1 :
  # column 1 에 담을 내용
  st.title('X1')
with col2 :
  # column 2 에 담을 내용
  st.title('X2')
  st.checkbox('this is checkbox1 in col2 ')
with col3 :
  # column 1 에 담을 내용
  st.title('X3')

# with 구문 말고 다르게 사용 가능 
col1.subheader(' i am column1  subheader !! ')
col2.checkbox('this is checkbox2 in col2 ') 
col3.checkbox('this is checkbox2 in col2 ') 
#=>위에 with col2: 안의 내용과 같은 기능을합니다






 

