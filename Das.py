import streamlit as st
import pandas as pd
st.title("vic")
url = ".devcontainer/Challenge dataset traité.csv"
data = pd.read_csv(url,sep=';')
st.dataframe(data)
st.DataFrame(data)
