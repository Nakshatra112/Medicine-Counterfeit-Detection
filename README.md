# 💊 MedVerify AI

## AI-Based Counterfeit Medicine Detection System

MedVerify AI is a computer vision-based system that verifies medicine authenticity by comparing medicine package images with verified genuine medicine samples. The system uses deep learning-based visual feature extraction to identify similarities between uploaded medicine images and trusted reference samples.

---

# 👥 Team Details

**Team Name:** Byteblasters

**Team Members:**

1. Nakshatra S
2. Navaneethan VK

---

# 📌 Problem Statement

Counterfeit medicines are a serious healthcare concern that can lead to treatment failure and risks to patient safety. Traditional medicine verification methods require manual inspection and expert knowledge, making them time-consuming and difficult to access.

This project aims to develop an AI-powered computer vision system that can analyze medicine package images and identify possible counterfeit medicines automatically.

---

# 🎯 Objective

The main objectives of MedVerify AI are:

* To detect possible counterfeit medicines using computer vision.
* To extract unique visual fingerprints from medicine packaging.
* To compare uploaded medicine images with verified genuine medicine samples.
* To generate an authenticity confidence score.
* To provide a quick and efficient preliminary medicine verification system.

---

# 💡 Proposed Solution

MedVerify AI uses a deep learning-based image verification approach.

The system workflow:

1. User uploads a medicine package image.
2. The image is preprocessed for analysis.
3. MobileNetV2 extracts deep visual features from the image.
4. Extracted features are converted into visual fingerprints.
5. The fingerprints are compared with verified genuine medicine samples.
6. Cosine similarity is used to calculate the similarity score.
7. The system provides the final authenticity result.

The prediction categories are:

* Genuine Medicine ✅
* Possible Counterfeit ❌

---

# ✨ Features

* Upload medicine package image.
* AI-based visual fingerprint extraction.
* Authenticity score generation.
* Matching with genuine medicine reference images.
* Counterfeit medicine detection.
* Streamlit-based interactive user interface.
* Visual comparison between uploaded medicine and genuine reference image.
* AI explanation of analyzed visual fingerprints.

---

# 🛠 Technologies Used

## Programming Language

* Python

## Computer Vision & Deep Learning

* TensorFlow
* Keras
* MobileNetV2
* PIL (Python Imaging Library)

## Machine Learning

* Scikit-learn
* Cosine Similarity

## User Interface

* Streamlit

## Development Tools

* GitHub
* VS Code

---

# 📂 Dataset

The system uses a medicine image dataset containing verified genuine medicine package images.

The images are processed using MobileNetV2 to generate feature embeddings. These embeddings are stored as reference fingerprints and used for similarity comparison.

---

# 🧠 Methodology / Model Architecture

The overall architecture of MedVerify AI:

```
Medicine Image Upload
          |
          ↓
Image Preprocessing
          |
          ↓
MobileNetV2 Feature Extraction
          |
          ↓
Visual Fingerprint Generation
          |
          ↓
Cosine Similarity Matching
          |
          ↓
Authenticity Score Calculation
          |
          ↓
Final Prediction
```

---

# 🔍 Visual Fingerprints Analyzed

The AI system analyzes visual characteristics from medicine packaging including:

### Packaging Layout

* Arrangement of text, logos, symbols, and design elements.

### Logo and Label Features

* Logo shape, position, and visual patterns.

### Color Patterns

* Dominant colors, color combinations, and printing consistency.

### Typography Appearance

* Font style, text alignment, spacing, and label structure.

### Package Geometry

* Shape, edges, dimensions, and overall package appearance.

### Graphic Patterns

* Printed images, icons, illustrations, and background designs.

### Texture Details

* Packaging texture and printing variations.

### Deep Visual Embeddings

* High-level image features extracted using MobileNetV2 neural network.

---

# ⚙ Installation & Setup Instructions

## Clone Repository

```bash
git clone https://github.com/Nakshatra112/Medicine-Counterfeit-Detection.git
```

## Navigate to Project Folder

```bash
cd Medicine-Counterfeit-Detection
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# 🚀 Usage Instructions

1. Launch the Streamlit application.
2. Upload a medicine package image.
3. Click the **Check Authenticity** button.
4. The system analyzes the image and displays:

* Authenticity percentage.
* Matched genuine medicine image.
* Final prediction.
* AI explanation.

---

# 📊 Results and Outputs

## Genuine Medicine Example

```
Authenticity Score: 93.xx %

Matched With: Genuine Reference Image

Result: Genuine Medicine ✅
```

## Counterfeit Medicine Example

```
Authenticity Score: 41.xx %

Result: Possible Counterfeit ❌
```

The system successfully differentiates between genuine and counterfeit medicine images based on visual similarity analysis.

---

# 🔮 Future Scope

Future improvements include:

* Training with a larger medicine image dataset.
* Barcode and QR code verification.
* OCR-based expiry date and batch number verification.
* Detection of packaging tampering.
* Mobile application deployment.
* Cloud-based medicine authentication platform.
* Integration with pharmaceutical databases.

---

# 📚 References

1. TensorFlow Documentation
   https://www.tensorflow.org/

2. MobileNetV2 Research Paper
   Sandler et al., "MobileNetV2: Inverted Residuals and Linear Bottlenecks"

3. Scikit-learn Documentation
   https://scikit-learn.org/

4. Streamlit Documentation
   https://streamlit.io/
