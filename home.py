import streamlit as st
import pandas as pd
with st.echo():
    st.title('This is Title:coffee:')
    st.header('I am Header')
    st. subheader('I am Subheader')
    st.text("안녕하세요")
    st.markdown('[google](https://www.google.co.kr/?hl=ko)')
    #streamlit run home.py
    df =pd.DataFrame({'col1':[1,2,3,4],
                      'col2':[11,12,13,14]})
    st.table(df)
    st.dataframe(df)
    st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2F7art7.com%2Fproduct%2F%25EC%2597%25B0%25ED%2595%2584%25EC%25B4%2588%25EC%2583%2581%25ED%2599%2594-a4%25EC%2582%25AC%25EC%259D%25B4%25EC%25A6%2588-%25EC%25B0%25B8%25EA%25B3%25A0%25EA%25B7%25B8%25EB%25A6%25BC%2F121%2F&psig=AOvVaw1eHhklk2ruk2kd45_p115C&ust=1732414492134000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMC38_mw8YkDFQAAAAAdAAAAABAE')
st.video('https://youtu.be/zbXXQCQACzs?si=cgRojv4S269mmjlC')
st.audio('교원 연수.mp3')