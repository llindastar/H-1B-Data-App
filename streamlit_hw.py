import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

st.header('H-1B Data')

h1b_data = pd.read_csv('h-1b-data-export (2).csv')

st.dataframe(h1b_data)

st.sidebar.header("Pick two variables for your scatterplot")
x_val = st.sidebar.selectbox("Pick your x-axis",h1b_data.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis",h1b_data.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(h1b_data, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f'{x_val}'),
    alt.Y(y_val,title=f'{y_val}'),
    tooltip=[x_val,y_val]).configure(background='#D9E9F0')
st.altair_chart(scatter, use_container_width=True)

Employer = st.multiselect('Select Employer',h1b_data['Employer'])
new_employer_data = h1b_data[h1b_data['Employer'].isin(Employer)]

st.sidebar.header("Pick variables for your chart")
z_val = st.sidebar.selectbox("Pick your y-axis for your chart",h1b_data.select_dtypes(include=np.number).columns.tolist())
sum_approval = h1b_data['Sum Approval']

my_chart = alt.Chart(new_employer_data).mark_bar().encode(
    x=alt.X('Employer',sort=alt.EncodingSortField(field="Employer", op="count", order='descending')),
    y=alt.Y(z_val,title=f'{z_val}'),
    color='City'
)

st.altair_chart(my_chart)