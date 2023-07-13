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
st.divider()

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
fig.patch.set_facecolor("#0B0B43")
fig.patch.set_alpha(1)
plt.title('Sales Performance by Year and Region')
ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha='right')

st.pyplot(fig)

st.write("To enhance visualization and reduce mental processing, color saturation can be employed as a powerful tool to provide visual cues. By incorporating a heatmap, our eyes and brains can swiftly identify potential points of interest. The varying saturation levels in the heatmap enable quick identification of areas that stand out, allowing for a more efficient analysis and interpretation of the data.")

st.markdown("## Scatterplots")
st.markdown("Scatterplots are a powerful tool for visualizing the relationship between two variables. By encoding data on both the horizontal x-axis and the vertical y-axis, scatterplots provide a clear representation of the relationship and allow for insightful analysis. They enable us to examine the presence and nature of the relationship between variables, facilitating the identification of patterns, trends, and correlations in the data.")

iris = sns.load_dataset('iris')

fig2 = sns.pairplot(iris, hue='species', markers=['o', 's', 'D'])
st.columns([1.2,5,1])[1].write("Iris Dataset: Pairwise Relationships among Flower Measurements")
st.pyplot(fig2)

st.markdown("## Lineplots")

flights = sns.load_dataset("flights")
agg_df = flights[['year','passengers']].groupby('year').mean()

years = agg_df.index
passengers = agg_df['passengers']

fig3, ax = plt.subplots()
ax.plot(years, passengers, marker='o')

ax.set_title('Flights Dataset: Passenger Traffic Over the Years')
ax.set_xlabel('Year')
ax.set_ylabel('Passenger Count')

l1, l2 = st.columns(2)
with l2:
    st.markdown("Line graphs are a widely used visualization technique for representing continuous data. They are particularly effective for illustrating trends, patterns, and relationships over a continuous range of values. By connecting the data points with lines, line graphs emphasize the continuity and progression of the data.")
with l1:    
    st.pyplot(fig3)
    
    
data = {
    'Year': [2019, 2020],
    'Apple': [45.3, 48.2],
    'Samsung': [21.2, 20.4],
    'Huawei': [16.3, 14.6],
    'Xiaomi': [9.2, 11.4],
    'OPPO': [4, 5.4]
}


st.markdown("## Slope Graphs")


df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Brand', value_name='MarketShare')


fig, ax = plt.subplots()
sns.lineplot(data=df_melted, x='Year', y='MarketShare', hue='Brand', marker='o')

ax.set_title('Smartphone Market Share: 2019 vs 2020')
ax.set_xlabel('Year')
ax.set_ylabel('Market Share (%)')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xticks([2019,2020])

s1, s2 = st.columns([2,5])
with s2:
    st.pyplot(fig)
with s1:
    st.markdown("Slopegraphs are a valuable visualization technique for comparing two time periods or points of reference and effectively showcasing relative increases, decreases, or differences across various categories.")
    
tips = sns.load_dataset('tips')

avg_total_bill = tips.groupby('day')['total_bill'].mean()
avg_tip_amount = tips.groupby('day')['tip'].mean()


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# non-zero baseline
axes[0].bar(avg_total_bill.index, avg_total_bill, color='blue')
axes[0].bar(avg_tip_amount.index, avg_tip_amount, color='orange')
axes[0].set_title('Average Total Bill and Tip Amount by Day (Baseline Not at Zero)')
axes[0].set_xlabel('Day')
axes[0].set_ylabel('Amount')
axes[0].set_ylim([16, 30])
axes[0].legend(['Total Bill', 'Tip Amount'])

# zero
axes[1].bar(avg_total_bill.index, avg_total_bill, color='blue')
axes[1].bar(avg_tip_amount.index, avg_tip_amount, color='orange')
axes[1].set_title('Average Total Bill and Tip Amount by Day (Baseline at Zero)')
axes[1].set_xlabel('Day')
axes[1].set_ylabel('Amount')
axes[1].legend(['Total Bill', 'Tip Amount'])

# Display the plot using Streamlit
st.pyplot(fig)




