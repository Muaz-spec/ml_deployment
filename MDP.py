import streamlit as st
import pickle
from streamlit_option_menu import option_menu

#loading the dataset

heart = pickle.load(open("heart.sav", 'rb'))
diabetes = pickle.load(open("diabetes.sav", 'rb'))
liver = pickle.load(open("liver.sav", 'rb'))

with st.sidebar:
    selected = option_menu("Multiple Diseases Prediction",
                           ["Heart Diseases",
                            "Diabetes Diseases",
                            "Liver Diseases"],
                            icons=["heart", 'heart-pulse', 'heart-pulse-fill'],
                            default_index = 0)

if selected == 'Heart Diseases':

    st.title("Heart Disease Prediction")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.number_input("Age:")
    with col2:
        sex = st.number_input("Sex:")
    with col3:
        cp = st.number_input("CP:")
    with col4:
        therstbps = st.number_input("Therstbps:")
    with col1:
        chol = st.number_input("Chol:")
    with col2:
        fbs = st.number_input("FBS:")
    with col3:
        restecg = st.number_input("Restecg:")
    with col4:
        thalach = st.number_input("Thalach:")
    with col1:
        exang = st.number_input("Exang:")
    with col2:
        oldpeak = st.number_input("Oldpick:")
    with col3:
        slope = st.number_input("Slope:")
    with col4:
        ca = st.number_input("CA:")
    with col1:
        thal = st.number_input("Thal:")

    heart_diagnosis = ''

    if st.button("Heart Disease Prediction"):
        heart_prediction = heart.predict([[age, sex, cp, therstbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = "This person has heart disease"
        else:
            heart_diagnosis = "This person is safe"

    st.success(heart_diagnosis)

if selected == "Diabetes Diseases":

    st.title("Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnencies = st.text_input("Number of pregnencies")
    with col2:
        glucose = st.text_input("Glucose Level: ")
    with col3:
        blood_pressure = st.text_input("Blood pressure: ")
    with col1:
        skin_thickness = st.text_input("Skin thickness")
    with col2:
        insulin = st.text_input("Insulin: ")
    with col3:
        bmi = st.text_input("BMI: ")
    with col1:
        diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function: ")
    with col2:
        age = st.text_input("Age: ")

    diabetes_diagnosis = ''

    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes.predict([[pregnencies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = "This person has diabetes"
        else:
            diabetes_diagnosis = "This person does not have diabetes"

    st.success(diabetes_diagnosis)

if selected == "Liver Diseases":

    st.title("Liver Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input("Age:")
    with col2:
        Gender = st.number_input("Gender:")
    with col3:
        TB = st.number_input("TB")
    with col1:
        DB = st.number_input("DB")
    with col2:
        Alkphos = st.number_input("Alkphos")
    with col3:
        Sgpt = st.number_input("Sgpt")
    with col1:
        Sgot = st.number_input("Sgot")
    with col2:
        TP = st.number_input("TP")
    with col3:
        ALB = st.number_input("ALB")
    with col1:
        A_G_Ratio = st.number_input("A/g Ratio:")

    liver_diagnosis = ''

    if st.button("Liver Diseases Prediction"):
        liver_prediction = liver.predict([[Age, Gender, TB, DB, Alkphos, Sgpt, Sgot, TP, ALB, A_G_Ratio]])

        if liver_prediction[0] == 1:
            liver_diagnosis = "This person has liver deseases"
        else:
            liver_diagnosis = "This person is safe"


    st.success(liver_diagnosis)
