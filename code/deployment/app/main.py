import requests
import streamlit as st

st.title("Digit Recognition Web App")
image = st.file_uploader("Choose an image")

if image is not None:
    st.image(image, caption="Uploaded Image")

if st.button("Get Prediction"):
    if image is not None:
        files = {"file": image}
        url = "http://backend:8080/predict"
        response = requests.post(url, files=files)
        st.write(f"Predicted digit: {response.json().get('predicted_digit')}")