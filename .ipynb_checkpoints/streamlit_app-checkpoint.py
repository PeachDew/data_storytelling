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

st.title("Storytelling with Data 🎭📈")

st.dataframe(df, hide_index=True)

st.markdown('''
## Using the numbers themselves
When presenting/comparing few numbers, often a good idea to present the numbers themselves.
''')

max_sale = df.Sales.max()
mean_sale = df.Sales.mean()
percentage_difference = ((max_sale - mean_sale) / mean_sale) * 100
max_sales_year = df.loc[df['Sales'].idxmax(), 'Year']

st.markdown(f'''
In {max_sales_year} we had {max_sale} sakes, which was {percentage_difference.2f}% larger than on average!
''')
