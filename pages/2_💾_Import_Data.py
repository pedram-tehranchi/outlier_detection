import streamlit as st
import streamlit.server as server
import pandas as pd

st.markdown("# import your data 💾")
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    st.dataframe(df.head(15))
    df.to_csv("pages/data.csv", index=False)

st.sidebar.markdown("# import data 💾")
