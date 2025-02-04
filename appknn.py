import streamlit as st
import joblib
import numpy as np

# Load the trained model
model_path = "knn_breast_cancer_prediction.pkl"
model = joblib.load(model_path)

# Streamlit UI
st.title("SVM Model Prediction App")
st.write("Enter feature values to make a prediction.")

# Assuming 4 input features (adjust according to your model)
feature1 = st.number_input("Radius:", value=0.0)
feature2 = st.number_input("Texture", value=0.0)
feature3 = st.number_input("Perimeter", value=0.0)
feature4 = st.number_input("Area", value=0.0)
feature5 = st.number_input("Smoothness", value=0.0)

# Make prediction
if st.button("Predict"):
    if feature1 == 0.0 or feature2 == 0.0 or feature3 == 0.0 or feature4 == 0.0 or feature5 == 0.0:
        st.write("You have not entered a value for one or more fields.")
    else:
        input_data = np.array([[feature1, feature2, feature3, feature4, feature5]])
        prediction = model.predict(input_data)
        
        if prediction[0] == 0:
            st.write("congratulations you have No Cancer")
        else:
            st.write("You have Cancer hurry up to nearest medic")