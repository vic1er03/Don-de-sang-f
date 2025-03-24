import streamlit as st
import pandas as pd
st.title("vic")
data=pd.read_csv("Challenge_dataset_traité.csv")
st.DataFrame(data)
