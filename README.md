# 💊 MedVerify AI

## AI-Based Counterfeit Medicine Detection System

MedVerify AI is a computer vision-based system that verifies medicine authenticity by comparing medicine package images with verified genuine medicine samples.

## Features

- Upload medicine package image
- AI-based visual fingerprint extraction
- Authenticity score generation
- Genuine medicine matching
- Counterfeit detection
- Streamlit-based user interface

## How It Works

1. User uploads medicine image
2. MobileNetV2 extracts visual features
3. Extracted features are compared with genuine medicine database
4. Similarity score is calculated
5. System predicts:

- Genuine Medicine ✅
- Needs Inspection ⚠️
- Possible Counterfeit ❌


## Technologies Used

- Python
- TensorFlow
- MobileNetV2
- Streamlit
- Scikit-learn
- Computer Vision


## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt