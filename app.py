import streamlit as st
import pickle
import numpy as np

# Title of the App
st.title("Grade Prediction App")
st.write("This app predicts grades based on input features and assigns a letter grade.")

# Sidebar for feature inputs (assuming the model requires 5 features)
st.sidebar.header("Input Features")
feature1 = st.sidebar.number_input("G1", value=0.0, step=0.01)
feature2 = st.sidebar.number_input("G2", value=0.0, step=0.01)
feature3 = st.sidebar.number_input("failures", value=0.0, step=0.01)
feature4 = st.sidebar.number_input("famrel", value=0.0, step=0.01)
feature5 = st.sidebar.number_input("studytime", value=0.0, step=0.01)

# Load the trained model
try:
    with open("grade_prediction_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("The model file (grade_prediction_model.pkl) was not found. Please upload it to the app directory.")
    st.stop()

# Function to map numerical grades to letter grades
def map_to_letter_grade(grade):
    if grade >= 90:
        return "A+"
    elif grade >= 80:
        return "A"
    elif grade >= 70:
        return "B+"
    elif grade >= 60:
        return "B"
    elif grade >= 50:
        return "C+"
    elif grade >= 40:
        return "C"
    elif grade >= 30:
        return "D"
    else:
        return "Fail"

# Predict Button
if st.button("Predict Grade"):
    # Check if all features are 0.0
    if feature1 == 0.0 and feature2 == 0.0 and feature3 == 0.0 and feature4 == 0.0 and feature5 == 0.0:
        st.warning("All features are set to 0.00. Please enter meaningful values before predicting.")
    else:
        # Prepare the feature array
        features = np.array([[feature1, feature2, feature3, feature4, feature5]])
        
        # Make prediction
        try:
            predicted_grade = model.predict(features)[0]
            letter_grade = map_to_letter_grade(predicted_grade)
            st.success(f"Predicted Numerical Grade: {predicted_grade:.2f}")
            st.success(f"Assigned Letter Grade: {letter_grade}")
        except Exception as e:
            st.error(f"An error occurred while predicting: {e}")

# Additional Information
st.write("---")
st.write("This app demonstrates a grade prediction model with letter grade mapping.")
