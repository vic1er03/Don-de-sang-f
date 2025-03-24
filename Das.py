import streamlit as st
import pandas as pd
st.title("vic")
url = "https://raw.githubusercontent.com/Don-de-sang-f/main/Challenge_dataset_traité.csv"
data = pd.read_csv(url)
st.dataframe(data)
st.DataFrame(data)
