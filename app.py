#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:28:32 2025

@author: aideidemudia
"""


# PART 1
# Introduction to Streamlit
import plotly.express as px
import pandas as pd
import streamlit as st

st.title("**PART 1 EXERCISE**")
st.title("Streamlit is amazing")

st.write("Hello, Streamlit!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")



# PART 2
# My Plot of data
st.title("**PART 2 EXERCISE**")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)





