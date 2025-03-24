import streamlit as st
import pandas as pd
import os
print("Current working directory:", os.getcwd())
st.title("vic")
url = r".devcontainer/Challenge_dataset_traité.csv"
data = pd.read_csv(url,sep=';')
st.dataframe(data)
st.DataFrame(data)
