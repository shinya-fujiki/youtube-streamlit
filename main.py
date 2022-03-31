import streamlit as st
import numpy as np
import pandas as pd

st.title('straemlit入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(15,3),
    columns=['a','b','c']
)

st.write(df)

st.table(df)

st.dataframe(df, width=50, height=100)
st.dataframe(df, width=100, height=100)

st.line_chart(df)