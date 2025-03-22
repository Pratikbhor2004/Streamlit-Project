import streamlit as st
import numpy as np
import pandas as pd

st.title("This is our title")
st.write("This is what we have created")

df = pd.DataFrame({
    'name': ['sachin', 'virat', 'rohit'],
    'marks': [20, 40, 30]
})
st.write(df)

data =np.array([10,20,30,40,11])
st.line_chart(data)