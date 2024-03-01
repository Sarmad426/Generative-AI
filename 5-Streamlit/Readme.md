# Streamlit

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.

## Activate Virtual environment

```pip
conda activate py-12
```

## Install Streamlit

```pip
pip install streamlit
```

**Validate installation with Hello app:**

```pip
streamlit hello
```

> Open <http://localhost:8501>

This starts a basic streamlit app locally.

**Streamlit docs** <https://docs.streamlit.io/>

## Commands

```yml
streamlit --help
streamlit run your_script.py
streamlit hello
streamlit config show
streamlit cache clear
streamlit docs
streamlit --version
```

## Display text

```yml
st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3]) # see *
st.write_stream(my_generator)
st.write_stream(my_llm_stream)

st.text("Fixed width text")
st.markdown("_Markdown_") # see *
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
* optional kwarg unsafe_allow_html = True
```

## Display data

```yml
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)
```

## Display media

```yml
st.image("./header.png")
st.audio(data)
st.video(data)
```

## Display Chart

```yml
st.area_chart(df)
st.bar_chart(df)
st.line_chart(df)
st.map(df)
st.scatter_chart(df)

st.altair_chart(chart)
st.bokeh_chart(fig)
st.graphviz_chart(fig)
st.plotly_chart(fig)
st.pydeck_chart(chart)
st.pyplot(fig)
st.vega_lite_chart(df)
```

For more information Checkout official **Streamlit CheatSheet**
<https://docs.streamlit.io/library/cheatsheet>
