import streamlit as st
import joblib

st.title("News Category Prediction")

model = joblib.load('Naive_Bayes_model.joblib')

input_text= st.text_area(
    label='Enter news text that you want to predict',max_chars=2000
)
if st.button('Predict Category'):
    output= model.predict([input_text])
    st.success(output[0])