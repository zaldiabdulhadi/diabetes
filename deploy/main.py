import streamlit as st
import pickle

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

def head() :
    st.title('Data Mining Prediksi Diabetes')

def body() :
    
    st.download_button('Download Dataset Here', 'text/csv', 'diabetes.csv')
    
    col1, col2 = st.columns(2)
    
    with col1 :
        Pregnancies = st.text_input('Input Nilai Pregnancies')
        Glucose = st.text_input('Input Nilai Glucose')
        BloodPresure = st.text_input('Input Nilai BloodPresure')
        SkinThickness = st.text_input('Input Nilai SkinThickness')
    
    with col2 :
        Insulin = st.text_input('Input Nilai Insulin')
        BMI = st.text_input('Input Nilai BMI')
        DiabetesPedigreeFunction = st.text_input('Input Nilai DiabetesPedigreeFunction')
        Age = st.text_input('Input Nilai Age')
    
    diabetes_diagnosis = ''
    if st.button('Prediksi Diabetes') :
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPresure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diabetes_prediction :
            diabetes_diagnosis = 'Pasien Terkena Diabetes'
        else :
            diabetes_diagnosis = 'Pasien Tidak Terkena Diabetes'
            
        st.success(diabetes_diagnosis)
        
head()
body()