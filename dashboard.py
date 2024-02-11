
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
st.sidebar.markdown('Tickers Link : [All Coin Symbols](https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC)')
start_date = st.sidebar.date_input("Start Date: ", value = pd.to_datetime("2024-01-01"))
end_date = st.sidebar.date_input("End Date: ", value = pd.to_datetime("2024-02-01"))

uploaded_file = st.file_uploader(
    'C:/Users/woohy/Desktop/predict_btc/PT_ALL/rank/coin_rank_DAY_2024021009_v3.csv', accept_multiple_files=False)
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding='CP949')
    data = data.sort_values(by='RE_RANK', ascending=True)
else:
    file_name = "DatabaseSample.xlsx"
    
#ticker 종목의 시작~종료 날짜 사이의 가격변화를 데이터로 보여줌
# data = pd.read_csv('C:/Users/woohy/Desktop/predict_btc/PT_ALL/rank/coin_rank_DAY_2024021009_v3.csv', encoding='CP949') # , encoding='utf-8' , thousands = ','   .str.replace(',', '').astype('int64')
# data = data.sort_values(by='RE_RANK', ascending=True)
# read.csv( paste0("C:/Users/woohy/Desktop/predict_btc/PT_ALL/rank/coin_rank_DAY_2024021009_v3.csv")
st.write(data)

ticker = st.sidebar.text_input("Enter a Coin (e. g. BTC)", value = 'BTC')





# 여러개 선택할 수 있을 때는 multiselect를 이용하실 수 있습니다 
# return : list
select_multi_coin = st.sidebar.multiselect(
    'Select Coin Symbols',
    data['coin'].sort_values(ascending=True)
)

# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
data2 = data[data['coin'].isin(select_multi_coin)]
# 선택한 종들의 결과표를 나타냅니다.  
# st.header("Multi Select Coin Data Chart")
st.markdown(f'### 2. 코인 주요변수(다중), 예측날짜: {formatted_date} 9시 기준')
st.table(data2)

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_coin = st.sidebar.selectbox(
    'Select Coin Symbols For Plot',
    data['coin'].sort_values(ascending=True)
    # ['setosa','versicolor','virginica']
)
# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
data3 = data[data['coin']== select_coin]

# 선택한 종의 맨 처음 5행을 보여줍니다 
# st.table(data3)

# st.sidebar 를 통해 사이드바를 생성하고 내용을 넣을 수 있음.
# st.sidebar.text_input : 사이드바에 텍스트를 입력할 수 있는 요소를 만듦
# st.sidebar.date_input : 사이드바에 날짜를 입력할 수 있는 요소를 만듦
def plot_line_chart(data3, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.plot(data3['filter1'], label='Close Price', color='blue')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)

st.set_option('deprecation.showPyplotGlobalUse', False)

# st.header("Single Select Coin Data")
st.markdown(f'### 3. 코인차트 , 예측날짜:  {formatted_date} 9시 기준')

# 라인 차트 그리기
# select_multi_coin2 = data['coin'].sort_values(ascending=True)
# 주식 데이터 가져오기
# data_coin_sep = data3[data3['coin'].isin(select_coin)]

# 라인 차트 그리기
st.pyplot(plot_line_chart(data3, f'{select_coin} Coin Price', 'Date', 'Close Price (Won)'))



















col1,col2 = st.columns([2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

with col1 :
  # column 1 에 담을 내용
  st.title('X1')
with col2 :
  # column 2 에 담을 내용
  st.title('X2')
  st.checkbox('this is checkbox1 in col2 ')


# with 구문 말고 다르게 사용 가능 
col1.subheader(' i am column1  subheader !! ')
col2.checkbox('this is checkbox2 in col2 ') 
#=>위에 with col2: 안의 내용과 같은 기능을합니다






 

