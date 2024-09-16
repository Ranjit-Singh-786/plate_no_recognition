# code to be detect the number from the direct pass image
# but it is in process


import streamlit as st 
from PIL import Image  

st.set_page_config(page_title="Plate no. recognition") 
st.header("Recognize the number of plate 🚗🚓🚍")
uploaded_file  = st.file_uploader("choose your image : ",type=['jpg'])

if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file) 
    st.image(uploaded_image,caption="uploaded image",use_column_width=True)

submit = st.button("submit")

