import streamlit as st
import pandas as pd
st.title("vic")
paths=r".\Challenge_dataset_traité.csv"
data=pd.read_csv(paths)
st.DataFrame(data)
