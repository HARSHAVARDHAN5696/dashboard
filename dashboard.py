#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace with your dataset path)
file_path = r"C:\Users\hp\OneDrive\Documents\P PROJECTS\weekly challenge 4\cbp21cd (1).xlsx"
df = pd.read_excel(file_path)

# Page title
st.title("Interactive Dashboard: Business Analysis")

# Sidebar for interactivity
st.sidebar.header("Filters")
selected_state = st.sidebar.selectbox("Select a State", df['State'].unique())
state_data = df[df['State'] == selected_state]

# Visualization 1: Histogram of Number of Establishments
st.subheader(f"Distribution of Number of Establishments in {selected_state}")
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.histplot(state_data['Number of Establishments'], bins=20, kde=True, ax=ax1)
ax1.set_title(f"Number of Establishments in {selected_state}")
ax1.set_xlabel("Number of Establishments")
ax1.set_ylabel("Frequency")
st.pyplot(fig1)

# Visualization 2: Scatter Plot - Establishments vs Employment
st.subheader(f"Number of Establishments vs Employment in {selected_state}")
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='Number of Establishments', y='Employment', data=state_data, ax=ax2)
ax2.set_title(f"Establishments vs Employment in {selected_state}")
ax2.set_xlabel("Number of Establishments")
ax2.set_ylabel("Employment")
st.pyplot(fig2)

# Visualization 3: Correlation Heatmap
st.subheader(f"Correlation Heatmap for {selected_state}")
numerical_features = ['Number of Establishments', 'Employment', 'Annual Payroll ($1,000)']
correlation_matrix = state_data[numerical_features].corr()
fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax3)
ax3.set_title(f"Correlation Heatmap for {selected_state}")
st.pyplot(fig3)

# Additional insights section
st.sidebar.subheader("About the Dashboard")
st.sidebar.write("""
This dashboard provides an interactive way to explore the relationship between 
the number of establishments, employment, and payroll data across states.
""")


# In[ ]:




