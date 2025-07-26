# ♻️ Waste2Wealth AI Lite

A lightweight AI-powered Streamlit web app to:
- Classify waste (e.g., plastic bottles)
- Extract text from uploaded images using a cloud-based OCR API

---

## 🚀 Features

- Upload `.jpg`, `.jpeg`, or `.png` waste images
- Simulated classification with sample value output
- Real-time OCR using [OCR.Space](https://ocr.space/OCRAPI)
- Compatible with **Streamlit Cloud** (no Tesseract required)

---

## 📦 Installation

```bash
pip install -r requirements.txt
streamlit run Waste2Wealth_ai_app.py
