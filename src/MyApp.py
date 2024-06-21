import streamlit as st
import pandas as pd

st.write("""
# My dirst app
         Hello *world!*
""")

df = pd.DataFrame({"a": [1, 2, 3]})
st.line_chart(df)

number = st.slider("Pick a number", 0, 100)

date = st.date_input("Pick a date")