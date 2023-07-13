import streamlit as st
import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

with st.columns([2.5,8,1])[1]:
    st.dataframe(df.head(), hide_index=True)
# or st.columns(3)[1].dataframe(df)    

st.markdown('''
## Using the numbers themselves
When presenting/comparing few numbers, often a good idea to present the numbers themselves.
''')

max_sale = df.Sales.max()
mean_sale = df.Sales.mean()
percentage_difference = ((max_sale - mean_sale) / mean_sale) * 100
max_sales_year = df.loc[df['Sales'].idxmax(), 'Year']
st.divider()
st.markdown(f'''
<span style="font-size:25px;">In **{max_sales_year}** we had </span>

<span style="font-size:90px;font-weight:bold;color: #0099ff;">{max_sale} </span><span style="font-size:90px;">sales</span> 

<span style="font-size:25px;"> This was </span><span style="font-size:35px;font-weight:bold;color: #ff6600;">{percentage_difference:.2f}% </span> <span style="font-size:25px;"> larger than average!</span>
''', unsafe_allow_html=True)

st.markdown("## Heatmaps")
st.markdown("A heatmap is an effective visualization technique used to represent tabular data, replacing or supplementing numerical values with colored cells to visually depict the relative magnitudes of the data.")

years = np.arange(2015, 2023)
regions = ['North', 'South', 'East', 'West']
sales_data = np.random.randint(50000, 200000, size=(len(years), len(regions)))

df = pd.DataFrame(sales_data, columns=regions)
df['Year'] = years
df = df.set_index('Year')

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax = sns.heatmap(df, cmap='YlGnBu', annot=True, fmt='.0f', cbar=True)
plt.title('Sales Performance by Year and Region')
ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha='right')
ax.patch.set_alpha(0.5)

st.pyplot(fig)

st.write("To enhance visualization and reduce mental processing, color saturation can be employed as a powerful tool to provide visual cues. By incorporating a heatmap, our eyes and brains can swiftly identify potential points of interest. The varying saturation levels in the heatmap enable quick identification of areas that stand out, allowing for a more efficient analysis and interpretation of the data.")

