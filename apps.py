import streamlit as st
import joblib
import numpy as np

# Load the SVM model
#model_path = '/Users/shasankjoshi/Desktop/Python Projects/streamlit_tutorial/svm_model.pkl'
with open("svm_model.pkl", "rb") as file:
    model = joblib.load(file)

st.title("SVM Model Prediction App")

# Example: Assuming the model expects 2 numerical inputs
feature_1 = st.number_input("Enter Feature 1", value=0.0)
feature_2 = st.number_input("Enter Feature 2", value=0.0)
feature_3 = st.number_input("Enter Feature 3", value=0.0)
feature_4 = st.number_input("Enter Feature 4", value=0.0)
feature_5 = st.number_input("Enter Feature 5", value=0.0)
feature_6 = st.number_input("Enter Feature 6", value=0.0)
feature_7 = st.number_input("Enter Feature 7", value=0.0)
feature_8 = st.number_input("Enter Feature 8", value=0.0)
feature_9 = st.number_input("Enter Feature 9", value=0.0)
feature_10 = st.number_input("Enter Feature 10", value=0.0)
feature_11 = st.number_input("Enter Feature 11", value=0.0)
feature_12 = st.number_input("Enter Feature 12", value=0.0)
feature_13 = st.number_input("Enter Feature 13", value=0.0)
feature_14 = st.number_input("Enter Feature 14", value=0.0)
feature_15 = st.number_input("Enter Feature 15", value=0.0)

# Convert input to numpy array
input_data = np.array([[feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7, feature_8, feature_9, feature_10,feature_11,feature_12,feature_13,feature_14,feature_15]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Prediction:", prediction[0])