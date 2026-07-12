import streamlit as st
from PIL import Image
from medicine_detector import check_medicine
import os


# Page configuration
st.set_page_config(
    page_title="MedVerify AI",
    page_icon="💊",
    layout="centered"
)


# Title
st.title("💊 MedVerify AI")
st.subheader("AI-powered counterfeit medicine detection system")

st.write(
    "Upload a medicine package image to verify its authenticity using AI."
)


# Upload image
uploaded_file = st.file_uploader(
    "Upload Medicine Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file:

    # Open uploaded image
    image = Image.open(uploaded_file)


    st.image(
        image,
        caption="Uploaded Medicine Image",
        width=300
    )


    if st.button("🔍 Check Authenticity"):


        st.info("Analyzing medicine image...")


        # Save uploaded image temporarily
        temp_path = "temp_image.jpg"


        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())


        # Run AI model
        score, matched, result = check_medicine(temp_path)


        # Convert numpy value to normal float
        score = float(score)


        st.success("Analysis Completed ✅")


        # Score display
        st.metric(
            "Authenticity Score",
            f"{score:.2f}%"
        )


        # Progress bar
        st.progress(score / 100)


        # Image comparison
        st.subheader("🔍 Visual Comparison")


        col1, col2 = st.columns(2)


        with col1:

            st.image(
                image,
                caption="Uploaded Medicine",
                width=250
            )


        with col2:

            if os.path.exists(matched):

                matched_img = Image.open(matched)

                st.image(
                    matched_img,
                    caption="Matched Genuine Medicine",
                    width=250
                )

            else:

                st.write(
                    "Matched Image:",
                    matched
                )


        # Result
        st.subheader("📌 Result")


        if "Genuine" in result:

            st.success(result)


        elif "Inspection" in result:

            st.warning(result)


        else:

            st.error(result)



        # AI Explanation
        st.subheader("🤖 AI Explanation")


        st.write(
            """
            The AI system verifies medicine authenticity by comparing
            the uploaded medicine image with verified genuine medicine
            samples.

            Analysis includes:

            ✅ Packaging appearance  

            ✅ Brand logo and Label features

            ✅ Visual feature patterns  

            ✅ Text and Typography appearance

            ✅ Shape and color information  

            ✅ Texture and Surface details
            
            ✅ Similarity matching with genuine medicines  

            The final decision is generated based on the similarity score.
            """
        )