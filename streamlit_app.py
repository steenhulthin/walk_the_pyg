import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide")
st.write("It's alive!")

uploaded_file = st.file_uploader("Add your csv data")

if uploaded_file:
    df = pd.read_csv(uploaded_file, delimiter=';')
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()