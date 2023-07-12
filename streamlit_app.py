import streamlit as st
import random
import pandas as pd

random.seed(42)

st.set_page_config(
        page_title="Data Storytelling",
        page_icon="📊"
)

data = {
    'Year': [],
    'Sales': [],
    'Expenses': [],
    'Profit': [],
    'Region': []
}

for _ in range(99):
    year = random.randint(2010, 2022)
    sales = random.randint(10000, 200000)
    expenses = random.randint(5000, 100000)
    profit = sales - expenses
    region = random.choice(['North', 'South', 'East', 'West'])
    
    data['Year'].append(year)
    data['Sales'].append(sales)
    data['Expenses'].append(expenses)
    data['Profit'].append(profit)
    data['Region'].append(region)

# Add one outlier 
data['Year'].append(2022)
data['Sales'].append(10000000)  # Outlier value
data['Expenses'].append(500000)
data['Profit'].append(9500000)
data['Region'].append('Outlier')

df = pd.DataFrame(data)

st.title("Storytelling with Data 🎭📈 helooo")

st.dataframe(df, hide_index=True)