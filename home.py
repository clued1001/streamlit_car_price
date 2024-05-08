import streamlit as st

def run_home():
    st.subheader('자동차 데이터를 분석하고 예측합니다!!!')
    st.text('데이터는 캐글에 있는 Car_Purchasing_Data.csv 파일을 사용합니다.')
    st.text('탐색적 데이터 분석과 자동차 구매 금액을 예측하는 앱입니다.')
    
    url = 'https://cdn.autoview.co.kr/news/photo/202401/90224_200461_4424.jpg'
    st.image(url, use_column_width= True)
    