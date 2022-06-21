import joblib
import streamlit as st
from eda import EDA

st.write("# 10 Year Heart Disease Prediction")
gender = st.selectbox("Enter your gender", ["Male", "Female"])

col1, col2, col3 = st.columns(3)

age = col2.number_input("Enter your age")
education = col3.selectbox(
    "Highest academic qualification",
    ["High school diploma", "Undergraduate degree", "Postgraduate degree", "PhD"]
)

model = joblib.load('model.pkl')

df_pred = EDA.do_eda(col1, col2, col3, gender, age, education)

prediction = model.predict(df_pred)


if st.button('Predict'):
    if prediction[0] ==0 :
        st.write(
            '<p class="big-font">You likely will not develop heart disease in 10 years.</p>',
            unsafe_allow_html=True
        )
    else:
        st.write(
            '<p class="big-font">You are likely to develop heart disease in 10 years.</p>',
            unsafe_allow_html=True
        )
