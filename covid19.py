import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('full_grouped.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.ffill()  # or df.bfill()


countries = df['Country/Region'].unique()
selected_country = st.selectbox("Choose a country", countries)
filtered = df[df['Country/Region'] == selected_country]

st.line_chart(filtered.set_index('Date')['Confirmed'])
st.line_chart(filtered.set_index('Date')['Deaths'])
st.line_chart(filtered.set_index('Date')['Recovered'])