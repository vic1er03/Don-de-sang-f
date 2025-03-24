import streamlit as st
import pandas as pd
from pathlib import Path
url = Path(__file__).parent / "Challenge_dataset_traité.csv"
data = pd.read_csv(url,sep=';')
st.dataframe(data)
st.DataFrame(data)
