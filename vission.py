from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from PIL import Image as Pilimg
import google.generativeai as genai
genai.configure(api_key=os.getenv("API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)    
    return response.text



st.set_page_config(page_title="Gemini Image Demo")
st.header('Gemini Application')
input=st.text_input("Input Prompt :",key="input")


uploaded_file=st.file_uploader("Choose an image...",type=["jpg",'jpge','png'])
Image=""
if uploaded_file is not None:
    image=Pilimg.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)


submit=st.button("Tell e about the image")   

## if submit is clicked
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is ")
    st.write(response)