import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff


st.header("Welcome to Manohar's Data Visualization")
data = pd.read_csv("C:/PYTHON_DS/STREAMLIT/NANNA/LPI _ EPI updated (5).csv")
df = pd.DataFrame(data)
st.dataframe(df)

#-------------------------------------------------------------------------------------------------

st.subheader("Sales Growth Executive wise")
set1 = set(df['Sale State'])
choice = st.multiselect("Select State:",set1)
#df2 = df['Sale State'] == choice
# df3 = df.copy()
# df3 = df3[df3['Sale State'] == choice]
# filtered_df = df['Sale State'] == choice

    
if choice:
    filtered_df = df[df['Sale State'].isin(choice)]
    tot_qty = filtered_df['Qty'].sum()
    
    fig = px.bar(filtered_df,x = 'F Y', y = 'Qty', labels={'Qty': 'Total Quantity', 'F Y': 'Year'})
    st.plotly_chart(fig)


