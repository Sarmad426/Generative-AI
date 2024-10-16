# Draw a title and some text to the app:
"""
# This is the document title

This is some _markdown_.
"""
import streamlit as st

import pandas as pd

df: pd.DataFrame = pd.DataFrame({"col1": [1, 2, 3], "col2": list("abc")})
df  # 👈 Draw the dataframe


x: int = 100

"x", x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np


"""
# Streamlit magic commands

## Visualizing numpy random array as histogram using `matplotlib`
"""

arr = np.random.randint(1, 100, size=100)
figure, axis = plt.subplots()
axis.hist(arr, bins=30)

figure  # 👈 Draw a Matplotlib chart
