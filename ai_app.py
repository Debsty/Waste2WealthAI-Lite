import streamlit as st
import numpy as np
from PIL import Image
import pytesseract
import plotly.express as px
import time

st.set_page_config(page_title="Waste2WealthAI Lite", layout="centered")

st.title("♻️ Waste2WealthAI Lite")
st.subheader("A lightweight waste classification and OCR demo using AI")

uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.info("Analyzing Image...")
    time.sleep(2)

    # --- Simulated AI Prediction ---
    predicted_class = "Plastic Bottle"
    estimated_value = "₦15.00"

    st.success(f"🧠 Predicted Class: {predicted_class}")
    st.success(f"💰 Estimated Value: {estimated_value}")

    # --- OCR Extraction ---
    st.subheader("🔍 Extracted Text (OCR)")
    text = pytesseract.image_to_string(image)
    st.code(text or "No text found.")

    # --- Visualization ---
    st.subheader("📊 Impact Visualization (Simulated)")
    data = {
        "Category": ["Plastic", "Glass", "Paper", "Metal"],
        "Weight (kg)": [2.4, 1.2, 0.5, 3.0],
        "Value (₦)": [120, 80, 25, 150]
    }

    fig = px.bar(data, x="Category", y="Value (₦)", color="Category", title="Recyclable Waste Value")
    st.plotly_chart(fig)
