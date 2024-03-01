import streamlit as st
import sys


weight = st.number_input("Enter your Weight", 0)
height = st.number_input("Enter your Height", 0)

if weight > 0 and height > 0:

    BMI = weight / height

    st.success(f"# BMI {BMI}")
else:
    sys.exit("Invalid Weight and height")
