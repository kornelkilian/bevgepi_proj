import streamlit as st
import joblib

# Load the trained model
model = joblib.load('mymodel.pkl')

# Streamlit app
st.title('Spotify Song Mode Prediction')

# User input
key_encoded = st.slider('Key Encoded', min_value=0, max_value=11, value=5)
danceability = st.slider('Danceability (%)', min_value=0, max_value=100, value=50)
instrumentalness = st.slider('Instrumentalness (%)', min_value=0, max_value=100, value=50)
acousticness = st.slider('Acousticness (%)', min_value=0, max_value=100, value=50)
liveness = st.slider('Liveness (%)', min_value=0, max_value=100, value=50)



# Make prediction
if st.button('Predict'):
    features = [[acousticness, danceability,key_encoded,instrumentalness,liveness]]  # Add other features
    prediction = model.predict(features)
    st.write('Prediction:', prediction)

# Add more Streamlit components and features as needed
