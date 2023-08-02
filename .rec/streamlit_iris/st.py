import streamlit as st
import pickle
from sklearn.datasets import load_iris

# Load the saved model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the Iris dataset
iris = load_iris()

# Function to make predictions
def predict_species(features):
    prediction = model.predict([features])
    species = iris.target_names[prediction[0]]
    return species

# Streamlit web app
st.title("Iris Flower Species Prediction")

# Input form for the user to enter feature values
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

# Make a prediction using the model
features = [sepal_length, sepal_width, petal_length, petal_width]
species = predict_species(features)

# Display the prediction
st.write(f"Predicted Species: {species}")
