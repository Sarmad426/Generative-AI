"""
Streamlit Callback args
"""

import streamlit as st

st.title("Counter Example using Callbacks with args")
if "count" not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input("Enter a value", value=1, step=5)


def increment_counter(increment_value: int):
    """
    Increments the counter by given parameter

    :param increment_value (int) :
    """
    st.session_state.count += increment_value


increment = st.button("Increment", on_click=increment_counter, args=(increment_value,))

st.write("Count = ", st.session_state.count)
