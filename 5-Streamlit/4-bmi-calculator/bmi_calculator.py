import streamlit as st
import sys


def suggestions(bmi: int):
    """
    Suggests users about health based on their bmi

    :param bmi (int): user's bmi
    """
    if bmi < 18.5:
        st.warning("**UnderWeight:** Increase calories. Intake through healthy foods")
    elif bmi > 18.5 and bmi < 24.5:
        st.success("**Normal Weight:** Maintain a balanced diet ")
    elif bmi > 24.5 and bmi < 29.5:
        st.warning("**OverWeight:** Control Calories. Start exercises to lose weight.")
    else:
        st.error(
            "**Obesity:** Start exercises to lose weight, control calories and take special trainer coaching"
        )


st.title("BMI Calculator")
st.text("Happy Fitness! 😃")

weight = st.number_input("Enter your Weight", 0)
height = st.number_input("Enter your Height", 0)

height *= 0.3048

if weight > 0 and height > 0:

    submit = st.button("Get BMI")
    BMI = weight / (height**2)

    if submit:
        f"# BMI {BMI}"
        suggestions(BMI)
else:
    sys.exit("Invalid Weight and height")
