import streamlit as st

st.text("Sarmad Basic Streamlit app.")
st.write("Basic Streamlit app.")
st.write(["st", "is <", 3])
st.markdown("# Markdown Heading")
st.title("Streamlit title")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.header("Streamlit header")
st.subheader("Streamlit sub heading")
st.subheader("\nStreamlit Code ")
st.code(
    """
    for i in range(8): 
        print(i)
    """
)

st.subheader("Streamlit python code for this page")

st.code(
    """
import streamlit as st

st.text("Sarmad Basic Streamlit app.")
st.write("Basic Streamlit app.")
st.write(["st", "is <", 3])
st.markdown("# Markdown Heading")
st.title("Streamlit title")
st.latex(r" e^{i\pi} + 1 = 0 ")
st.header("Streamlit header")
st.subheader("Streamlit sub heading")
st.subheader("\nStreamlit Code ")
    """
)
