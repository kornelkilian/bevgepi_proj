import streamlit as st
import joblib

# Load the trained model
model = joblib.load('mymodel.pkl')

# Streamlit app
st.title('Spotify Song Mode Prediction')

# Define the list of key options
key_options = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# User input
key_encoded_text = st.selectbox('Key Encoded', key_options, index=5)  # Default to 'F'
key_encoded = key_options.index(key_encoded_text)  # Convert the selected key to numerical value
danceability = st.slider('Danceability (%)', min_value=0, max_value=100, value=50)
instrumentalness = st.slider('Instrumentalness (%)', min_value=0, max_value=100, value=50)
acousticness = st.slider('Acousticness (%)', min_value=0, max_value=100, value=50)
liveness = st.slider('Liveness (%)', min_value=0, max_value=100, value=50)

# Make prediction
if st.button('Predict'):
    features = [[acousticness, danceability, key_encoded, instrumentalness, liveness]]
    prediction = model.predict(features)
    st.write('Prediction:', prediction)

# Add more Streamlit components and features as needed
