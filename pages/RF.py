import streamlit as st
import pandas as pd
import numpy as np
import pickle
import streamlit.components.v1 as com

loaded_model=pickle.load(open('C:/Users/Acer/project/pages/SVM.sav','rb'))

with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)

def main():
 st.markdown("""
    <div class="css-18ni7ap e13qjvis2" style='text-align: center;' >
             <p style='font-size: 50px;'><b>Heart Disease Prediction System</b></p>
    </div>

  """,unsafe_allow_html=True)
 
 st.markdown("<h1 style='text-align: center;'>Patient Information Form</h1>", unsafe_allow_html=True)
 st.markdown("---")
 with st.form("Form1"):

    # Name input field
    name = st.text_input("Name")
    
    # Age input field
    age = st.number_input("Age", min_value=1, max_value=150, step=1)
    
    # Sex selection field
    sex_options = ["1", "0"]
    sex = st.selectbox("Sex (1=Male,0=Female)", sex_options)
    
    # Chest Pain type selection field
    cp_options = ["0", "1", "2", "3"]
    cp = st.selectbox("Chest Pain Type (0=Typical Angina,1=Atypical Angina,2=Non-anginal Pain,3=Asymptomatic)", cp_options)
    
    # Resting ECG selection field
    restecg_options = ["1", "2", "3"]
    restecg = st.selectbox("Resting ECG(1=Normal,2=Abnormal,3=Probable or Definite Ventricular Hypertrophy)", restecg_options)
    
    # Maximum Heart Rate (thalach) input field
    thalach = st.number_input("Maximum Heart Rate (thalach)", min_value=1, max_value=300, step=1)
    
    # Exercise Induced Angina selection field
    exang_options = ["1", "0"]
    exang = st.selectbox("Exercise Induced Angina (1=Yes,0=No)", exang_options)
    
    # ST Depression Induced by Exercise Relative to Rest (oldpeak) input field
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest (oldpeak)")
    
    # Slope of the Peak Exercise ST Segment selection field
    slope_options = ["0", "1", "2"]
    slope = st.selectbox("Slope of the Peak Exercise ST Segment (0=Upsloping,1=Flat,2=Downsloping)", slope_options)
    
    # Number of Major Vessels Colored by Fluoroscopy (ca) input field
    ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy (ca)", min_value=0, max_value=4, step=1)
    
    # Thalassemia selection field
    thal_options = ["0", "1", "2"]
    thal = st.selectbox("Thalassemia (0=Normal,1=Fixed Defect,2=Reversible Defect)", thal_options)
    
    # Resting blood pressure
    restbps=st.number_input("Resting blood pressure")

    # Cholestoral
    chol=st.number_input("Cholestrol")

    # Fasting blood sugar
    fbps_options = ["0","1"]
    fbps=st.selectbox("Fasting blood sugar>120 (1=true,0=false)",fbps_options)
    
    


    diagnosis=''
    s_state=st.form_submit_button("Submit")

    # Submit button
    if s_state:
         diagnosis = heart_disease_prediction([
         int(age),
         int(sex),
         int(cp),
         int(restbps),
         int(chol),
         int(fbps),
         int(restecg),
         int(thalach),
         int(exang),
         int(oldpeak),
         int(slope),
         int(ca),
         int(thal)
         ])

    st.success(diagnosis)

def heart_disease_prediction(input_data):

    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
        return'The person does not have heart disease'
    else:
        return'The person has heart disease'
    
if __name__ == "__main__":
    main()

    


     


