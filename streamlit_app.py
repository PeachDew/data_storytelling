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
sales = 98020042
expenses = random.randint(5000, 100000)
profit = sales - expenses
data['Sales'].append(sales)  
data['Expenses'].append(expenses)
data['Profit'].append(profit)
data['Region'].append(random.choice(['North', 'South', 'East', 'West']))

df = pd.DataFrame(data)

st.title("Storytelling with Data 🎭📈")

with st.columns([1,5,1])[1]:
    st.dataframe(df, hide_index=True)
# or st.columns(3)[1].dataframe(df)    

st.markdown('''
## Using the numbers themselves
When presenting/comparing few numbers, often a good idea to present the numbers themselves.
''')

max_sale = df.Sales.max()
mean_sale = df.Sales.mean()
percentage_difference = ((max_sale - mean_sale) / mean_sale) * 100
max_sales_year = df.loc[df['Sales'].idxmax(), 'Year']

st.markdown(f'''
In **{max_sales_year}** we had <p style="font-size:50px;font-family:bold;">{max_sale} sales</p>, which was <p style="font-size:150px;">{percentage_difference:.2f}%</p> larger than on average!
''', unsafe_allow_html=True)
