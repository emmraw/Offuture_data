import pandas as pd
import streamlit as st
import matplotlib as plt

st.title("Offuture Graphs")

df = pd.read_excel("offuture_data.xlsx")
df.head()


