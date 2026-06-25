'''
Streamlit is an open source app fromework for machine learning and data science projects. 
It allows you to create beautiful web application for your machine learning and 
data science projects with simple python scripts.

Run the Streamlit app :- streamlit run FILE_NAME
'''

import streamlit as st
import pandas as pd
import numpy as np


#Title of the application
st.title("Hellow world")

#Display a simple text
st.write("This is a simple text.")

#Create a simple dataframe
df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

#Display the datafrae
st.write("Here is the dataFrame")
st.write(df)


#Create a line Chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns= ['a', 'b', 'c']
)
st.line_chart(chart_data)