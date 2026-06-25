import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")

name = st.text_input("Enter Your name: ")

if name:
    st.write(f"Hello, {name}")

#Slider 
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Hi {name} your age is {age}.")

#Select Box
options = ['Python', 'Java', "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language: ", options)
st.write(f"you selected {choice}.")


#Showing dataframe
data = {
    "Name" : ["jhon", "Ram", "Jake"],
    "Age" :  [23,35,67],
    "City" : ["New York", "Ayodhya", "Houston"]
}

df =pd.DataFrame(data)
st.write(df)

#File Upload

uploaded_file = st.file_uploader("Choose a CSV file", type="csv") 
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)