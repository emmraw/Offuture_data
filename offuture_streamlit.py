import strealit as st
import matplotlib as plt
import pandas as pd
import numpy as np

st.title('Offuture Graphs')

graph = df.groupby(df['Order Date'].dt.month)['Sales'].sum()
st.dataframe(graph)
st.line_chart(graph) 
