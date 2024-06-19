!pip install seaborn
import streamlit as st
import seaborn as sns
import pandas as pd
dataset=st.container()

with dataset:
    st.write("Titanic Data")
    df=sns.load_dataset('titanic')
    st.write(df.head())
