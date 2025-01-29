#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:28:32 2025

@author: aideidemudia
"""


# PART 1
# Introduction to Streamlit
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




# PART 3
# Building a Researcher Profile Page


# Title of the app
st.title("PART 3 EXERCISE")
st.title(":sunflower::sunflower::sunflower: Researcher Profile Page \:sunflower::sunflower::sunflower:")

# Collect basic information
name = "Ms. Zoe Aidomo Idemudia"
field = "Computer Science"
institution = "North West University"

# Display basic profile information
st.header(":sunflower::sunflower::sunflower: Researcher Overview  \:sunflower::sunflower::sunflower:")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Import an image on the side bar
with st.sidebar: 
    st.image("IMG_4809.jpeg", caption="Zoe A Idemudia", width=300)


# Adding tabs

tab1, tab2, tab3 = st.tabs(["Biography", "Qualifications & Certifications", "List of Achivements"])

with tab1:
    paragraph = """Zoe Idemudia is a distinguished computer scientist known for her contributions to network security, artificial intelligence, and distributed systems. With a strong academic background in computer science and cybersecurity, she has made significant strides in developing secure communication protocols and optimizing AI-driven security measures for modern networks.

Born with a passion for technology, Zoe pursued her bachelor’s degree in Computer Science at [University Name] before advancing to a master’s program in Cybersecurity and AI. During her graduate studies, she focused on machine learning applications for threat detection, publishing influential research on anomaly detection in large-scale networks.

Zoe’s professional journey has seen her work with leading tech companies and research institutions, where she contributed to developing secure cloud computing architectures and advancing blockchain security solutions. She has also played a key role in open-source projects aimed at improving privacy-preserving computing.

Beyond her technical expertise, Zoe is passionate about mentoring young women in STEM, leading initiatives that empower underrepresented groups in technology. She frequently speaks at cybersecurity conferences and AI summits, sharing insights on the evolving landscape of digital security.

Currently, Zoe is a senior researcher at [Organization], where she continues to push the boundaries of network resilience and AI-driven cybersecurity. Her work has earned her recognition as one of the Top 50 Women in Tech, solidifying her reputation as a thought leader in the field.

When she’s not working on cutting-edge technology, Zoe enjoys coding challenges, hiking, and exploring emerging trends in quantum computing.""" 

    st.header("Zoe Idemudia – Computer Scientist & Innovator")
    st.write(paragraph)



st.write("\n\n\n\n\n\n\n\n")

# Add a section for publications
st.markdown(":tulip::cherry_blossom::rose: Publications \:tulip::cherry_blossom::rose:")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="pdf")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower()
                               in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header(":tulip::cherry_blossom::rose: Publication Trends \:tulip::cherry_blossom::rose:")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "aide.idemudia@yahoo.com"
st.write(f"You can reach {name} at {email}.")


